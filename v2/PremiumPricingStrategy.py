
from PricingStrategy import PricingStrategy


class PremiumPricingStrategy(PricingStrategy):

    def calculate_price(self, price):
        return price * 0.8