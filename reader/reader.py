import time

from Bio import SeqIO
import pandas as pd
from collections import defaultdict
from itertools import product

all_kmers_cache = {}


def reverse_compliment(s):
    reverse_letter = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    return ''.join([reverse_letter[i] for i in s[::-1]])


def all_kmers(k):
    if k in all_kmers_cache: return all_kmers_cache[k]
    all_strings = [''.join(i) for i in product("ACGT", repeat=k)]
    proper_strings = [min(i, reverse_compliment(i)) for i in all_strings]
    unique_kmers = list(set(proper_strings))
    unique_kmers.sort()
    all_kmers_cache[k] = unique_kmers
    return unique_kmers


def vectorize_seq(seq, k=4):
    d = defaultdict(lambda: 0)
    for c in range(len(seq) - k + 1):
        d[seq[c:c + k]] += 1
    return [d[kmer] if kmer == reverse_compliment(kmer) else d[kmer] + d[reverse_compliment(kmer)] for kmer in
            all_kmers(k)]


def process(config, path, k):
    file = SeqIO.parse(path, "fasta")

    sequences = []
    ids = []
    a = []
    c = []
    g = []
    t = []
    count = 0
    for i in file:
        seq_str = str(i.seq)
        sequences.append(vectorize_seq(seq_str, k))
        ids.append(count)
        a.append(seq_str.count('A') + seq_str.count('a'))
        c.append(seq_str.count('C') + seq_str.count('c'))
        g.append(seq_str.count('G') + seq_str.count('g'))
        t.append(seq_str.count('T') + seq_str.count('t'))
        if count % 10000 == 0:
            print("Reading & Vectorizing seq", count, time.strftime('%X'))
        #if count == 100000: break
        count += 1

    data = pd.DataFrame(ids, columns=['id'])
    data['vector'] = data['id'].map(lambda x: sequences[x])
    data['a'] = data['id'].map(lambda x: a[x])
    data['c'] = data['id'].map(lambda x: c[x])
    data['g'] = data['id'].map(lambda x: g[x])
    data['t'] = data['id'].map(lambda x: t[x])
    print("Reading & Vectorizing done",time.strftime('%X'))
    print('loaded & vectorized input file')
    return data
