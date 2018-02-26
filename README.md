# Random Projection-based IBD Detection (RaPID)
    
The RaPID Technology is based on Richard Durbin’s PBWT (richarddurbin/pbwt). RaPID is free for academic and research use only. This allowance excludes the use and/or re-use of any portion of RaPID for any Commercial Use. The term “Commercial Use” means use of RaPID, including without limitation, for direct or indirect financial, commercial, or strategic gain or advantage, including, without limitation: (a) bundling or integrating RaPID, in any format, with any hardware product and/or another software product or printed and/or electronic materials for transfer, sale, or license to a third party; (b) providing third parties with any part of RaPID for use with hardware or another software product or printed and/or electronic materials purchased by that third party; or (c) use in connection with the performance of services for which the user is compensated.
 
For Commercial Use inquiries, please contact the below authors:
 
Authors: Ardalan Naseri, Xiaoming Liu, Shaojie Zhang shzhang@cs.ucf.edu, Degui Zhi Degui.Zhi@uth.tmc.edu.

## Example (v.1.6):
You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder.

To run the program for detecting the IBDs with a minimum length of 3 Mbps type:

`RaPID_v.1.2 -i 4k_1e8_e0.0025.vcf.gz -o output -r 10 -w 0.005 -s 2 -l 3.0 -g genetic_map_4k.map`


The program outputs all detected IBD segments in the following format:
MATCH <sample_id1> <sample_id2> <starting_position> <ending_position> <length>
<starting_position> denotes the genomic start of the IBD segment. <ending_position> denotes the end of the IBD segments, respectively.

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
