
def binary_search(lst, l, k):
    i = 0
    j = l-1
    while i <= j:
        m = int((i+ j)/2)
        if k == lst[m]:
            print("\nEntered number %d is present at position: %d" % (k, m+1))
            return
        elif k < lst[m]:
            j = m - 1
        elif k > lst[m]:
            i = m+ 1
    print("\nElement not found!")
    return -1

list = []

size = int(input("Enter size of list: \t"))

for e in range(size):
    elements = int(input("Enter any number: \t"))
    list.append(elements)

list.sort()
print('\n\nThe list will be sorted, the sorted list is:', list)

x = int(input("\nEnter the number to search: "))

binary_sort(list, size, x)

