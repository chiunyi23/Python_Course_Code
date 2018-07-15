hour = 20
rank = 91
if rank > 90:
    money = 8000 + (hour * 200)
elif rank >= 70 and rank <= 90:
    money = 6000 + (hour * 200)
else:
    money = 4000 + (hour * 200)
print("A rank : ", rank, ", hour : ", hour, ", salary ", money)

hour = 15
rank = 75
if rank > 90:
    money = 8000 + (hour * 200)
elif rank >= 70 and rank <= 90:
    money = 6000 + (hour * 200)
else:
    money = 4000 + (hour * 200)
print("B rank : ", rank, ", hour : ", hour, ", salary ", money)

hour = 25
rank = 60
if rank > 90:
    money = 8000 + (hour * 200)
elif rank >= 70 and rank <= 90:
    money = 6000 + (hour * 200)
else:
    money = 4000 + (hour * 200)
print("C rank : ", rank, ", hour : ", hour, ", salary ", money)