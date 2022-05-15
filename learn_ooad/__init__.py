class Computer:
    def __init__(self,processor,ram):
        self.__processor = processor 
        self.__ram = ram
    def config(self):
        print(self.__processor,self.__ram)
    def compare(self,other):
        print(self.__processor==other.__processor)
        
        
com1 = Computer('i5','16GB')
com2 = Computer('i3','8GB')


com1.config()
com2.config()
com1.compare(com2)

#binding of object data and its methoda together