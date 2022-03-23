
from decimal import ROUND_CEILING
from math import ceil, floor, trunc


# arr = [0, 7, 11, 35, 67, 98, 117, 143, 165, 199, 200]
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
val = 25
search = False
len = len(arr)
beg = 0
end = len-1

while beg<=end:
    mid = floor((beg+end)/2)
    if val == arr[mid]:
        search = True
    elif val < arr[mid]:
        end = mid-1
    elif val > arr[mid]:
        beg = mid+1
print(search)
