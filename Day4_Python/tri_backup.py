
n = int(input())

for i in range(n):
    k = (n - i - 1)
    for x in range(k):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print()