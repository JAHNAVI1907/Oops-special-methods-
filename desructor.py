class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("object variable:",var)
        print("class variable:",abc.cv)
    def __del__(self):
        print("object with %d is going out of scope "%self.var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)
del obj1
del obj2
del obj3
