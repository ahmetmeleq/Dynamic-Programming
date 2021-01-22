import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    mysum = 0
    for i,cal in enumerate(calorie):
        mysum += 2**i * cal
    return mysum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
