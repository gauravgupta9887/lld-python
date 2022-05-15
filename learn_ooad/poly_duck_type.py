class PyCharm:
    def execute(self):
        print("Compile")
        print("run programs")
        
class MyEditor:
    def execute(self):
        print("Compile")
        print("run programs")
        print("spell checker")
        
class Laptop:
    def code(self,ide):
        ide.execute()
        
l = Laptop()
p = PyCharm()
m = MyEditor()
l.code(p)
l.code(m)

        