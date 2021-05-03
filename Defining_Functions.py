# See https://www.tutorialspoint.com/python3/python_functions.htm


def Replace_Character_At_Index(str1, chr1, idx):
    str2 = str1[0:idx]
    str3 = str1[idx + 1 :]
    print(str2)
    print(str3)
    str1 = str2 + chr1 + str3
    return str1


print("\n\n")

str1 = "abc"
str1 = Replace_Character_At_Index(str1, "S", 1)
print(str1)

print("\n\n")
