def Ex1():
    list={}
    for i in list.keys():
        print(i, list[i])
    inp=input()
    if list.get(inp, -1)==-1:
        print("This item does not exist")
    else:
        print(list[inp])
    
    