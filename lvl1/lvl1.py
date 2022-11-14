import networkx
from collections import defaultdict, deque


def main():
    N = int(input())
    l = []
    for _ in range(N):
        l.append(input())
        
    s = ''.join(l)
    print(s.count("C"))
    
    
if __name__ == "__main__":
    main()