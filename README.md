# Random Projection-based IBD Detection (RaPID)
    
RaPID is free for academic use. For commercial use, please contact authors.
RaPID is based on Richard Durbin's PBWT (richarddurbin/pbwt).

Authors: Ardalan Naseri, Xiaoming Liu, Shaojie Zhang <shzhang@cs.ucf.edu>, Degui Zhi <Degui.Zhi@uth.tmc.edu>



## Example:
You can find an example of a panel with 4000 haplotypes with the chromosome length of 10 Mbps in the examples folder. Unzip the file using:

`gunzip 4k_1e7_e0.001.tar.gz`

`tar -xvf 4k_1e7_e0.001.tar`

To run the program for detecting the IBDs with a minimum length of 3 Mbps type:

`RaPID_v.1.2 -i 4k_1e7_e0.001 -o output -r 10 -w 150 -s 2 -l 3.0 -t 10`

The program outputs all detected IBD segments in the following format:
MATCH <hap1_index> <hap2_index> <starting_position> <ending_position> <length>
<starting_position> denotes the start of the IBD segments in terms of variant sites. <ending_position> denotes the end of the IBD segments, respectively.
