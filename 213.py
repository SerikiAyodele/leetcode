# import random

# def shuffleArray(arr):
#     shuffle_arr = random.sample(arr, len(arr))
#     for i in range(len(arr)):
#         arr[i] = shuffle_arr[i]

# arr = [3,7,5,4,9,2,1,5,6,7]
# print("original arr:", arr)
# shuffleArray(arr)
# print("new array:", arr)

# ----------------------------------------------------

# class bits:
#     def __init__(self, size):
#         self.bit_array = [0] * size

#     def flipBits(self, start, length):
#         for i in range(start, start+length):
#             self.bit_array[i]

#     def getBits(self, index):

# ----------------------------------------------------
def findIndices(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                if arr[i] < arr[j] < arr[k]:
                    return i,j,k
                
arr = [3,7,5,4,9,2,1,5,6,7]
output = findIndices(arr)
print(output)


for i in arr:
    l=0 r=1
    if r 
