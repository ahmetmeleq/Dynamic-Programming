def longestCommonSubsequence(i, j):
    global a,b,n,m
    
    if i>=n or j>=m:
        return 0
    
    if (i,j) in memory:
        return memory[i,j]
    
    if a[i] == b[j]:
        memory[i,j] = 1 + longestCommonSubsequence(i+1,j+1)
        backtrack[i,j] = 1,1
        return memory[i,j]
    
    left = longestCommonSubsequence(i+1,j)
    right = longestCommonSubsequence(i, j+1)
    
    if left>=right:
        chosen = left
        backtrack[i,j] = 1,0
    elif right>left:
        chosen = right
        backtrack[i,j] = 0,1
    
    memory[i,j] = chosen
    return memory[i,j]
    
    
def printer():
    i = 0
    j = 0
    while(1):
        if i+1>n or j+1>m:
            break
            
        if a[i] == b[j]:
            print(a[i], end = ' ')
            
        if (i,j) in backtrack:
            myop = backtrack[i,j]
            i = i + int(myop[0])
            j = j + int(myop[1])
        else:
            break
    

n, m = map(int, input().split())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

memory = {}
backtrack = {}
length = longestCommonSubsequence(0, 0)
printer()


