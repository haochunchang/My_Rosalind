'''
Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes; 
each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, 
for which the kth integer represents the distance between xk and yk in Tk.
'''

from Bio import Phylo

def distance(trees, nodes):
    num = 0
    result = ""
    for tree in trees:
        ancestor = tree.common_ancestor(nodes[num][0], nodes[num][1])
        newtree = Phylo.BaseTree.Tree.from_clade(ancestor)
        dis_root1 = len(newtree.get_path(nodes[num][0]))
        dis_root2 = len(newtree.get_path(nodes[num][1]))
        dis = dis_root1 + dis_root2
        result += str(dis) + " " 
        num += 1
    return result
    
if __name__ == "__main__":
    with open("data/rosalind_nwck.txt", "r") as f:
        trees = []
        nodes = []
        for line in f:
            if line[0] != "(" and not line.isspace():
                add = line.rstrip().split(" ")
                nodes.append(add)
            else:
                trees.append(line.rstrip()) 

        with open("data/nwck_trees.txt", "w") as w:
            for tree in trees:
                w.write(tree)
                w.write("\n")
        
        trees = Phylo.parse("data/nwck_trees.txt", "newick")
        with open("data/output_nwck.txt", "w") as o:
            result = distance(trees, nodes)
            print(result)
            o.write(result)
