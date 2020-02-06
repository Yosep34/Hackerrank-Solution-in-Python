import math
import os
import random
import re
import sys

def leftRotation(a,d):
    a = [a[(i+d) % len(a)] for i, x in enumerate(a)]
    return a



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    result = leftRotation(a,d)

    print(*result)

    
