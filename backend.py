import configparser as cp
import os
import sys

backend_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(backend_path)

from mapper import mapper_search
from taxonomy import taxonomy
from blast import blast
from autoencoder import autoencoder
from reader import reader


def process(input_fasta_path, k, epochs, activation, layers_sizes, train_perc, run_vect=True, run_AE=True,
            run_blast=True, data=None, config_path=backend_path + '/config.ini'
            ):
    print("backend pipeline started")
    config = parse_config(config_path)

    if data is None:
        vectors_acgt = reader.process(config, input_fasta_path, k)
        data = vectors_acgt
    elif run_vect:
        vectors_acgt = reader.process(config, input_fasta_path, k)
        data['vector'] = vectors_acgt['vector']
        data['a'] = vectors_acgt['a']
        data['c'] = vectors_acgt['c']
        data['g'] = vectors_acgt['g']
        data['t'] = vectors_acgt['t']

    if run_blast:
        blast.process(config, data, input_fasta_path)
        mapper_search.process(config, data)
        taxonomy.process(config, data)


    if run_AE:
        autoencoder.process(config, data, epochs, activation, layers_sizes, train_perc)

    print("backend pipeline completed")
    return data

def parse_config(config_path):
    configparser = cp.ConfigParser()
    configparser.read_string('[dummy_section]\n' + open(config_path, 'r').read())
    config = configparser['dummy_section']
    for key in [i[0] for i in config.items()]:
        config[key] = config[key].replace("{BACKEND_PATH}", backend_path)
    return config
