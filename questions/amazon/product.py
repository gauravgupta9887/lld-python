class ProductCategory:
    def __init__(self,name,description):
        self.__name = name
        self.__description = description
        
class Product:
    def __init__(self,name,description,price,availale_item_count,category):
        self.__name = name
        self.__description = description
        self.__price = price 
        self.__availale_item_count = availale_item_count
        self.__category = category
        self.__review = []
    
    @property
    def get_available_count(self):
        return self.__availale_item_count
    
class ProductReview:
    def __init__(self,review,rating):
        self.__review = review 
        self.__rating = rating
        
    def get_rating(self):
        return self.__rating