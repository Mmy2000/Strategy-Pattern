

from Checkout import Checkout
from MembershipType import MembershipType
from PaymentMethod import PaymentMethod
from Product import Product
from GoldPricingStrategy import GoldPricingStrategy
from PremiumPricingStrategy import PremiumPricingStrategy
from RegularPricingStrategy import RegularPricingStrategy
from PaypalPaymentStrategy import PaypalPaymentStrategy
from BankTransferPaymentStrategy import BankTransferPaymentStrategy
from VisaCardPaymentStrategy import VisaCardPaymentStrategy
from PremiumPlusPricingStrategy import PremiumPlusPricingStrategy


def main():
    
    wallet : Product = Product("wallet" , 200,RegularPricingStrategy())
    wallet_price = wallet.calculate_price()

    jacket : Product = Product("jacket" , 500, GoldPricingStrategy())
    jacket_price = jacket.calculate_price()

    dress : Product = Product("dress" , 1200,PremiumPricingStrategy())
    dress_price = dress.calculate_price()

    shirt : Product = Product("shirt" , 150 , PremiumPlusPricingStrategy())
    shirt_price = shirt.calculate_price()
    
    paypal_payment = PaypalPaymentStrategy()
    visa_card = VisaCardPaymentStrategy()
    bank_transfer = BankTransferPaymentStrategy()

    checkout_1 : Checkout = Checkout(paypal_payment)
    checkout_2 : Checkout = Checkout(visa_card)
    checkout_3 : Checkout = Checkout(bank_transfer)
    checkout_1.process_payment(wallet_price)
    checkout_2.process_payment(jacket_price)
    checkout_3.process_payment(dress_price)
    checkout_3.process_payment(shirt_price)


if __name__ == "__main__":
    main()