num:int
num=int(input())
if num>54:
    print("Место не существует")
else:
    ## По информации, которую я нашёл распределение идёт по чётности\нечётности для положения полки и по номеру (до 37 идут купе, далее плацкарт)
    if num>36:
        print("Плацкарт")
    else:
        print("Купе")

    if num%2==0:
        print("Верхнее место")
    else:
        print("Нижнее место")