from random import randint

def Ex1():
    list=[]
    for i in range(0, 5):
        list.append(randint(1,99))
    
    inp=int(input())
    flag:bool=False
    for i in range(0, 5):
        print(list[i], end=" ")
        if list[i]==inp:
            flag=True
    print("User numb:", inp)
    if flag:
        print("Congratulation, this number stored in list")
    else:
        print("This numb does not exist")
    
    
def Ex2():
    list=[]
    for i in range(0, 5):
        list.append(randint(1,99))
    cou={}
    for i in range(0, 5):
        if cou.get(list[i], -1)==-1:
            cou[list[i]]=0
        cou[list[i]]+=1
    
    for i in cou.keys():
        print(i,": ", cou[i])
   

def Ex3():
    days=("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    print("Amount of day offs:", end="")
    numb=int(input())
    print("Day off: ", end=" ")
    for i in range(7-numb, 7):
        print(days[i], end=" ")
    print()
    print("Working days: ", end=" ")
    for i in range(0 ,7-numb):
        print(days[i], end=" ")
    print()


def Ex4():
    list1=["List1Name1", "List1Name2", "List1Name3", "List1Name4"]
    list2=["List2Name1", "List2Name2", "List2Name3", "List2Name4"]
    Team=(list1[0], list1[1],list2[2],list2[3])
    print("Group1:", *list1, sep=" ")
    print("Group2:", *list2,sep=" ")
    print("Team List:", *Team,sep=", ")
    print("TeamSize", len(Team))
    print("Am of Ivanov", Team.count("Ivanov"))    
    
    
            
    
Ex3()