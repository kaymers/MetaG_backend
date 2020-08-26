import threading
import os
import random
import pandas as pd

processed_path = None
map_size = None
map_file_ptr = None
no_of_threads = None
count = None
accessions = None
result = None

def read_key(i):
    map_file_ptr.seek(22 * i)
    return map_file_ptr.read(18)

def read_value(i):
    map_file_ptr.seek(22 * i + 18)
    return int.from_bytes(map_file_ptr.read(4), 'little')

def bin_search(key, a, b):
    if isinstance(key, str) : key = key.encode('ascii')+bytes(18-len(key))
    if b < a : return -1
    mid_point = (a+b)//2
    mid_point_value = read_key(mid_point)
    if key > mid_point_value : return bin_search(key,   mid_point + 1, b)
    if key < mid_point_value : return bin_search(key,   a, mid_point - 1)
    return read_value(mid_point)


def process(config, data):
    global map_size, map_file_ptr, count, accessions, result
    count = data.shape[0]
    accessions = data['accession']
    result = {}
    map_paths = [config['mapper_data_directory'] +'/'+ i for i in config['mapper_data_filenames'].replace('"','').split()]
    for map_path in map_paths:
        map_size = os.path.getsize(map_path) // 22
        map_file_ptr = open(map_path, "rb")

        for i in range (count):
            if i not in result or result[i] == -1:
                if accessions[i] != -1:
                    result[i] = bin_search(accessions[i], 0, map_size)
                else:
                    result[i] = -1

    data['taxid'] = pd.Series([result[x] for x in range(len(data))])





# request = []
# map_file_ptr = open("./mapper_data/nucl_gb", "rb")
# for i in range(3000): request.append(read_key(random.randint(0, 250000000)).decode('ascii').replace('\x00',''))
#
# k = process(request)