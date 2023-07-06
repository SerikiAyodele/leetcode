# remove elements present in L1 which are also present in L2

def comparison(l1, l2):
    result = []

    for i in l1:
        if i not in l2:
            result.append(i)
        else:
            pass
    return result


l1 = [3,4.8,5,3,1,6,8,0]
l2 = [4,6,9,1,3,0,4,2,7,4]

unique_elements = comparison(l1, l2)
print(unique_elements)

        
# RESULT
# ayodeleseriki@MacBook-Pro-2 Leetcode % python3 elements_in_l1_also_in_l2.py
# [4.8, 5, 8]