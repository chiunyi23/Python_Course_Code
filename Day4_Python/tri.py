import Baska

#Baska.f(1, 2)


n = int(input())

for i in range(n):
    k = (n - i - 1)
    for x in range(k):
        print(' ', end='')
    for j in range(1, i+2):
        print(Baska.f(i+1-1, j-1), end=' ')
    print()


