# biobakery_post_processing_codes

This is a set of codes used each time after our biobakery nextflow pipeline is completed. Each code is easy to run and most are pretty quick.

### Changes needed

This set of code is intended to run **IN ORDER**.  The order is found in the README.tsv  I always update the README.tsv as I run the codes, to ensure I don't do something stupid.

The proper order is:
1. Update `UPDATE_ME.sh`.  This should be the main directory that branches out into workflow-output and code-output.    The codes are setup to be run based off of the formats we have them. spelling matters.  from the main_dir found in UPDATE_ME.sh you should see `code  code-output  workflow  workflow-output`
2. `merge_metaphlan_output.sh`
3. `nreads.sh`
4. `convert_metaphlan_relabs_to_absabund.py`
5. `create_metaphlan_biom_file.py`
6. `merge_human_output.sh`
7. `renorm_humann_output.sh`
8. `2024-01-24-make-unstratified-tables.py`
9. `tidy-transfer-create-log.sh`
10. `tidy-transfer-read-log.sh`
11. `clean_work_dir.sh`

**The codes should be run in order**

Before running these codes you will need to activate a biobakery conda environment.  Specifically for merging metaphlan and humann.

**The codes should be run in order**

Code number **1** is literally only the input directory.  If your biobakery environment is loaded, this should be the *only* thing you change. 

Code numbers **2, 3, 4, and 5** are all for **Metaphlan**

Code numbers **6, 7, and 8** are all for **Humann**

Code numbers **9 and 10** are to help with nextflows outputs being symbolic links.  These are not required, but we find the very helpful.  9 will create a log file, which I visually check to make sure I'm not unswapping what should be swapped. and 10 reads that log file.

Code number **11** will clean up the copies of fastq.gz files that are hidden in the work folders.  Be careful with this one, it does make a log of everything deleted, but it is mean to delete a lot of things. We usually see our directories going from a few Gigs of memory, to a few Megs.  This is important to do, Just be careful.

**The codes should be run in order**


The outputs will be found in `code-output` and organized in a fairly straightfoward way; by metaphlan and humann. 

Best of luck.

-AKBA
