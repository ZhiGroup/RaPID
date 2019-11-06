import unittest
import sys

pos_list = []
pos_set = ()

if (len(sys.argv) < 3):
	print ("Usage:\npython filter_mapping_file.py <input_map_file> <output_file>")
	sys.exit()
	
input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file)
for line in f:
	if ('Position' in line):
		continue
	vals = line.split()
	_pos = int(vals[1])
	if (_pos in pos_set):
		print ("duplicate positions in the file" + "\t" + str(_pos))
		sys.exit(1)
	pos_list.append(_pos)
	
f.close()


f_o = open(output_file,'w+')

def LIS(X):
	n = len(X)
	X = [None] + X 
	M = [None] * (n + 1) 
	P = [None] * (n + 1)
	L = 0
	for i in range(1, n + 1):
		if L == 0 or X[M[1]] >= X[i]:
			j = 0
		else:
			lo = 1 
			hi = L + 1  
			while lo < hi - 1:
				mid = (lo + hi) // 2
				if X[M[mid]] < X[i]:
					lo = mid
				else:
					hi = mid
			j = lo

		P[i] = M[j]
		if j == L or X[i] < X[M[j + 1]]:
			M[j + 1] = i
			L = max(L, j + 1)

	output = []
	pos = M[L]
	while L > 0:
		output.append(X[pos])
		pos = P[pos]
		L -= 1
	output.reverse()
	return output



r = LIS(pos_list)

pos_set = set(r)

f = open(input_file)

for line in f:
	if ('Position' in line):
		continue
	vals = line.split()
	_pos = int(vals[1])
	if (_pos in pos_set):
			f_o.write(line)
f.close()

f_o.close()

