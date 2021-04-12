import configparser as cp
import os
import sys

backend_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(backend_path)

from mapper import mapper_search
from taxonomy import taxonomy
from blast import blast
from vectorizer import vectorizer
from gc_counter import gc_counter
from autoencoder import autoencoder
from reader import reader


def process(input_fasta_path, k, epochs, activation, layers_sizes, train_perc, run_vect, run_AE,
            run_blast, data=None, config_path=backend_path + '/config.ini'
            ):
    config = parse_config(config_path)

    data = reader.process(config, input_fasta_path, k)
    print('loaded & vectorized input file')

    print('gc count done')
    # blast.process(config, data, input_fasta_path)
    # print('blast done')
    # mapper_search.process(config, data)
    # print('mapping done')
    # taxonomy.process(config, data)
    autoencoder.process(config, data, epochs, activation, layers_sizes, train_perc)
    # data.drop('sequence', axis=1, inplace=True)
    # data.drop('vector', axis=1, inplace=True)
    return data


def process_ae(input_fasta_path, k, epochs, activation, layers_sizes, train_perc, data,
               config_path=backend_path + '/config.ini'):
    config = parse_config(config_path)

    sequences = reader.process(config, input_fasta_path)
    data['sequence'] = sequences['sequence']
    print('loaded input file')
    vectorizer.process(config, data, k)
    print('vectorizing done')
    autoencoder.process(config, data, epochs, activation, layers_sizes, train_perc)
    data.drop('sequence', axis=1, inplace=True)
    data.drop('vector', axis=1, inplace=True)
    return data


def parse_config(config_path):
    configparser = cp.ConfigParser()
    configparser.read_string('[dummy_section]\n' + open(config_path, 'r').read())
    config = configparser['dummy_section']
    for key in [i[0] for i in config.items()]:
        config[key] = config[key].replace("{BACKEND_PATH}", backend_path)
    return config
