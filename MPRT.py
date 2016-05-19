'''
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
'''
'''
[XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}
'''
from urllib.request import urlretrieve
import glob
from Bio import SeqIO 

# search the input file, and convert the access IDs from uniprot to rosalind's given IDs 
def given_id(ref, key):
    key_list = key.split("|")
    
    for line in ref:
        if key_list[1] == line.rstrip():
            return key_list[1]
        elif (key_list[1] + "_" + key_list[2]) == line.rstrip():        
            return key_list[1] + "_" + key_list[2]
     

# download uniprot data using access IDs and combine into a single file, "input_mprt.txt"
def file_process():
    with open("data/rosalind_mprt.txt", "r") as f:
       # download data into seperate files as fasta format
       n = 1
       for uniprot_id in f:
           url = "http://www.uniprot.org/uniprot/" + uniprot_id.rstrip() + ".fasta"  
           urlretrieve(url, "uniprot/uniprot" + str(n) + ".txt")
           n += 1

    # combine multiple file into a single file
    read_files = glob.glob("uniprot/*.txt")
    with open("uniprot/input_mprt.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

# find and print the location of N-glycosylation motif from "input_mprt.txt"
def find_motif(data):
    motif_dic = {}
    ref = open("data/rosalind_mprt.txt", "r").readlines()

    for key, value in data.items():
        key = given_id(ref, key)   
        # search for motif
        for x in range(0, len(value.seq) - 4):
            if (value.seq[x] == "N" and value.seq[x + 1] != "P") and value.seq[x + 3] != "P":
                if value.seq[x + 2] == "S" or value.seq[x + 2] == "T":
                    if key in motif_dic:
                        motif_dic[key] += str(x + 1) + " "
                    else:
                        motif_dic.update({key: str(x + 1) + " "})
    
    return motif_dic

if __name__ == "__main__":
    file_process()
    record_dict = SeqIO.index("uniprot/input_mprt.txt", "fasta")
    motif = find_motif(record_dict)
    with open("data/output_mprt.txt", "w") as o:
        for key, value in motif.items():
            o.write(key + "\n")
            o.write(value + "\n")

