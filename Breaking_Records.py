import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count, min_count = 0, 0
    Max, Min = scores[0], scores[0]
    for i in scores[1:]:
        if i > Max:
            Max = i
            max_count += 1
        if i < Min:
            Min = i
            min_count += 1
            
    return max_count, min_count



if __name__ == "__main__": 
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(f'{result})))
    print('\n')