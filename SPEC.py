'''
Given: A list L of n (n≤100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L 
(if multiple solutions exist, you may output any one of them). 
'''
# Build mass table from mass_table.txt
# {mass: amino acid}
def mass_table():
    with open("ProteinMass/mass_table.txt", "r") as table:
        mass = {}
        for line in table:
            lst = line.split("   ")
            mass[round(float(lst[1].rstrip()), 5)] = lst[0]
    return mass
  
# nth prefix - (n - 1)th prefix = the mass of last amino acid
def mass_spec(prefix, mass):
    result = ""
    for i in range(len(prefix) - 1):
        aa_mass = round(abs(prefix[i] - prefix[i + 1]), 5)
        result += mass[aa_mass]

    return result               

if __name__ == "__main__":
    with open("data/rosalind_spec.txt", "r") as f:
        mass = mass_table()
        prefix = []    
        for line in f:
            prefix.append(float(line.rstrip()))
        with open("data/output_spec.txt", "w") as o:
            o.write(mass_spec(prefix,mass))
            print(mass_spec(prefix, mass))
