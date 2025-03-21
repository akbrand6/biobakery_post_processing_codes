#!/usr/bin/env python

import os
import re
import numpy as np
import pandas as pd
import subprocess

# Function to source the config.sh file and get the main_dir variable
def get_main_dir(config_file):
    command = f'source {config_file} && echo $main_dir'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')
    return result.stdout.strip()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the config.sh file
config_file = os.path.join(script_dir, 'config.sh')

# Get the main_dir from the config.sh file
main_dir = get_main_dir(config_file)


def unstratify(df):
    '''
    params
        (pd.DataFrame) features x samples
    return
        (pd.DataFrame) unstratified
        (pd.DataFrame) stratified
    '''

    pattern = r"\|s__|\|g__|\|unclassified|UNINTEGRATED|UNMAPPED|UNGROUPED"

    # get list of features, unstratified only
    ls_features = df.index.values
    ls_features_unstratified = [feature for feature in ls_features if not re.search(pattern, feature)]
    ls_features_stratified = list(set(ls_features).difference(set(ls_features_unstratified)))
    
    # subset dataframe
    df_unstratified = df.loc[ls_features_unstratified,:].sort_index()
    df_stratified = df.loc[ls_features_stratified,:].sort_index()

    return df_unstratified, df_stratified

dir_work = f"{main_dir}/code-output"
dir_input = f"{dir_work}/humann/merged/formatted/"
dir_output = f"{dir_work}/humann/processed/"

for category in ['pathabundance','ecs','kos','pfams','genefamilies']:

    path_output = f"{dir_output}/{category}"
    if not os.path.exists(path_output): os.makedirs(path_output)
    
    for suffix in ['rpk','cpm','relab']:

        key = f"{category}_{suffix}"
        print(f"PROCESSING: {key}")
        
        filepath = f"{dir_input}/{suffix}/{key}.tsv"
        df_category = pd.read_csv(filepath,sep="\t",index_col=0,header=0)
        df_category.columns = [ii.split('_Abundance')[0] for ii in df_category.columns]

        df_unstratified, df_stratified = unstratify(df_category)
        
        path_unstratified = f"{dir_output}/{category}/{key}_unstratified.tsv"
        path_stratified = f"{dir_output}/{category}/{key}_stratified.tsv"
    
        dfs_to_write = [
            (df_unstratified, path_unstratified),
            (df_stratified, path_stratified)
        ]
        
        for df,filepath in dfs_to_write: 
            if df is not None: df.to_csv(filepath,sep="\t",header=True,index=True)
