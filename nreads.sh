#!/bin/bash

source "$(dirname "$0")/config.sh"

pattern1="#[0-9]\+ reads processed"
pattern2="[0-9]\+"

file_path="${main_dir}/workflow-output/metaphlan" # this is a folder with all of your individual metaphlan files
nreads="${main_dir}/code-output/metaphlan/nreads.txt" # this will be a file that this script will write

touch "$nreads" 
echo -e "Sample\tNumberReads" >> "$nreads" # Use -e to enable interpretation of escape sequences

for i in "${file_path}"/*_profile.tsv; do 
  sample=$(basename "$i" | sed 's/_profile.tsv$//')
  echo -n "${sample}" >> "$nreads"
  number=$(cat "${i}" | grep -o "$pattern1" | grep -o "$pattern2")
  echo -e "\t${number}" >> "$nreads"
done