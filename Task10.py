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

def Ex1():
    rest=Restaurant("Guestau", "france", 4)
    print(rest.name)
    print(rest.cuisine_type)
    print(rest.social_credit)
    rest.describe_restaurant()
    
def Ex2():
    rest1=Restaurant("Rest1", "Asian", 2)
    rest2=Restaurant("Rest2", "Gogria", 4)
    rest3=Restaurant("Rest3", "Bar", 5)
    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest3.describe_restaurant()

def Ex3():
    rest=Restaurant("Shavermac24", "Yes.", 2)
    rest.describe_restaurant()
    rest.rate(1)
    rest.describe_restaurant()
Ex3()