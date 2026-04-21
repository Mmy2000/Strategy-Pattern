

from Checkout import Checkout
from MembershipType import MembershipType
from PaymentMethod import PaymentMethod
from Product import Product


def main():
    
    wallet : Product = Product("wallet" , 200)
    wallet_price = wallet.calculate_price(MembershipType.REGULAR)

    jacket : Product = Product("jacket" , 500)
    jacket_price = jacket.calculate_price(MembershipType.GOLD)

    dress : Product = Product("dress" , 1200)
    dress_price = dress.calculate_price(MembershipType.PREMIUM)

    checkout : Checkout = Checkout()
    checkout.process_payment(wallet_price,PaymentMethod.VISA_CARD)
    checkout.process_payment(jacket_price,PaymentMethod.PAYPAL)
    checkout.process_payment(dress_price,PaymentMethod.BANK_TRANSFER)


if __name__ == "__main__":
    main()