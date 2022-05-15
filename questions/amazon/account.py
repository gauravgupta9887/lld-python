from msilib.schema import Property


class Account:
    def __init__(self,user_name,password,name,shipping_address,email,phone):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__shipping_address = shipping_address
        self.__email = email
        self.__phone = phone
        
    # def add_product_review(self):
        # None
        
    # def add_product(self):
        # None 
        
    @property
    def get_shipping_address(self):
        return self.__shipping_address
        
    
    