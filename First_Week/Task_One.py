#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
import math
import os
import random
import re
import sys

def plusMinus(arr):

    negative_integers = 0
    positive_integers = 0
    zero_integers = 0
    for i in range(len(arr)):
        if (int(arr[i])) < 0:
            negative_integers += 1

        if (int(arr[i])) == 0:
            positive_integers += 1

        if (int(arr[i])) > 0:
            zero_integers += 1

    print('%.6f' %(zero_integers / len(arr)))        
    print('%.6f' %(negative_integers / len(arr)))
    print('%.6f' %(positive_integers / len(arr)))


if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))
        plusMinus(arr)
