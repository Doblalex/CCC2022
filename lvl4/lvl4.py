import networkx
from collections import defaultdict, deque

mvdc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
mvdcinv = {(-1,0): "U", (1,0): "D", (0,-1): "L", (0,1): "R"}


def applyp(pos, command):
    return (pos[0]+mvdc[command][0], pos[1]+mvdc[command][1])

def addv(pos,d):
    return (pos[0]+d[0], pos[1]+d[1])

def indg(g, pos):
    return g[pos[0]][pos[1]]

def dfs(pos, grid, vis, ans):
    q = deque()
    vis.add(pos)
    
    for idir, dir in enumerate(dirs):
        if indg(grid, addv(pos, dir)) == "C" and addv(pos, dir) not in vis:  
            ans.append(mvdcinv[dir])
            dfs(addv(pos,dir), grid, vis, ans)
            ans.append(mvdcinv[dirs[(idir+2)%4]])
            
    
    

def main():
    N = int(input())
    grid = []
    coinspos = set()
    for row in range(N):
        grid.append(input())
        for column in range(len(grid[row])):
            if grid[row][column] == "C":
                coinspos.add((row, column))
            
        

    s = ''.join(grid)

    r, c = list(map(int, input().split()))
    pospacman = (r-1, c-1)
    ans = []
    vis = set()
    
    maxsteps = int(input())
    dfs(pospacman, grid, vis, ans)
    assert(len(ans)<maxsteps)
    print(''.join(ans))
    


if __name__ == "__main__":
    main()
