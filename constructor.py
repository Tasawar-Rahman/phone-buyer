class mobile:
    brand=""
    model=""
    price=""
    def __init__(self,b,m,p):
        self.brand=b
        self.model=m
        self.price=p
    def __del__(self):
        print(f"The {self.brand} {self.model} {self.price} has been bought")      
    def show_details(self):
        print(f" Brand : {self.brand} | Model : {self.model} | Price : {self.price}")
    def discount(self,percent):
        n_price=self.price-(self.price*percent/100)
        print(f"After {percent}, discounted price will be {n_price}")
Mob1 = mobile("Samsung","Galaxy S25 Ultra",199999)
Mob2 = mobile("Iphone","17 pro max",201000)
phone=[Mob1,Mob2]
print("\n Available Phones in the Shop :")
for i in phone:
    i.show_details()
target=input("Enter the Phone Model You want discount for: ")
percent=float(input("Enter the discount percentage :"))
found = False
for i in phone:
    if i.model.lower() == target.lower():
        i.discount(percent)
        want= input("want to buy it now: yes || no?")
        if (want=="yes"):
            del i
        found=True

if not found:
    print("No phone found with this name")




#def __del__(self):
       #print(f"Obj has been deleted!")
    #def showValue(self):
        #print(f"Roll: {self.roll}, GPA: {self.gpa}")