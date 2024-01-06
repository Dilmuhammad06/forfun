def sort(n):
    lenn = range(1, len(n))

    for i in lenn:
        value = n[i]

        while n[i - 1] > value and i > 0:
            n[i], n[i - 1] = n[i - 1], n[i]
            i = i - 1
    return n


print(sort([6, 5, 7, 4, 3, 5, 2, 1, 99]))

# Better than last try
