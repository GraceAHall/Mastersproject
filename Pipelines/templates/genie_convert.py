#This script converts the output of GENIE3 into a csv file

import numpy as np
import sys
import re

infile = sys.argv[1]
num_genes = int(sys.argv[2])

#This produces a list containing all the values
data = []
with open(infile, 'r') as fp:
    lines = fp.readlines()

for line in lines[1:]:
    #Gets the location of the genes
    location =[loc.start() for loc in re.finditer('Gene', line)]
    #This gives us the gene number
    location = [x+4 for x in location]
    vals = []
    for loc in location:
        current = loc
        gene_ID = ''
        while line[current] != ' ':
            gene_ID = gene_ID + line[current]
            current = current + 1
        vals.append(gene_ID)
    data.append(vals)

matrix = np.zeros((num_genes,num_genes))

#now puts into matrix
for x in data:
    val1 = int(x[0]) - 1
    val2 = int(x[1]) - 1
    matrix[val1][val2] = 1
    matrix[val2][val1] = 1

np.savetxt("matrix_genie.csv", matrix, delimiter=",")
