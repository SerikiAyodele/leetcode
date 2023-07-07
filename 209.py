#Write a function to return the most frequently occurring number in a list

def mostOccouring(num):
    dict = {}
    max = 0
    count = 0

    for i in num:
        dict[i] = dict.get(0, i) + 1
        if max<dict[i]:
            max = dict[i]
            count = i
        return i

num = [4,6,9,1,3,0,4,2,7,4]
highestNumber = mostOccouring(num)
print(highestNumber)
