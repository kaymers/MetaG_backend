import pytest

import os
import sys
import pandas as pd
import configparser as cp

from backend import parse_config

backend_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(backend_path)
config_path = backend_path+'/config.ini'
config = parse_config(config_path)


from vectorizer.vectorizer import reverse_compliment, vectorize_seq, all_kmers, process


# vectorizer_reverse_compliment

def test_vectorizer_reverse_compliment_1():
    assert reverse_compliment('ACGT') == 'ACGT'


def test_vectorizer_reverse_compliment_2():
    assert reverse_compliment('ACGTCCATAAAAAA') == 'TTTTTTATGGACGT'


def test_vectorizer_reverse_compliment_3():
    assert reverse_compliment(
        'ACGTCCATAAAAAAAAAACCCCCTGAGAGAGAGACCTCTCTCGTA') == 'TACGAGAGAGGTCTCTCTCTCAGGGGGTTTTTTTTTTATGGACGT'


def test_vectorizer_reverse_compliment_4():
    assert reverse_compliment('AAAAGT') == 'ACTTTT'


# vectorizer_vectorize_seq

def test_vectorizer_vectorize_seq_1():
    assert vectorize_seq("AACTAAAAAAGAACGGTAA") == [3, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                                                    0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                    0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_vectorizer_vectorize_seq_2():
    assert vectorize_seq("ACCCTTAAAGGGAGAGAGTTCAGTGGGTCCCACGTATTCGGATATCGAGGGGAGGGTCTAG") == [0, 0, 1, 0, 0, 0, 0, 1, 0,
                                                                                              0, 2, 0, 1, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 3, 0, 0, 0, 0, 0,
                                                                                              1, 0, 1, 1, 0, 1, 2, 0, 0,
                                                                                              0, 0, 0, 0, 0, 4, 0, 0, 1,
                                                                                              0, 1, 0, 1, 0, 1, 1, 0, 0,
                                                                                              0, 0, 1, 0, 0, 0, 0, 0, 0,
                                                                                              1, 0, 0, 0, 0, 0, 0, 0, 2,
                                                                                              0, 2, 1, 0, 1, 0, 0, 0, 2,
                                                                                              1, 0, 1, 0, 0, 0, 1, 0, 1,
                                                                                              0, 0, 0, 1, 0, 2, 1, 0, 1,
                                                                                              0, 0, 1, 0, 2, 2, 0, 2, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 1,
                                                                                              0, 0, 3, 0, 0, 0, 0, 0, 0,
                                                                                              1, 0, 1, 0, 0, 0, 1, 1, 0,
                                                                                              1]


def test_vectorizer_vectorize_seq_3():
    assert vectorize_seq("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT") == [58, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                              0, 0]


def test_vectorizer_vectorize_seq_4():
    assert vectorize_seq("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTCTTTTTTTTTTTTTTTTTT") == [55, 0, 1, 0, 0, 0, 0, 0,
                                                                                               1, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 1,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 1, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0,
                                                                                               0, 0, 0, 0, 0, 0, 0, 0]


# vectorizer_all_kmers

def test_vectorizer_all_kmers_1_3mers():
    assert 'AAT' in all_kmers(3)
    assert 'ACT' in all_kmers(3)
    assert 'CCC' in all_kmers(3)
    assert 'GAA' in all_kmers(3)
    assert 'GAT' not in all_kmers(3)


def test_vectorizer_all_kmers_2_4mers():
    assert 'AATC' in all_kmers(4)
    assert 'ACGT' in all_kmers(4)
    assert 'CGCC' in all_kmers(4)
    assert 'GGCA' in all_kmers(4)
    assert 'TATC' not in all_kmers(4)


# vectorizer_process

def test_vectorizer_process_1():
    df = pd.DataFrame([{'sequence': "ACGTACGATCTACTGACGATATCG"}])
    process(None, df, 4)
    assert df['vector'][0] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0,
                               1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                               1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


def test_vectorizer_process_2():
    df = pd.DataFrame([{'sequence': "ACGTGTGTGTTGTGACACACAAAAAAAAACGGCGCGCGGGGGGCGTATTATTGC"}])
    process(None, df, 4)
    assert df['vector'][0] == [6, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1,
                               0, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_vectorizer_process_3():
    df = pd.DataFrame([{'sequence': "AAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCGGGGGGGGGTTTTTTTTTTT"}])
    process(None, df, 4)
    assert df['vector'][0] == [19, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_vectorizer_process_4():
    df = pd.DataFrame([{'sequence': "AAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCGGGGGGGGGTTTTTTTTTTT"}])
    process(None, df, 3)
    assert df['vector'][0] == [21, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

