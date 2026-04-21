
from PricingStrategy import PricingStrategy


class GoldPricingStrategy(PricingStrategy):

    def calculate_price(self, price):
        return price * 0.9