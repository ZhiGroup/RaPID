# Random Projection-based IBD Detection (RaPID)

RaPID is an ultra-fast tool for the identification of identity-by-descent segments among genotyped individuals. Simulation results proved that our tool (RaPID) achieves almost linear scaling up to sample size and is orders of magnitude faster than GERMLINE. At the same time, RaPID maintains a detection power and accuracy superiour or comparable to existing mainstream algorithms, GERMLINE and IBDseq. With our tool, it is feasible to identify IBDs in biobank-scale cohorts.

RaPID is free for academic and research use only.  For Commercial Use inquiries, please contact the below authors:
 
Authors: Shaojie Zhang shzhang@cs.ucf.edu, Degui Zhi Degui.Zhi@uth.tmc.edu.


## RaPID (v.1.7):

Minimum cut-off for RaPID v.1.7 is provided only in terms of cM. The input file for this version is compressed VCF file.

Usage:
`./RaPID_v.1.7 -i <input_file_vcf_compressed>  -g <genetic_mapping_file> -d <min_length_in_cM> -o <output_folder>   -w  <window_size>  -r <#runs> -s <#success>`


You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps _4k_1e7.vcf.gz_. The file _4k_1e7_e0.001.g_ contains the genetic mapping for the example file.


To run the program for detecting the IBDs with a minimum length of 5 cM type:

`./RaPID_v.1.7  -i 4k_1e7.vcf.gz -g 4k_1e7_e0.001.g -d 5 -w 250 -r 10 -s 2 -o output_folder`


The program outputs all detected IBD segments in the following format:
<chr_name> <sample_id1> <sample_id2> <hap_id1> <hap_id2> <starting_pos_genomic> <ending_pos_genomic> <genetic_length> <starting_site> <ending_site>


 
Genetic Mapping File Format (tab-delimited):
`<site_number> <genetic_location>`
Each line contains the site index and genetic location of a site, the same order as the VCF input file. Please note that the genetic mapping file should be monotically increasing and the genetic locaion should be provided for each site. We have provided two Python scripts to filter the genetic mapping file and also a python script to interpolate the genetic locaions. 

Usage:


`python filter_mapping_file.py <genetic_map> <filtered_map>` 

`python interpolate_loci.py <filtered_map> <vcf_input_gzip> <output_map_file>`


If the marker density of your data is low, you will have to decrease the window size accordingly. For example, for UK-Biobank, the maker density was 80-10 times less than the attached example, and we used -w 3 instead of 250 for 5 cM minimum target lengths. We have provided a script on to estimate the parameters.

## Citations

1. Naseri, Ardalan, Xiaoming Liu, Kecong Tang, Shaojie Zhang, and Degui Zhi. "RaPID: ultra-fast, powerful, and accurate detection of segments identical by descent (IBD) in biobank-scale cohorts." Genome biology 20, no. 1 (2019): 143; doi: https://doi.org/10.1186/s13059-019-1754-8 

2. Ultra-fast Identity by Descent Detection in Biobank-Scale Cohorts using Positional Burrows-Wheeler Transform
Ardalan Naseri, Xiaoming Liu, Shaojie Zhang, Degui Zhi
bioRxiv 103325; doi: https://doi.org/10.1101/103325
https://www.biorxiv.org/node/29448
