#!/bin/bash

source "$(dirname "$0")/UPDATE_ME.sh"

input_dir="${main_dir}/workflow-output/metaphlan"
output_dir="${main_dir}/code-output"

mkdir -p "${output_dir}/metaphlan"

cd $input_dir
merge_metaphlan_tables.py *profile.tsv -o ${output_dir}/metaphlan/metaphlan_relabund.tsv --overwrite
