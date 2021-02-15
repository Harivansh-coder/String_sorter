
# String Sorting function
def sorter(a, mode):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if mode == "asc":
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
            else:
                if a[j] < a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]


# String input
print("Enter your string: ", end='')
a = input()
a = a.lower()

# converting string to list for manipulation
a = list(a)

# Ascending or descending condition
while True:
    print("Ascending or descending (A/D): ", end='')
    c = input()
    if c in ['a', 'A']:
        sorter(a, "asc")
        break
    elif c in ['d', 'D']:
        sorter(a, "desc")
        break
    else:
        print("Invalid Input")

# Converting list back to string and printing the sorted
print("".join(a))
