import networkx
from collections import defaultdict, deque
from copy import deepcopy
import sys

mvdc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
dirs = [(1,0),(0,-1),(0,1),(-1,0)]
# d l r u
mvdcinv = {(-1,0): "U", (1,0): "D", (0,-1): "L", (0,1): "R"}


def applyp(pos, command):
    return (pos[0]+mvdc[command][0], pos[1]+mvdc[command][1])

def addv(pos,d):
    return (pos[0]+d[0], pos[1]+d[1])

def indg(g, pos):
    return g[pos[0]][pos[1]]

def bfs(pospacman, grids, target, MOD):
    q = deque()
    q.append((0, pospacman, frozenset(), []))
    vis = set()
    vis.add((0, pospacman, frozenset()))
    
    ans = set()
    anslen = sys.maxsize
    while len(q) > 0:
        i, pos, coinshave, seq = q.popleft()
        if len(seq) > anslen: continue
        if coinshave == target:
            anss = ''.join(seq)
            anslen = len(anss)
            ans.add(anss)
            continue    
        
        for dir in dirs:
            posnew = addv(pos, dir)
            coinshavenew = set(coinshave)
            if grids[(i+1) % MOD][posnew[0]][posnew[1]] == "C":
                coinshavenew.add(posnew)
            coinshavenew = frozenset(coinshavenew)
            if grids[(i+1)%MOD][posnew[0]][posnew[1]] not in ["G", "W"] and ((i+1) % MOD, posnew, coinshavenew) not in vis:
                vis.add(((i+1) % MOD, posnew, coinshavenew))
                q.append(((i+1) % MOD, posnew, coinshavenew, seq+[mvdcinv[dir]]))     
                
    ans = list(sorted(ans))
    print(ans[0])
                
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
        for column in range(len(grid[row])):
            if grid[row][column] == "C":
                coinspos.add((row, column))
        emptygrid.append([])
        for c in grid[-1]:
            if c == "W":
                emptygrid[-1].append("W")
            elif c == "C":
                emptygrid[-1].append("C")
            else:
                emptygrid[-1].append("E")

    r, c = list(map(int, input().split()))
    grid[r-1][c-1] = "E"
    pospacman = (r-1, c-1)
    target = frozenset(coinspos)
    
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
    
    bfs(pospacman, grids, target, MOD)
    


if __name__ == "__main__":
    main()
