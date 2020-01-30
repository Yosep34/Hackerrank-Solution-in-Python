import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if (sum(s[i:m+i]) == d):
            count+=1
    return count

n = int(input())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
result = birthday(s, d, m)
print(result)
