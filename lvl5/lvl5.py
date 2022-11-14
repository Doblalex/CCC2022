import networkx
from collections import defaultdict, deque
from copy import deepcopy

mvdc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
mvdcinv = {(-1,0): "U", (1,0): "D", (0,-1): "L", (0,1): "R"}


def applyp(pos, command):
    return (pos[0]+mvdc[command][0], pos[1]+mvdc[command][1])

def addv(pos,d):
    return (pos[0]+d[0], pos[1]+d[1])

def indg(g, pos):
    return g[pos[0]][pos[1]]

def bfs(pospacman, grids, MOD):
    q = deque()
    q.append((0, pospacman, []))
    vis = set()
    vis.add((0, pospacman))
    
    while len(q) > 0:
        i, pos, seq = q.popleft()
        
        if indg(grids[i], pos) == "C":
            print(''.join(seq))
            exit(0)
            
        for dir in dirs:
            posnew = addv(pos, dir)
            if grids[(i+1)%MOD][posnew[0]][posnew[1]] not in ["G", "W"] and ((i+1) % MOD, posnew) not in vis:
                vis.add(((i+1) % MOD, posnew))
                q.append(((i+1) % MOD, posnew, seq+[mvdcinv[dir]])) 
                
def invseq(seq):
    s = []
    for c in seq:
        if c == "U":
            s.append("D")
        elif c == "D":
            s.append("U")
        elif c == "L":
            s.append("R")
        else:
            s.append("L")
    return list(reversed(s))
    
    

def main():
    N = int(input())
    grid = []
    emptygrid = []
    coinspos = set()
    for row in range(N):
        grid.append(list(input()))
        emptygrid.append([])
        for c in grid[-1]:
            if c == "W":
                emptygrid[-1].append("W")
            elif c == "C":
                emptygrid[-1].append("C")
            else:
                emptygrid[-1].append("E")

    r, c = list(map(int, input().split()))
    grid[r][c] = "E"
    pospacman = (r-1, c-1)
    ans = []
    vis = set()
    grids = []
    grids.append(grid)
    
    posghosts = []
    stepsghosts = []
    Nghosts = int(input())
    for _ in range(Nghosts):
        r, c = list(map(int, input().split()))
        Ns  = int(input())
        stepsghost = list(input().strip())
        stepsghost = stepsghost+invseq(stepsghost)
        posghosts.append((r-1,c-1))
        stepsghosts.append(stepsghost)
        
    MOD = len(stepsghosts[0])
    for i in range(MOD):
        for j in range(Nghosts):
            posghosts[j] = applyp(posghosts[j], stepsghosts[j][i])
        gridnow = deepcopy(emptygrid)
        for pos in posghosts:
            gridnow[pos[0]][pos[1]] = "G"
        grids.append(gridnow)
    
    maxsteps = int(input())
    bfs(pospacman, grids, MOD)
    


if __name__ == "__main__":
    main()
