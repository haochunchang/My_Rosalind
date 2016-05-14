'''
Given: A positive integer n (n≤1000) and an adjacency list corresponding to 
a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

def min_tree(n, adj_list):
    # list of sets of nodes connected with each other
    # initialize with nodes totally disconnected
    connected_nodes = [{i} for i in range(1, n + 1)]

   
    for edge in adj_list:
        
        temp_nodes = set()
        del_nodes = []
        
        for nodes in connected_nodes:                

            # if both nodes are already connected, proceed next.
            if (edge[0] in nodes) and (edge[1] in nodes):
                break

            # if only one of the edges are in the nodes, save the nodes.
            elif (edge[0] in nodes) or (edge[1] in nodes):
                temp_nodes.update(nodes)
                del_nodes.append(nodes)

            if len(del_nodes) == 2:
                break
        
        # check if update is necessary.
        if len(del_nodes) != 0:
            temp_nodes.add(edge[0])
            temp_nodes.add(edge[1])
            for node in del_nodes:
                connected_nodes.remove(node)

        # add a brand new set of nodes which contains all of the edges.
        connected_nodes.append(temp_nodes)

    return len(connected_nodes) - 1
    
    
if __name__ == "__main__":
    with open("data/rosalind_tree.txt", "r") as f:
        data = f.read().strip().split("\n")
        n = int(data.pop(0))
        adj_list = [list(map(int, i.split(" "))) for i in data if i != ""]
        print(min_tree(n, adj_list))
