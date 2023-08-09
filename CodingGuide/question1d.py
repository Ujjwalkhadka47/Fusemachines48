

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

class PaymentOnlyProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

# Example usage
if __name__ == "__main__":
    online_processor = OnlinePaymentProcessor()
    online_processor.process_payment(100)
    online_processor.process_refund(50)

    payment_only_processor = PaymentOnlyProcessor()
    payment_only_processor.process_payment(200)
