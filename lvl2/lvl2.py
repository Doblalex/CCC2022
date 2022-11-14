import networkx
from collections import defaultdict, deque


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input())
        
    s = ''.join(grid)
    cointcnt = s.count("C")
    
    r,c = list(map(int,input().split()))
    r-=1
    c-=1
    Ns = int(input())
    
    steps = input()
    ans = set()
    for chr in steps:
        if chr=="D":
            r+=1
        elif chr == "U":
            r-=1
        elif chr == "L":
            c-=1
        else:
            c+= 1
            
        if grid[r][c] == 'C':
            ans.add((r,c))
    print(len(ans))
        
    
    
if __name__ == "__main__":
    main()