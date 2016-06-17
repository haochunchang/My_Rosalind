'''
Given: A collection of n weighted trees (n≤40) in Newick format, with each tree containing at most 200 nodes; 
each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n
numbers, for which the kth number represents the distance between xk and yk in Tk.
'''


from Bio import Phylo

def weighted_distance(trees, nodes):
    num = 0
    result = ""
    for tree in trees:
        dis = int(tree.distance(nodes[num][0], nodes[num][1]))
        result += str(dis) + " " 
        num += 1
    return result
    
if __name__ == "__main__":
    with open("data/rosalind_nkew.txt", "r") as f:
        trees = []
        nodes = []
        for line in f:
            if line[0] != "(" and not line.isspace():
                add = line.rstrip().split(" ")
                nodes.append(add)
            else:
                trees.append(line.rstrip()) 

        with open("data/nkew_trees.txt", "w") as w:
            for tree in trees:
                w.write(tree)
                w.write("\n")
        
        trees = Phylo.parse("data/nkew_trees.txt", "newick")
        with open("data/output_nkew.txt", "w") as o:
            result = weighted_distance(trees, nodes)
            print(result)
            o.write(result)
