# Random Projection-based IBD Detection (RaPID)

RaPID is an ultra-fast tool for the identification of identity-by-descent segments among genotyped individuals. Simulation results proved that our tool (RaPID) achieves almost linear scaling up to sample size and is orders of magnitude faster than GERMLINE. At the same time, RaPID maintains a detection power and accuracy superiour or comparable to existing mainstream algorithms, GERMLINE and IBDseq. With our tool, it is feasible to identify IBDs in biobank-scale cohorts.


*The RaPID Technology is based on Richard Durbin’s PBWT (richarddurbin/pbwt). RaPID is free for academic and research use only. This allowance excludes the use and/or re-use of any portion of RaPID for any Commercial Use. The term “Commercial Use” means use of RaPID, including without limitation, for direct or indirect financial, commercial, or strategic gain or advantage, including, without limitation: (a) bundling or integrating RaPID, in any format, with any hardware product and/or another software product or printed and/or electronic materials for transfer, sale, or license to a third party; (b) providing third parties with any part of RaPID for use with hardware or another software product or printed and/or electronic materials purchased by that third party; or (c) use in connection with the performance of services for which the user is compensated.*

*The source code of the RaPID version 1.2.3 is released under the GNU General Public License version 2 (https://opensource.org/licenses/GPL-2.0).*
 
For Commercial Use inquiries, please contact the below authors:
 
Authors: Ardalan Naseri, Xiaoming Liu, Shaojie Zhang shzhang@cs.ucf.edu, Degui Zhi Degui.Zhi@uth.tmc.edu.


## RaPID (v.1.7):

Minimum cut-off for RaPID v.1.7 is provided only in terms of cM. The input file for this version is compressed VCF file.

Usage:
`./RaPID_v.1.2.4 -i <input_file_vcf_compressed>  -g <genetic_mapping_file> -d <min_length_in_cM> -o <output_folder>   -w  <window_size>  -r <#runs> -s <#success>`


You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder _4k_1e8_e0.0025.vcf.gz_. The file 4k_1e7_e0.001.g contains the genetic mapping for the example VCF file.


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


## Example (v.1.2.3):
You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder. Unzip the file using:

`gunzip 4k_1e7_e0.001.tar.gz`

`tar -xvf 4k_1e7_e0.001.tar`

You can also find the genetic mapping file for the dataset in the examples folder (4k_1e7_e0.001.g)

To run the program for detecting the IBDs with a minimum length of 1.5 Mbps type:

`RaPID_v.1.2.3 -i 4k_1e7_e0.001 -o output -r 10 -w 80 -s 2 -l 1500000 -t 10000000 -d 1.5 -g 4k_1e7_e0.001.g`
<br/>
-l Specify the minimum lengths of the IBD segment in terms of genomic distance and <br/>
-d Specify the minimum length in terms of genetic distance.
<br/>
<br/>
The program outputs all detected IBD segments in the following format:
MATCH <hap1_index> <hap2_index> <starting_position> <ending_position> <length>
<starting_position> denotes the start of the IBD segments in terms of variant sites. <ending_position> denotes the end of the IBD segments, respectively.
 

## Example (v.1.6): (deprecated)
You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder _4k_1e8_e0.0025.vcf.gz_.

To run the program for detecting the IBDs with a minimum length of 3 Mbps type:

`RaPID_v.1.6 -i 4k_1e8_e0.0025.vcf.gz -o output -r 10 -w 0.02 -s 2 -l 3.0 -g genetic_map_4k.map`


The program outputs all detected IBD segments in the following format:
MATCH <sample_id1> <sample_id2> <starting_position> <ending_position> <length>. <starting_position> denotes the genomic start of the IBD segment. <ending_position> denotes the end of the IBD segments, respectively.

The file genetic_map_4k.map contains the genetic mapping. In addition, a mask file can be provided with the tag -x for skipping certain regions.
The folder _genetic\_maps_ contains the genetic mapping files for hg19, hg38. The folder _mask\_file_ contains the mask files for two chromosomes (chr2 and chr15) in hg19 and hg38. 


## Example (v.1.2):
You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder. Unzip the file using:

`gunzip 4k_1e7_e0.001.tar.gz`

`tar -xvf 4k_1e7_e0.001.tar`

To run the program for detecting the IBDs with a minimum length of 3 Mbps type:

`RaPID_v.1.2 -i 4k_1e7_e0.001 -o output -r 10 -w 150 -s 2 -l 3.0 -t 10`

The program outputs all detected IBD segments in the following format:
MATCH <hap1_index> <hap2_index> <starting_position> <ending_position> <length>
<starting_position> denotes the start of the IBD segments in terms of variant sites. <ending_position> denotes the end of the IBD segments, respectively.
 
## Citations

Ultra-fast Identity by Descent Detection in Biobank-Scale Cohorts using Positional Burrows-Wheeler Transform
Ardalan Naseri, Xiaoming Liu, Shaojie Zhang, Degui Zhi
bioRxiv 103325; doi: https://doi.org/10.1101/103325
https://www.biorxiv.org/node/29448
