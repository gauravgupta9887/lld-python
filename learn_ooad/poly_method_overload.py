class Student:
    def __init__(self,m1=None,m2=None):
        self.m1 = m1
        self.m2 = m2 
        
    def __add__(self,other):
        return Student(self.m1+other.m1,self.m2+other.m2)
    
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
        
# no method overload in python ==> use none that means if not there is no issue
    
s1 = Student(65,54)
s2 = Student(33,65)

s3 = s1 + s2
print(s3.m1,s3.m2)

print(s1)
print(s1.__str__())