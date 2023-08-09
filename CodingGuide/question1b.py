
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass


class RegularProduct(Product):
    def calculate_price(self):
        return self.price


class DiscountedProduct(Product):
    def __init__(self, price, discount):
        super().__init__(price)
        self.discount = discount

    def calculate_price(self):
        discounted_price = self.price * (1 - self.discount)
        return discounted_price


def calculate_total_price(products):
    total_price = sum(product.calculate_price() for product in products)
    return total_price


# Using the calculate_total_price function with a list of products
products = [RegularProduct(100), RegularProduct(50), DiscountedProduct(75, 0.2)]  # 20% discount on the last product
print("Total Price:", calculate_total_price(products))
