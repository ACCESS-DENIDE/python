from random import randint

def Ex1():
    outp_str:str
    flag:bool
    flag=True
    outp_str=""
    while (flag):
        inp:str
        inp=input()
        if inp=="stop":
            flag=False
        else:
            outp_str+=inp+' '
    print(outp_str)

def Ex2():
    flag:bool
    inp:str
    inp=input()

    for i in inp:
        flag=False
        if i=='ф' or i=='Ф':
            flag=True
            break
    if flag:
        print("Редкое слово")
    else:
        print("Не редкое слово")

def Ex3():
    strike:int=3
    right:int=0
    a:int
    b:int
    ans:int
    while (strike>0):
        a=randint(1,99)
        b = randint(1, 99)
        print(str(a) + "+" + str(b)+"=", end='')
        ans=int(input())
        if ans==a+b:
            print("Right")
            right+=1
        else:
            strike-=1
            if strike!=0:
              print("wrong, strikes left:"+ str(strike))
    print("Game Over, amount of right ans:" +str(right))
