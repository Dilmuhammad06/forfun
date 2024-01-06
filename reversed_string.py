def reverser(n):
    length = range(1, len(n))
    cycles = []
    word_l = []
    rev = []
    for i in length:
        cycles.append(i)
    for j in n:
        word_l.append(j)
    for i in cycles[::-1]:
        rev.append(n[i])
    rev.append(n[0])

    result = ''.join(rev)
    return result


print(reverser('desrever ma I'))

# Used none of chatbots
