'''
Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A ∪ B, A ∩ B, A − B, B − A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
'''
def six_sets(n, A, B):
    U = {i for i in range(1, n + 1)}
    set_list = [0 for i in range(6)]
    set_list[0] = A | B
    set_list[1] = A & B
    set_list[2] = A - B
    set_list[3] = B - A
    set_list[4] = U - A
    set_list[5] = U - B
    
    lst = ""
    for s in set_list:
        lst += str(s) + "\n"

    return lst

if __name__ == "__main__":
    with open("data/rosalind_seto.txt", "r") as f:
        lines = f.readlines()
        n = int(lines[0].rstrip())
        A = list(map(int, lines[1][1:-2].rstrip().split(", ")))
        B = list(map(int, lines[2][1:-2].rstrip().split(", ")))
        with open("data/output_seto.txt", "w") as o:
            o.write(six_sets(n, set(A), set(B)))
            print(six_sets(n, set(A), set(B)))
