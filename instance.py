class number:
    even=0
    def check(self,num):
        if num%2==0:
            number.even=1 #or self.even=1
    def eo(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.eo(2)
