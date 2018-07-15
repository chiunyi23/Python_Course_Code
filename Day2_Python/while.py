'''
a = 1
while a < 100:
    print(a, end=' ')
    a += 2
print ('end')
'''
def f(n):
    i = 1
    j = 1
    while i <= n:
        while j <= n:
            print(i, '*', j, '=', i* j, sep='', end='\t')
            j += 1
        print("")
        j = 1
        i += 1

n = int(input())

f(n)