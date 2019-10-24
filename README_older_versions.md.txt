

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
 