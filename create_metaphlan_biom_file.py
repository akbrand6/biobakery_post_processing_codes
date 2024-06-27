#!/usr/bin/env python

import os
import pandas as pd
from biom.table import Table
import subprocess

# Function to source the config.sh file and get the main_dir variable
def get_main_dir(config_file):
    command = f'source {config_file} && echo $main_dir'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')
    return result.stdout.strip()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the config.sh file
config_file = os.path.join(script_dir, 'UPDATE_ME.sh')

# Get the main_dir from the config.sh file
main_dir = get_main_dir(config_file)

metaphlan_absabund_file=f"{main_dir}/code-output/metaphlan/metaphlan_absabund.tsv"
output_biom_file=f"{main_dir}/code-output/metaphlan/merged_absabund.json.biom"

def create_biom_table(df,dict_taxa_map):
    '''
    Generate BIOM table from abundance table
    
    Args:
         df (pandas.DataFrame)
         dict_taxa_map (dictionary that maps unique species names to full taxonomic id)

    Notes:
         taxonomic IDs should have the following format, see example
         "k__Eukaryota|p__Basidiomycota|c__Tremellomycetes|o__Tremellales|f__Cryptococcaceae|g__Cryptococcus|s__Cryptococcus_gattii_VGII"
    
    '''
    data = df.values
    sample_ids = df.columns
    observ_ids = df.index.values

    # create metadata
    def break_down_taxa(x): return [ii.split('__')[1] for ii in x.split('|')]
    observ_metadata = [break_down_taxa(dict_taxa_map[ii]) for ii in df.index.values]
    observ_metadata = [{'taxonomy':ii} for ii in observ_metadata]
    observ_metadata

    return Table(data,observ_ids,sample_ids,observ_metadata)

df_abundance = pd.read_csv(metaphlan_absabund_file,sep='\t',header=0,index_col=0,skiprows=0)
df_abundance = df_abundance[df_abundance.index.str.contains(r'\|s__')]
df_abundance = df_abundance[~df_abundance.index.str.contains(r'\|t__')]
ls_species = []

for idx in df_abundance.index.values:
    if '|s__' in idx and '|t__' not in idx:
        ls_species.append(idx.split('|s__')[1].replace('_', ' ', 1))

ls_species = [species for species in ls_species if "|t__" not in species]

# create dictionaries that map species to long taxonomy names, and vice versa
dict_taxa_to_species = {taxa:species for species,taxa in zip(ls_species,df_abundance.index.values)}
dict_species_to_taxa = {species:taxa for species,taxa  in zip(ls_species,df_abundance.index.values)}

# rename row names in data frame
df_abundance = df_abundance.rename(index=dict_taxa_to_species)

## CREATE BIOM FILE
biom_abundance = create_biom_table(df_abundance,dict_species_to_taxa)
fid = open (output_biom_file, 'w')
fid.write(biom_abundance.to_json(generated_by='Andrew Kyle Brand Ardis'))
fid.close()

