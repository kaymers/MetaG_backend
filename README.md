# MetaG_backend

## Setup dependancies


1. Install dependancies in *requirements.txt*. (pip install -r requirements.txt)

2. Extract all the .rar files in *mapper_data* folder to *mapper_data* folder.

If you do not have blast configured in your machine follow the below steps.

3. Install BLAST+ executables [manual](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download).

4. Add blast+ executables insallation directory to *path*.

5. Create a blast database (or configure a standard database like nt).

### Edit the config.ini (in this repository root)

6. Set blast_db_directory and blast_db_name according to the blast setup in your machine.
Extract rankedlineage.dmp from ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.zip to your machine and set the path for the field *rankedlineage_path* in *config.ini*.

7. You can leave the fields *mapper_data_directory* and *mapper_data_filenames* without change if you follow the instructions for configuring mapper_data in an earlier step.

Backend should be ready to use.

## Usage
You can use the backend by importing *backend.py* and calling *backend.process()* method.
