class number():
    el=[]
    ol=[]
    def __init__(self,num):
        if num%2==0:
            self.el.append(num)
        else:
            self.ol.append(num)
obj=number(21)
obj=number(32)
obj=number(43)
obj=number(54)
obj=number(65)
print(number.el)#print(obj.el)
print(obj.ol)
