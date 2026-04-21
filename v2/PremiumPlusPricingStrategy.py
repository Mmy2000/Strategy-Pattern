
from PricingStrategy import PricingStrategy


class PremiumPlusPricingStrategy(PricingStrategy):

    def calculate_price(self, price):
        return price * 0.7