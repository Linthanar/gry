def per(l):
    if len(l) == 1:
        return [l]
    return [[l[i]] + p for i in range(len(l))for p in per(l[:i] + l [i+1:])]


print(per(['a','b','c']))

print(per(['a','b']))