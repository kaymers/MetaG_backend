import pandas as pd

lineage = None

def load_to_memory(config):
    global lineage


    if lineage is not None: return
    lineage = {}
    i=0
    file = open(config['rankedlineage_path'].replace('"',''), encoding='utf-8')
    for line in file:
        i += 1
        line_components = [i.replace('\t', '').strip() for i in line.split('|')]
        lineage[int(line_components[0])] = line_components[2:-1]
        if lineage[int(line_components[0])][0] == '': lineage[int(line_components[0])][0] = line_components[1]


def process(config, data):
    load_to_memory(config)
    lineages =  [lineage[x] if x in lineage else ['UNKNOWN']*8 for x in data['taxid']]

    for i in range(8):
        data['lin_'+str(i)] = pd.Series([lineages[x][i] for x in range(data.shape[0])])
