#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
import math
import os
import random
import re
import sys

def plusMinus(arr):

    negative_integers = 0   #created for negative an empty paramaters which is equal to 0
    positive_integers = 0   #created for positive an empty paramaters which is equal to 0
    zero_integers = 0   #created an empty paramaters which is equal to 0
    for i in range(len(arr)):   #loop for created where i = 0 and will countinue to the lenegth of our arry
        if (int(arr[i])) < 0:   #if converted integer negative_integers which is less then 0
            negative_integers += 1  #then our negative_integers will be incremented

        if (int(arr[i])) == 0: # if converted integer of our array is 0
            positive_integers += 1  #then our positive_integers will be incremented by one each loop will be countinued

        if (int(arr[i])) > 0: # if converted integer is positive_integers which is greater 0
            zero_integers += 1 # then zero_integers will be incremented by each loop

    print('%.6f' %(zero_integers / len(arr)))        #prints the the incremented zero_integers then devide to len 0f our array
    print('%.6f' %(negative_integers / len(arr)))   #prints the the incremented negative_integers then devide to len 0f our array
    print('%.6f' %(positive_integers / len(arr)))   #prints the the incremented positive_integers then devide to len 0f our array


if __name__ == '__main__':
        n = int(input().strip()) #created input as integer and strips removes any whitespace and etc and it returns a new string with the whitespace removed.

        arr = list(map(int, input().rstrip().split())) #so first we got it will create a list of map functon where applies to integer function to each  substring in the list
                                                        #then we rstrip it will ignore any whitespace from the right of input
                                                        #and then we spilit this This method splits the input string into a list of substrings at each occurrence of a space character.
        plusMinus(arr)
