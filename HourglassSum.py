import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr = max([sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for i in range(1,5) for j in range (1,5)])
    return arr

#Explanation
"""i use list comprehension because it takes less memory and readable
    The first loop take sum from 1 row and 3 columns
    The second loop take sum from 1 row and 1 columns 
    The third loop take sum from 1 row and 3 columns from index i+1
    the first index in for loop parameter is 1 because it's shape must be hourglass
    and the last use max function to give the maximum hourglass sum
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    
    fptr.write(str(result) + '\n')

    fptr.close()
