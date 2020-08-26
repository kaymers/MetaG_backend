# MetaG_backend

## Configuring
Install dependancies in *requirements.txt*.

Extract .rar files in *mapper_data* to *mapper_data*.

### Edit the config.ini

Set blast_db_directory and blast_db_name according to the blast setup in your machine (you need to have blast in your machine)

Extract rankedlineage.dmp from ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.zip to your machine and set the path for the field *rankedlineage_path* in *config.ini*.

You can leave the fields *mapper_data_directory* and *mapper_data_filenames* without change if you follow the instructions for configuring mapper_data in an earlier step.

Backend should be ready to use.

## Usage
You can use the backend by importing *backend.py* and calling *backend.process()* method.
