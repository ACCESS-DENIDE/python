from tkinter import *
from tkinter import ttk

class IceCream():
    flavour=""
    type_cream=""
    amount:int
    def __init__(self, name_ref, amount, cream_type) -> None:
        self.flavour=name_ref
        self.amount=amount
        self.type_cream=cream_type
        pass
    def _take(am:int):
        amount-=am
    def _add(am:int):
        amount+=am

class Restaurant():
    name=""
    cuisine_type=""
    social_credit:int
    def __init__(self, name_ref, ct, credit) -> None:
        self.name=name_ref
        self.cuisine_type=ct
        self.social_credit=credit
        pass
    def describe_restaurant(self)->None:
        print("Name: "+self.name)
        print("Cuisine_type: "+self.cuisine_type)
        print("Raiting:"+ str(self.social_credit))
    def rate(self, new_rate):
        self.social_credit=new_rate

class IceCreamStand(Restaurant):
    flavors=[]
    geolocation=""
    open_time=""
    def __init__(self, name_ref, credit)->None:
        self.name=name_ref
        self.cuisine_type="IceCream"
        self.social_credit=credit
    def has_flavor(self, src)->bool:
        for i in self.flavors:
            if(i==src):
                return True
        return False
    def add_flavors(self, new_fl)->None:
        self.flavors.append(new_fl)
    def remove_flavors(self, old_fl)->None:
        if(self.has_flavor(old_fl)):
            self.flavors.remove(old_fl)
                
        pass

def Ex1():
    ICS=IceCreamStand("Cream", 5)
    NewCream=IceCream("Milk", 15, "Soft")
    ICS.add_flavors(NewCream)
    print(ICS.flavors)
    ICS.remove_flavors(NewCream)
    print(ICS.flavors)


def Ex2():
    def add_rest():
        Restaurant_list.append(IceCreamStand(Name_holder.get(), 3))
        rest_var = Variable(value=Restaurant_list)
        rest_listbox.insert(len(Restaurant_list), Name_holder.get())
    Restaurant_list:IceCreamStand=[]

    def edit_rest():
        
        root_2 = Tk()
        root_2.title("Restaurant Editor")
        root_2.geometry("300x250")
        mem=int(rest_listbox.curselection()[0])
        cou=0
      
        def add_flavour():
            Restaurant_list[mem].add_flavors(Name_flavour.get())
            flavour_listbox.insert(len(Restaurant_list[mem].flavors), Name_flavour.get())
        def remove_flavour():
             Restaurant_list[mem].remove_flavors(Name_flavour.get())
             flavour_listbox.delete(flavour_listbox.curselection()[0])
        btn = ttk.Button(root_2,text="AddFlavour", command=add_flavour)
        btn.pack()

        btn2 = ttk.Button(root_2,text="RemoveFlavour", command=remove_flavour)
        btn2.pack()

        Name_flavour = ttk.Entry(root_2)
        Name_flavour.pack(anchor=NW, padx=6, pady=6)

        flavour_listbox = Listbox(root_2)
        flavour_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
        
        
        for i in  Restaurant_list[mem].flavors:
             flavour_listbox.insert(cou, i)
             cou+=1
        root_2.mainloop()
        

    root = Tk()
    root.title("Restaurant Manager")
    root.geometry("300x250")
    
    btn = ttk.Button(text="AddNew", command=add_rest)
    btn.pack()

    Name_holder = ttk.Entry()
    Name_holder.pack(anchor=NW, padx=6, pady=6)
    
    rest_listbox = Listbox()
    rest_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
    
    btn2 = ttk.Button(text="Edit", command=edit_rest)
    btn2.pack()

    root.mainloop()
Ex2()