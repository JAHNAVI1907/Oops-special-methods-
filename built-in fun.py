class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=abc("abcdef",10)
print("the value stored in object is :",repr(obj))
print("the length of name stored in object:",len(obj))
obj1=abc("ghijkl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("both lengths are equal")
elif val==-1:
    print("first values is less than second")
else:
    print("second value is less than first")
