import math
import os
import random
import re
import sys

# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

def dynamicArray(n, queries):
    LastAns = 0
    seqList = [[] for i in range(n)]
    answer = []
    for i in range(len(queries)):
        Q_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        seq = (x^LastAns) % n 
        if Q_type == 1:
            seqList[seq].append(y)
        else:
            LastAns = seqList[seq][y % len(seqList[seq])]
            answer.append(LastAns)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
