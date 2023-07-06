import random

def shuffle_array(arr):
    shuffle_arr = random.sample(arr, len(arr))
    for i in range(len(arr)):
        arr[i] = shuffle_arr[i]

arr = [3,5,6,3,2,9]
print ("original arr:", arr)

shuffle_array(arr)
print ("new arr:", arr)