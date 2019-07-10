from collections import Counter

def solve(num):
    list = []
    n = 1
    for i in range(num):
        list.append(n)
        n = n * -1

    c = Counter(list)
    c.most_common()
    mode = c.most_common(2)

    if mode[0][1] != mode[1][1]:
        return 0
    else:
        return 1

print solve(5)
print solve(10)

# If the argument is 1 or less, a bug will occur but this time it will be ignored.

