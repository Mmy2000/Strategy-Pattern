
from PaymentStrategy import PaymentStrategy


class PaypalPaymentStrategy(PaymentStrategy):

    def process_payment(self , amount):
        print(f"Processing payment with paypal for amount {amount}")
        print("Calculating fees of the amount for paypal...")