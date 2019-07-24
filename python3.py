def sortStringArray(s, a, n):

    a = sorted(a, key = lambda word: [s.index(c) for c in word])
    for i in a:
        print(i, end =' ')

s = "rcta"
a = ["car", "rat", "cat"]
n = len(a)
sortStringArray(s, a, n)
