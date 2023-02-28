year:int
year=int(input())
if year %4==0:
    if year%100==0 and year%400!=0:
        print("Этот год не високосный")
    else:
        print("Год "+ str(year)+" високосный")
else:
    print("Этот год не високосный")