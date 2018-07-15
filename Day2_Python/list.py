s = [100, 200, 300, 400, 500]

# s[i:j]  從 i 開始，遇到 j 停止(不會到 j)
print(s[0:])
print(s[0:2])
del s[1:2]

print(s[0:])

# max, min, len
print(max(s))
print(min(s))
print(len(s))


# 'in' and 'not in'
print(10 in s)
print(100 in s)
print(10 not in s)
