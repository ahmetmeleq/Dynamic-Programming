import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)
def unboundedKnapsack(k, arr):
    if k in memory:
        return memory[k]
    
    chosen_sum = 0
    for item in arr:
        candidate_sum = 0
        if item <= k:
            candidate_sum = unboundedKnapsack(k-item, arr) + item
        else:
            continue
        
        if candidate_sum > chosen_sum:
            chosen_sum = candidate_sum
    
    memory[k] = chosen_sum
    return chosen_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for i in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))
        
        memory = {}
        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
