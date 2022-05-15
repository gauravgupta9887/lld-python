class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno 
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
    
    # this is inner class 
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.processor = 'I5'
            self.ram = 8
        
        def show(self):
            print(self.brand , self.processor, self.ram)
            
            
s = Student('Gaurav',4)
s.show()
lappi = s.lap
lappi.show()