def Ex1(): 
  print(Div3(6))


def Ex2():
    print(div100(10))

def Ex3():
    print(LuckCh("02.11.2021"))

def Ex4():
    print(TicCheck("3856"))

def Div3(inp:int)->bool:
    return inp % 3==0


def div100(delimetr)->str:
    delimetr=str(delimetr)
    if delimetr=="0":
        return "Err: Zero Div"
    if not(delimetr.isnumeric()):
        return "Err: string input"
    delimetr=int(delimetr)
    return 100/delimetr

def LuckCh(inp:str)->bool:
    inp=inp.split(".")    
    return (int(inp[0]))*(int(inp[1]))==((int(inp[2]))%100)

def TicCheck(inp:str)->bool:
    
    checkSum:int=0
    for i in range(0, int(len(inp)/2)):
        checkSum+=int(inp[i])
        checkSum-=int(inp[int(len(inp)/2+i)])
    if checkSum==0:
        return True
    else:
        return False

Ex4()