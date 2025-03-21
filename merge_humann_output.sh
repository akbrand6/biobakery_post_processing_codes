#!/bin/bash

source "$(dirname "$0")/config.sh"

input_dir="${main_dir}/workflow-output"
output_dir="${main_dir}/code-output"

mkdir -p ${output_dir}/humann/merged/main
mkdir -p ${output_dir}/humann/merged/regroup
mkdir -p ${output_dir}/humann/merged/rename

cd $input_dir

declare -a FILETYPES

FILETYPES=( 'genefamilies' 'pathcoverage' 'pathabundance' )
for i in ${FILETYPES[@]}; do
  humann_join_tables -i ${input_dir}/humann/main/ -o ${output_dir}/humann/merged/main/${i}.tsv --file_name "$i" -v
  done

FILETYPES=( 'ecs' 'kos' 'pfams' )
for i in ${FILETYPES[@]}; do
  humann_join_tables -i ${input_dir}/humann/regroup/ -o ${output_dir}/humann/merged/regroup/${i}.tsv --file_name "$i" -v
  done

FILETYPES=( 'ecs_rename' 'kos_rename' 'pfams_rename' )
for i in ${FILETYPES[@]}; do
  humann_join_tables -i ${input_dir}/humann/rename/ -o ${output_dir}/humann/merged/rename/${i}.tsv --file_name "$i" -v
  done