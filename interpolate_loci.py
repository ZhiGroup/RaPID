
import gzip
import sys

import numpy

if (len(sys.argv) < 3):
	print ("Usage:\npython interpolate_loci.py <input_map_file> <vcf_input_gzip> <output_file>")
	sys.exit()
	
map_filepath = sys.argv[1]

vcf_input = sys.argv[2] 
output_file = sys.argv[3]

f = gzip.open(vcf_input)
_started = False

_sites = []
for line in f:
	if (_started):
		vals = line[0:1000].split()
		_sites.append(int(vals[1]))
	elif ("#CHROM" in line[0:1000]):
		_started = True
f.close()


f = open(map_filepath)

f_o = open(output_file,'w+')

xp = []
yp = []

for line in f:
	vals = line.split()
	xp.append(int(vals[1]))
	yp.append(float(vals[len(vals)-1]))

_output_vals =numpy.interp(_sites,xp,yp)

for i in range(0,len(_output_vals)):
	f_o.write(str(i)+ "\t" + str(_output_vals[i]) + "\n")



f.close()
f_o.close()
