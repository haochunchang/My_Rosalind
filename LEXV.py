'''
Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜  and a positive integer n.

Return: All strings of length at most n formed from 𝒜, ordered lexicographically.
'''

from itertools import product

# compare according to sdict, return TRUE if s1 < s2
def compare(s1, s2, sdict):
    for i in range(len(s1)):
        if sdict[s1[i]] < sdict[s2[i]]: 
            return True
        elif sdict[s1[i]] > sdict[s2[i]]:
            return False    

# mergesort the list according to sdict
def lexi_sort(perm_list, sdict): 
    result = ["" for x in range(len(perm_list))]
    
    if len(perm_list) == 1:
        return perm_list
    elif len(perm_list) > 1:
        mid = int(len(perm_list) / 2)
        x = lexi_sort(perm_list[:mid], sdict)
        y = lexi_sort(perm_list[mid:], sdict)
        
        i = 0
        j = 0
        k = 0
        while i < len(x) and j < len(y):
            if compare(x[i], y[j], sdict):
                result[k] = x[i]
                i += 1
                k += 1
            elif not compare(x[i], y[j], sdict):
                result[k] = y[j]
                j += 1
                k += 1
        while i < len(x):
            result[k] = x[i]
            i += 1
            k += 1
        while j < len(y):
            result[k] = y[j]
            j += 1
            k += 1
    
    return result

def all_perm(symbol, n):
    perm_list = [] 
    
    # generate all the permutations of length at most n in tuple
    for x in range(1, n + 1):
        for s in product(symbol, repeat = x):
            perm_list.append(str(s))
   
    # process tuple into list of strings
    temp = [""]
    case = 0
    for perm in perm_list:
        for x in range(0, len(perm)):
            if perm[x].isalpha():
                temp[case] += perm[x]
        temp.append("")
        case += 1
    del temp[temp.index("")]            
    perm_list = temp 
    
    # append null symbol to every permutation
    for perm in perm_list:
        if len(perm) < n:
            perm_list[perm_list.index(perm)] += " " * (n - len(perm))
    
    # add null symbol to the top of the symbol table,
    sdict = {" ": 1}
    n = 2
    for s in symbol:
        sdict.update({s: n})
        n += 1

    # sort the perm_list  
    perm_list = lexi_sort(perm_list, sdict)

    return perm_list

if __name__ == "__main__":
    with open("data/rosalind_lexv.txt", "r") as f:
        f = f.readlines()
        symbol = f[0].replace(" ", "").strip("\n")
        n = int(f[1])
        perm_list = all_perm(symbol, n)
        with open("data/output_lexv.txt", "w") as o:    
            for perm in perm_list:
                o.write(perm)
                o.write("\n")






