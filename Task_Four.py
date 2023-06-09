import math
import os
import random
import re
import sys

def count_matching_string(strings, target):
    count = []
    for i in target:
        if i in strings:
            count.append(strings.count(i))
        else:
            count.append(0)

    return count

s = int(input())
my_string = []
for i in range(s):
    string_item = input()
    my_string.append(string_item)


q = int(input())
queries = []
for i in range(q):
    queries_item = input()
    queries.append(queries_item)



matching_count = count_matching_string(my_string, queries)
print(matching_count)
