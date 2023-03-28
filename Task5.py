def Ex1():
    list={"USA":"New york","UK":"Great britan","Russia":"Mosscow","China":"Ching-Chong","Australia":"Canberra"}
    for i in list.keys():
        print(i,":", list[i])
    inp=input()
    if list.get(inp, -1)==-1:
        print("This item does not exist")
    else:
        print(list[inp])
    outp=sorted(list.keys())
    for i in outp:
        print( i,": ",list[i])

def Ex2():
    list={1:"", 2:"",3:"",4:"",5:"",8:"",10:""}

Ex1()