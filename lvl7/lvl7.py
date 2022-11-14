import networkx
from collections import defaultdict, deque
from copy import deepcopy
import sys

mvdc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
dirs = [(1,0),(0,-1),(0,1),(-1,0)]
# d l r u
mvdcinv = {(-1,0): "U", (1,0): "D", (0,-1): "L", (0,1): "R"}
mvdcinv2 = {(-1,0): "D", (1,0): "U", (0,-1): "R", (0,1): "L"}


def applyp(pos, command):
    return (pos[0]+mvdc[command][0], pos[1]+mvdc[command][1])

def addv(pos,d):
    return (pos[0]+d[0], pos[1]+d[1])

def indg(g, pos):
    return g[pos[0]][pos[1]]

def bfs(pospacman, emptygrid, posghosts, movements, num, coinvals):
    states = defaultdict(lambda: (-1, []))
    states[pospacman] = (0, [])
    
    for i in range(num):
        newstates = defaultdict(lambda: (-1, []))
        
        for j in range(len(posghosts)):
            posghosts[j] = applyp(posghosts[j], movements[j][i % len(movements[j])])
        ghostset = set(posghosts)
        
        for row in range(len(emptygrid)):
            for col in range(len(emptygrid[0])):
                pos = (row,col)
                if emptygrid[row][col] == "W" or pos in ghostset:
                    newstates[pos] = (-1, [])
                    continue
                
                add = coinvals[pos]
        
                for dir in dirs:
                    oldpos = addv(pos, dir)
                    score, seq = states[oldpos]
                    if score != -1 and score+add > newstates[pos][0]:
                        newscore = score+add
                        newseq = seq + [mvdcinv2[dir]]
                        newstates[pos] = (newscore, newseq)     
        states = newstates
        
    ans = 0
    seq = []
    
    for k,v in states.items():
        if v[0] > ans:
            ans = v[0]
            seq = v[1]
    print(ans)
        
    
def shortestpath(grid, start, end):
    q = deque()
    vis = set()
    q.append((start, []))
    vis.add(start)
    
    ans = list()
    while len(q)>0:
        pos,s = q.popleft()
        if len(ans)>0 and len(s) > len(ans[0]): continue
        if pos == end:
            ans.append(s)
            continue
        for dir in dirs:
            newpos = addv(pos, dir)
            if newpos not in vis and grid[newpos[0]][newpos[1]] not in ["W"]:
                vis.add(newpos)
                q.append((newpos, s+[mvdcinv[dir]]))
    ans.sort()
    return ans[0]
                
    
                
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
        
    posghosts = []
    movements = []
    Nghosts = int(input())
    for _ in range(Nghosts):
        r, c = list(map(int, input().split()))
        r-=1
        c-=1
        posghosts.append((r,c))
        movement = shortestpath(emptygrid, (r,c), pospacman)
        movement = movement + invseq(movement)
        movements.append(movement)
    
    coincnt = int(input())
    coinvals = defaultdict(lambda: 0)
    for _ in range(coincnt):
        r,c,v = list(map(int,input().split()))
        coinvals[(r-1,c-1)] = v
        
    num = int(input())
    bfs(pospacman, grid, posghosts, movements, num, coinvals)    


if __name__ == "__main__":
    main()
