from enum import Enum

class OrderStatus(Enum):
    UNSHIPPED, PENDING,SHIPPED,COMPLETED,CANCELLED = 0,1,2,3,4
    
class ShipmentStatus(Enum):
    PENDING,SHIPPED,DELIVERED,ONHOLD = 0,1,2,3
    
class PaymentStatus(Enum):
    UNPAID, PAID,CANCELLED,REFUNDED,FAILED = 0,1,2,3,4
    
class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
        
