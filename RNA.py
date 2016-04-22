'''
Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.
'''
from DataProcess import validate_base

# transcibe a DNA string into a RNA string
def transcribe(DNA):
	DNA = DNA.upper()
	if not validate_base(DNA):
		return "It is not a DNA string!!"		
    
	RNA = ""
	for nu in DNA:
		if nu == "T":
			RNA += "U"
		else:
			RNA += nu
	return RNA

if __name__ == '__main__':
	with open(input("file input: ")) as f:
 		with open("Output\output_RNA.txt", "w") as o:
 			o.write(transcribe(f.read().rstrip()))