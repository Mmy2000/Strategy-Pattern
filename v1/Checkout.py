from PaymentMethod import PaymentMethod

class Checkout:

    def process_payment(self , amount:float , payment_method : PaymentMethod):
        if payment_method == PaymentMethod.VISA_CARD:
            print(f"Processing payment with visa card for amount {amount}")
            print("Calculating fees of the amount for visa cards...")
        elif payment_method == PaymentMethod.PAYPAL:
            print(f"Processing payment with paypal for amount {amount}")
            print("Calculating fees of the amount for paypal...")
        elif payment_method == PaymentMethod.BANK_TRANSFER:
            print(f"Processing payment with bank transfer for amount {amount}")
