import networkx
from collections import defaultdict, deque

mvdc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def applyp(pos, command):
    return (pos[0]+mvdc[command][0], pos[1]+mvdc[command][1])


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input())

    s = ''.join(grid)

    r, c = list(map(int, input().split()))
    pospacman = (r-1, c-1)
    Ns = int(input())
    stepspacman = input()
    
    posghosts = []
    stepsghosts = []
    Nghosts = int(input())
    for _ in range(Nghosts):
        r, c = list(map(int, input().split()))
        Ns  = int(input())
        stepsghost = input()
        posghosts.append((r-1,c-1))
        stepsghosts.append(stepsghost)
    
    coins = set()
    for i in range(Ns):
        pospacman = applyp(pospacman, stepspacman[i])
        
        for j in range(Nghosts):
            posghosts[j] = applyp(posghosts[j], stepsghosts[j][i])
            if posghosts[j] == pospacman:
                print(len(coins), "NO")
                exit(0)
        if grid[pospacman[0]][pospacman[1]] == "W":
            print(len(coins), "NO")
            exit(0)
        if grid[pospacman[0]][pospacman[1]] == "C":
            coins.add(pospacman)
            
            
        
        
    print(len(coins), "YES")


if __name__ == "__main__":
    main()
