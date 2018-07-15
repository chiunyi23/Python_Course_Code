# Key 與 Value 可以為任意型態

age = {
    'Alice' : 20,
    'Mike'  : 23,
    'Amy'   : 33
}

# 新增
print("add")
print(age)
age['Allen'] = 55
print(age)

# 更改
print("change value")
print(age)
age['Alice'] = 11
print(age)

# 複製字典
copy_age = age.copy
print(copy_age)