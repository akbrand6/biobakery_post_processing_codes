#!/bin/bash
#SBATCH --job-name=BioBakery_post_processing
#SBATCH --mail-user=<your_email.bcm.edu>
#SBATCH --mail-type=END,FAIL
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=12G
#SBATCH --time=4:00:00
#SBATCH --error ./logs/post_process.e%j
#SBATCH --output ./logs/post_process.o%j


### This path must be updated to the main directory for the job.  it will be looking for "workflow-output", "code", and "code-output" from this directory
main_dir="PATH/TO/YOUR/MAIN/DIRECTORY"


module load anaconda3/2023.03-1
source activate /mount/britton/kyle/conda_envs/biobakery_env


# You may want to change this path depending on where all of your codes live after pulling from github.  main_dir + this should get you to all of the codes.
cd ${main_dir}/code/biobakery_post_processing_codes

echo "main_dir=$main_dir" > config.sh


echo "Starting BioBakery Post-Processing"

echo "Beginning merge_metaphlan_output.sh"
bash merge_metaphlan_output.sh 2>&1

echo "----------------------------------------------------------------"

echo "Beginning nreads.sh"
bash nreads.sh 2>&1

echo "----------------------------------------------------------------"


echo "Beginning convert_metaphlan_relabs_to_absabund.py"
python convert_metaphlan_relabs_to_absabund.py 2>&1

echo "----------------------------------------------------------------"


echo "Beginning create_metaphlan_biom_file.py"
python create_metaphlan_biom_file.py 2>&1

echo "----------------------------------------------------------------"


echo "Beginning merge_humann_output.sh"
bash merge_humann_output.sh 2>&1

echo "----------------------------------------------------------------"


echo "Beginning renorm_humann_output.sh"
bash renorm_humann_output.sh 2>&1

echo "----------------------------------------------------------------"


echo "Beginning make-unstratified-tables.py"
python 2024-01-24-make-unstratified-tables.py 2>&1

echo "----------------------------------------------------------------"


echo "Beginning tidy-transfer-create-log.sh"
bash tidy-transfer-create-log.sh 2>&1

echo "----------------------------------------------------------------"


echo "Beginning tidy-transfer-read-log.sh"
bash tidy-transfer-read-log.sh 2>&1

echo "----------------------------------------------------------------"


echo "Beginning clean_work_dir.sh"
bash clean_work_dir.sh 2>&1

echo "----------------------------------------------------------------"


echo "All scripts complete"
