# tuple 用小括號
# 小括號也是先算的意思，若沒加逗號會被當成 其他型別
t = (1)
print(type(t))
t = (1,)
print(type(t))

# 不能更動到裡面的值
a = (1, 2, 3)
# a[1] = 3

# 但可以重新賦值
a = (7,8)
print(a[0:])