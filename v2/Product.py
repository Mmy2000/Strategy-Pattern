
from MembershipType import MembershipType
from PricingStrategy import PricingStrategy


class Product:

    def __init__(self , name , price , pricing_strategy:PricingStrategy) -> None:
        self._name = name
        self._price = price
        self._pricing_strategy = pricing_strategy

    def calculate_price(self):
        return self._pricing_strategy.calculate_price(self._price)
        

    def get_name(self):
        return self._name

    def set_name(self,name):
         self._name = name
        
    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price = price