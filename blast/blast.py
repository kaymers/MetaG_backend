from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
from io import StringIO
import pandas as pd




def process(config, data, input_fasta_path):
    blast_db = '"' + config['blast_db_directory'].replace('"','') + "/" + config['blast_db_name'].replace('"','') + '"'
    input_fasta_path = '"'+str(input_fasta_path)+'"'
    blastn_results_xml = NcbiblastnCommandline(cmd='blastn', query=input_fasta_path, db=blast_db, outfmt=5, )()
    blastn_results = NCBIXML.parse(StringIO(blastn_results_xml[0]))

    results_accessions = []
    for i in blastn_results:
        try:
            accession = i.alignments[0].accession
        except:
            accession = -1

        results_accessions.append(accession)

    data['accession'] = pd.Series(results_accessions)
    print('blast done')
