class A:
    def __init__(self):
        print("init of A")
    def feature1(self):
        print("feature1")
        
    def feature2(self):
        print("feature2")
        
class B(A):
    def __init__(self):
        super().__init__()    #invoking init method of superclass, that means getting the attributes of superclass
        print("init of B")
    def feature3(self):
        print("feature3")
        
    def feature4(self):
        print("feature4")
        
class C(B):
    def feature5(self):
        print("feature5")
        
a = A()
a.feature1()
a.feature2()

b = B()  # if you don't have construcor in B, it will call A's constructor. 
# Incase B has its own constructor, it won't call A's constructor.
b.feature3()
b.feature4()
b.feature1()
b.feature2()

# single level inheritance
#muli level inheritance
#multiple inheritance

#method resolution order (order in sequence from left to right)
