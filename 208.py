# Remove chars at first string from second string.

def removeChar(str1: list[str],str2: list[str]) -> list[str]:
    result = []

    for char in str1:
        if char in str2:
            str2.remove(char)
        else:
            result.append(char)
    return result
        

str1 = ["d","f","h","a","w","e","c","g","x","s"]
str2 = ["w","f","g","s","h","d","g","s","g","v"]

ans = removeChar(str1,str2)
print(ans)