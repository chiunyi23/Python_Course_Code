def f(k, n):
    diff = k - n
    if diff is 0:
        return 1
    up = 1
    down = 1
    for i in range(diff):
        up *= k
        k = k - 1
        down *= (i + 1)
    c = up // down
    return c
'''
n = int(input())
m = int(input())
print(f(n, m))
'''

#for i in range(1, n):


'''
for i in range(2, n+1):
    for j in range(i):
        list = [i, i+1]
        num[i] = list
for i in range(1, n+1):
    print(num[i])
'''