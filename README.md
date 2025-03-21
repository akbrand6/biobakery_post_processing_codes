# biobakery_post_processing_codes

This is a set of codes used each time after our biobakery nextflow pipeline is completed. The UPDATE_AND_RUNME.sh file should be opened, and the **email address** and **path to your main directory *must* be updated**. 
Sbatch UPDATE_AND_RUNME.sh, and it should run the post-processing codes below for you.  

### Notes about what the individual steps are and how they work:

This set of code is intended to run **IN ORDER**.  The order is seen below.  I used to run them all one by one and update a file (that no longer exists here) named README.tsv as I run the codes, to ensure I don't do accidentally mess something up. More recently I learned how to run them all in order and recognize the value of removing the opportunity of human error. 

The proper order is:
1. `UPDATE_AND_RUNME.sh`.  
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



Code number **1** is the only one that needs updating and/or running. **Update the `main_dir`** to be the main directory that branches out into `code-output`, and `workflow-output`.  
Previously we recommending having a 'workflow' and 'code directory present as well. But, nothing interact with `workflow` at any point. and as long as line 22 in UPDATE_AND_RUNME.sh is properly formatted, it doesn't matter if you have `code`, or go straight to ${main_dir}/biobakery_post_processing_codes. But that is up to you. 
The important part is, it will read the outputs from biobakery in `workflow-output` and write files into `code-output`.

Code numbers **2, 3, 4, and 5** are all for **Metaphlan**

Code numbers **6, 7, and 8** are all for **Humann**

Code numbers **9 and 10** are to help with nextflows outputs being symbolic links.  These are not required, but we find the very helpful.  9 will create a log file, which I visually check to make sure I'm not unswapping what should be swapped. and 10 reads that log file.

Code number **11** will clean up the copies of fastq.gz files that are hidden in the work folders.  Be careful with this one, it does make a log of everything deleted, but it is mean to delete a lot of things. We usually see our directories going from a few Gigs of memory, to a few Megs.  This is important to do, Just be careful.


The outputs will be found in `code-output` and organized in a fairly straightfoward way; by metaphlan and humann. 

Best of luck.

-AKBA
