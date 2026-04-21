
from PaymentStrategy import PaymentStrategy


class BankTransferPaymentStrategy(PaymentStrategy):

    def process_payment(self , amount):
        print(f"Processing payment with visa card for amount {amount}")