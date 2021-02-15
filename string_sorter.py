# List to string converter function
def convert(a):
    b = ""
    for i in a:
        b+=i
    
    return b

# String Sorting function
def sorter(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    




#String input
print("Enter your string: ",end='')
a = input()
a=a.lower()
b = list(a)






sorter(b)



print(b)

# Ascending or descending condition
print("Ascending or descending (A/D): ",end='')
c = input()


e =""

# Ascending and descending implementation
while len(e) == 0: 
    if (c == 'A' or c == 'a'):
        b=convert(b)
        print(b)
        e+='A'

    elif (c == 'D' or c == 'd'):

        d = []
        i = len(b)-1
        while i >= 0:
            d.append(b[i])
            i-=1
        d=convert(d)
        print(d)
        e+='D'

    else:
        print("invalid input")

