def fuc(h, hour, rank):
    if rank > 90:
        money = 8000 + (hour * 200)
    elif rank >= 70 and rank <= 90:
        
        money = 6000 + (hour * 200)
    else:
        money = 4000 + (hour * 200)        
    print(h, " rank : ", rank, ", hour : ", hour, ", salary ", money)

hour = 14
rank = 55
fuc('A', hour, rank)

hour = 13
rank = 96
fuc('B', hour, rank)

hour = 22
rank = 85
fuc('C', hour, rank)