from Bio import SeqIO
import pandas as pd

def process(config, path):
    file=SeqIO.parse(path, "fasta")

    sequences = []
    ii=0
    for i in file:
        ii+=1
        if ii%100000==0:print(ii)
        if ii%100==0:sequences.append(str(i.seq))
    print(sequences)
    return pd.DataFrame(sequences, columns=['sequence'])
