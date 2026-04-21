
from PaymentStrategy import PaymentStrategy


class VisaCardPaymentStrategy(PaymentStrategy):

    def process_payment(self,amount):
        print(f"Processing payment with visa card for amount {amount}")
        print("Calculating fees of the amount for visa cards...")