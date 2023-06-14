
def countingSort(n,arr):
      counts = {}
      result = []
      for element in arr:
          if element >= 0 and element < n:
              if element in counts:
                  counts[element] += 1
              else:
                  counts[element] = 1
      for i in range(0, 100):
          if i in counts:
              result.append(counts[i])
          else:
              result.append(0)


      return result

#a lot of test have been run and asked to chatgpt to fix as my range was n + 1 I coundnt fix and it has to be from range(n) instead of range(n+1)
#After submission I got 2 correct out of 6 where range again was inccorect
#range has to be between 0 to 100 corrected for i in range(0, 100): ...
n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = countingSort(n,arr)
print(' '.join(map(str,result)))


#63 25 73 1 98 73 56 84 86 57 16 83 8 25
#81 56 9 53 98 67 99 12 83 89 80 91 39 86 76
#85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46
#96 27 32 18 21 92 69 81 40 40 34 68 78 24 87
#42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3
#70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33
