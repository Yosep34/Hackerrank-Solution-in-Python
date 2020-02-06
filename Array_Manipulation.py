import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1) #create an empty array of N 
    for a, b, k in queries:
        arr[a-1] += k 
        arr[b] -= k
    '''you can just use itertools.accumulate function to return
maximum of arr example:(max(accumulate(arr)))'''
    result = acc = 0
    for x in arr:
        acc += x
        result = max(result, acc)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
