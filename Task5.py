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
    list={1:"aeioulnstr", 2:"dg",3:"bcmp",4:"fhvwy",5:"k",8:"jx",10:"qz"}
    inp=input()
    inp=inp.casefold()
    sum=0
    for i in inp:
     for g in list.keys():
         if(list[g].find(i)!=-1):
            sum+=g
    print(sum)

def Ex3():
    stud={"Stud1":"russian,english,french", "Stud2":"chineese,russian,french", "Stud3":""}
    

Ex2()