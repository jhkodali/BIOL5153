#! /usr/bin/python3

import re
import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='this script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
    
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    
    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        start = int(line[3])
        end = int(line[4])
        strand = line[6]
        feature = line[8]  
        species = line[-1]

        gene_name = re.findall(r'[a-z]{3}[0-9]{1,2}', feature)
       

        #rev_comp function
        if strand == "-":
            print(genome.reverse_complement())
        else:
            print(genome)

        #if re.search(r"exon", reader):
         #   print(genome)
        exon_pres = re.findall(r"exon", feature)
        print(exon_pres)
        # extract the sequence 
        #if exon_pres == 0:
        #    seq_feature = '>' + str(species) + '\n' + str(gene_name) #+ '\n' + genome.id + '\n' + feature
         #   seq_feature = seq_feature + '\n' + genome.seq[start-1:start-1]
        #else:
            #seq_feature = genome.seq[start-1:end-1] + '\n' + feature
            #print(seq_feature)