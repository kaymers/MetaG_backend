from backend import process

data=process('/home/sadeepw/Desktop/sample1.fasta', 3, 15, 'sigmoid', [32,3,32],.6, data = data, run_vect = True, run_AE = True, run_blast=False)