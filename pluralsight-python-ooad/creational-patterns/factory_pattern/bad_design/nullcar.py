class NullCar(object):
    
    def __init__(self,carname):
        self.carname = carname

    def start(self):
        print(f'unknown car: {self.carname}')

    def stop(self):
        pass