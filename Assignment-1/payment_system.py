from abc import ABC,abstractmethod
from dataclasses import dataclass

# Item details of the order
@dataclass
class Item:
    name: str
    price: float
    quantity: int

# Order class
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    # Calculating  total number of items
    @property
    def total_items(self):
        return sum(item.quantity for item in self.items)

    # Calculating total price of the order
    @property
    def grand_total(self):
        return sum(item.price * item.quantity for item in self.items)

# Payment method parent class
class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

# Razorpay card payment
class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Razorpay Card"

    def pay(self, amount):
        print("Paying", amount, "using Razorpay Card")
        return True

# Razorpay UPI payment
class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Razorpay UPI"

    def pay(self, amount):
        print("Paying", amount, "using Razorpay UPI")
        return True

# Stripe card payment
class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Stripe Card"

    def pay(self, amount):
        print("Paying", amount, "using Stripe Card")
        return True

# Stripe UPI payment
class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Stripe UPI"

    def pay(self, amount):
        print("Paying", amount, "using Stripe UPI")
        return True

# Factory for creating payment methods
class FactoryPaymentMethod(ABC):
    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type in cls.factory:
            return cls.factory[method_type](**kwargs)
        raise ValueError("Invalid payment method")

# Razorpay payment factory
class RazorpayFactory(FactoryPaymentMethod):
    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }

# Stripe payment factory
class StripeFactory(FactoryPaymentMethod):
    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }

# Aggregator parent class
class Aggregator(ABC):
    def __init__(self, name, processing_fee, factory):
        self.name = name
        self.processing_fee = processing_fee
        self.factory = factory

    # Create payment object and process payment
    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.factory.get_payment_object(method_type, **kwargs)

        # Calculate processing fee
        fee = amount * self.processing_fee / 100
        total = amount + fee

        print("Payment method:", payment.get_details())
        print("Processing fee:", fee)

        return payment.pay(total)

# Razorpay aggregator
class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay", 2.0, RazorpayFactory)

# Stripe aggregator
class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe", 2.9, StripeFactory)

# Factory for selecting payment aggregator
class AggregatorFactory:
    factory = {
        "razorpay": RazorpayAggregator,
        "stripe": StripeAggregator
    }

    @classmethod
    def get_aggregator_object(cls, name):
        if name in cls.factory:
            return cls.factory[name]()
        raise ValueError("Invalid aggregator")

# Take order items from the user
def get_order_items():
    items = []

    while True:
        name = input("Enter item name (or done): ")

        if name.lower() == "done":
            break

        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))

            if price < 0 or quantity <= 0:
                print("Enter valid price and quantity")
                continue

            items.append(Item(name, price, quantity))

        except ValueError:
            print("Please enter numbers for price and quantity")

    return items

# Main function
def main():
    print("Welcome to Order Processing System")
    print("Multi-Gateway Payment Processing")
    order_id = input("Enter order ID: ")

    # Get items for the order
    items = get_order_items()

    if len(items) == 0:
        print("No items added")
        return

    # Create order object
    order = Order(order_id, items)

    print("Total items:", order.total_items)
    print("Grand total:", order.grand_total)

    # Select payment gateway
    print()
    print("Select Payment Gateway")
    print("1. Razorpay")
    print("2. Stripe")

    gateway = input("Enter choice: ")

    if gateway == "1":
        gateway = "razorpay"
    elif gateway == "2":
        gateway = "stripe"
    else:
        print("Invalid gateway")
        return

    # Select payment method
    print()
    print("Select Payment Method")
    print("1. Card")
    print("2. UPI")

    choice = input("Enter choice: ")

    if choice == "1":
        method = "card"
    elif choice == "2":
        method = "upi"
    else:
        print("Invalid payment method")
        return

    try:
        # Get the selected aggregator
        aggregator = AggregatorFactory.get_aggregator_object(gateway)

        # Take card details
        if method == "card":
            card_number = input("Enter card number: ")

            result = aggregator.call_get_payment_object(
                method,
                order.grand_total,
                card_number=card_number
            )
        # Take UPI details
        else:
            upi_id = input("Enter UPI ID: ")

            result = aggregator.call_get_payment_object(
                method,
                order.grand_total,
                upi_id=upi_id
            )

        if result:
            print("Payment successful")

    except ValueError as e:
        print(e)

# Start the program
if __name__ == "__main__":
    main()