#!/usr/bin/env python

import os
import pandas as pd
import numpy as np
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

metaphlan_relabun_file=f"{main_dir}/code-output/metaphlan/metaphlan_relabund.tsv"
nread_file=f"{main_dir}/code-output/metaphlan/nreads.txt"
output_file=f"{main_dir}/code-output/metaphlan/metaphlan_absabund.tsv"



df_abundance = pd.read_csv(metaphlan_relabun_file, sep='\t', header=0, skiprows=1,index_col=0)
nreads = pd.read_csv(nread_file, sep='\t',header=0,index_col=0)
df_abundance = df_abundance / 100.0
df_absolutes = df_abundance*nreads.loc[df_abundance.columns,:].T.values
df_absolutes = df_absolutes.round().astype(int)
df_absolutes.to_csv(output_file, sep='\t',header=True,index=True)

print(f'absolute abundance file created in {output_file}')
