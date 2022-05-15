
class School:
    
    name = "ABC Public"
    
    def __init__(self,count,fee):
        self.__count = count
        self.__fee = fee 
        
    def get_count(self):
        return self.__count
    
    def set_count(self,count):
        self.__count = count 
    
    @classmethod # this is a decorator 
    def school_name(cls):
        print(cls.name)
        
    @staticmethod #static
    def info():
        print("static method")
        

        
s = School(200,20000)
School.school_name()
print(s.get_count())      
School.info() 