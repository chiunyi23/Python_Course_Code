import Baska

#Baska.f(1, 2)
def dig_count(n):
    count = 0
    while n is not 0:
        count = count + 1
        n = n // 10
    return count

#n = int(input())
#print(dig_count(n))


n = int(input())
space = 4
digit = 0

for i in range(n):
    k = (n - i - 1)
    for x in range(2 * k):
        print(' ', end='')
    for j in range(1, i+2):
        c = Baska.f(i+1-1, j-1)
        digit = dig_count(c)
        for r in range(space - digit):
            print(' ', end='')
        print(c, end='')

    
    print()


