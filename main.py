
import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        a=q[0]
        b=q[1]
        k=q[2]
        arr[a-1]+=k
        if b<len(arr):
            arr[b]-=k
    max=sum=0
    for i in arr:
        sum+=i
        if sum>max:
            max=sum
    return max              
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
