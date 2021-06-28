"""
Following function sorts the characters of the string.
It takes two parameters, first the string itself and second 1 or 0 (ascending or descending).   
It has a worst case time complexity of O(n**2)
"""

# String Sorting function
def sortString(string_val, order):
    string_val=list(string_val.lower())
    result = ""

    # for string to be sorted in ascending order
    if order == 1:
        for i in range(1,len(string_val)):
            temp = string_val[i]
            j = i - 1
            while j >= 0 and string_val[j] > temp:
                string_val[j+1] = string_val[j]
                j -= 1
            string_val[j+1] = temp

    # for string to be sorted in descending order
    elif order == 0:
        for i in range(1,len(string_val)):
            temp = string_val[i]
            j = i - 1
            while j >= 0 and string_val[j] < temp:
                string_val[j+1] = string_val[j]
                j -= 1
            string_val[j+1] = temp

    for i in string_val:
        result += i
    
    return result

    
#String input
a = input("Enter the string: ")

#function call
print(sortString(a,1))

"""
#OUTPUT
Enter the string: ncjndjncdnnv
ccddjjnnnnnv

Enter the string: dcbaabca
aaabbccd

"""


