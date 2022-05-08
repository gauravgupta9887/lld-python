from autofactory import AutoFactory 

factory = AutoFactory()

for carname in ['Chervolet','Ford','Jeep','Tesla']:
    car = factory.creat_instance(carname)
    car.start()
    car.stop()