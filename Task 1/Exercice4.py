inp:str
par:int
par=0
for i in range(1,3,1):
    inp=input()
    match inp:
        case "красный":
            par+=1
        case "синий":
            par+=2
        case "жёлтый":
            par+=4
        case _:
            print("Неверный цвет")
            break

match par:
    case 3:
        print("фиолетовый")
    case 5:
        print("оранжевый")
    case 6:
        print("зелёный")
