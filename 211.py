# Given an array of integers find indices I < j < k such that a[I] < a[j] < a[k]

def findIndices(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] < arr[j] < arr[k]:
                    return i,j,k
                
arr = [4.8,5,1,6,8,0,4,6,7,8,5,5,6]
output = findIndices(arr)
print(output)