class abc():
    c=0
    def __init__(self,var):
        abc.c+=1
        self.var=var
        print("object variable:",var)
        print("class variable:",abc.c)
obj=abc(10)
obj=abc(20)
