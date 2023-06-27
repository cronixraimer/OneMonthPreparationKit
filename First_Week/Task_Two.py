import math
import os
import random
import re
import sys


def plusMinus(arr):     #a class called plusMinus where substring arr
    sorted_set = sorted(arr) #sorting our array
    subset = sorted_set[:4] #elements from 0 to 4 but 4 will not including
    subset_max = sorted_set[1:] #elements from 1 to the end
    sum_of_max = sum(subset_max) # sum of our substted max
    sum_of_min = sum(subset) # min sum of subset elements
    print(sum_of_min, sum_of_max) # printing our sum of min and max elements 

if __name__ == '__main__':

        arr = list(map(int, input().rstrip().split()))  #so first we got it will create a list of map functon where applies to integer function to each  substring in the list
                                                        #then we rstrip it will ignore any whitespace from the right of input
                                                        #and then we spilit this This method splits the input string into a list of substrings at each occurrence of a space character.
        plusMinus(arr)
