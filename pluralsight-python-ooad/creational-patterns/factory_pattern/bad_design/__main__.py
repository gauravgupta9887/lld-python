from chervoletbeat import ChrevoletBeat
from fordfusion import FordFusion
from jeepcompass import JeepCompass
from nullcar import NullCar

def getcar(carname):
    if carname=='Chervolet':
        return ChrevoletBeat()
    elif carname=='Ford':
        return FordFusion()
    elif carname=='Jeep':
        return JeepCompass()
    else:
        return NullCar(carname)  # example of null pattern, if no previous condition met, return default


for carname in ['Chervolet','Ford','Jeep','Tesla']:
    car = getcar(carname)
    car.start()
    car.stop()