#!/bin/bash

source "$(dirname "$0")/UPDATE_ME.sh"

work_dir="${main_dir}/code-output"

mkdir -p ${work_dir}/humann/merged/formatted
mkdir -p ${work_dir}/humann/merged/formatted/rpk
mkdir -p ${work_dir}/humann/merged/formatted/cpm
mkdir -p ${work_dir}/humann/merged/formatted/relab

cd $work_dir

declare -a FILETYPES

FILETYPES=( 'genefamilies' 'pathcoverage' 'pathabundance' )
for i in ${FILETYPES[@]}; do
  cp ${work_dir}/humann/merged/main/${i}.tsv ${work_dir}/humann/merged/formatted/rpk/${i}_rpk.tsv 
  humann_renorm_table -i ${work_dir}/humann/merged/main/${i}.tsv -u cpm -o ${work_dir}/humann/merged/formatted/cpm/${i}_cpm.tsv 
  humann_renorm_table -i ${work_dir}/humann/merged/main/${i}.tsv -u relab -o ${work_dir}/humann/merged/formatted/relab/${i}_relab.tsv 
  done

FILETYPES=( 'ecs_rename' 'kos_rename' 'pfams_rename' )
for i in ${FILETYPES[@]}; do
  filename=$(echo $i| cut -d'_' -f1)
  cp ${work_dir}/humann/merged/rename/${i}.tsv ${work_dir}/humann/merged/formatted/rpk/${filename}_rpk.tsv 
  humann_renorm_table -i ${work_dir}/humann/merged/rename/${i}.tsv -u cpm -o ${work_dir}/humann/merged/formatted/cpm/${filename}_cpm.tsv 
  humann_renorm_table -i ${work_dir}/humann/merged/rename/${i}.tsv -u relab -o ${work_dir}/humann/merged/formatted/relab/${filename}_relab.tsv 
  done