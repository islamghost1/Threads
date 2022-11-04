class a:     
    def __init__(self,data):
        self.left = 2
        print("self : {},data : {}".format(self.left , data))
    def func(self,data):
        print("self.left : {},data from func  : {}".format(self.left , data))

    
s = a(10)
s.func(20)
