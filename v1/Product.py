
from MembershipType import MembershipType


class Product:

    def __init__(self , name , price) -> None:
        self._name = name
        self._price = price

    def calculate_price(self,member_ship_type : MembershipType):
        if member_ship_type == MembershipType.REGULAR:
            return self._price
        elif member_ship_type == MembershipType.GOLD:
            return self._price * 0.9
        elif member_ship_type == MembershipType.PREMIUM:
            return self._price * 0.8
        else:
            return self._price


    def get_name(self):
        return self._name

    def set_name(self,name):
         self._name = name
        
    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price = price