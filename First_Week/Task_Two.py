import math
import os
import random
import re
import sys


def plusMinus(arr):
    sorted_set = sorted(arr)
    subset = sorted_set[:4]
    subset_max = sorted_set[1:]
    sum_of_max = sum(subset_max)
    sum_of_min = sum(subset)
    print(sum_of_min, sum_of_max)

if __name__ == '__main__':

        arr = list(map(int, input().rstrip().split()))
        plusMinus(arr)
