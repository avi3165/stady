#q1
from PIL.ImImagePlugin import split
from matplotlib.pyplot import title


class BankAccount:

    def __init__(self, initial_balance):
        self.__balance = initial_balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance-= amount
    def get_balance(self):
        return self.__balance
#q2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"the book {self.title} from {self.author}"
    def __repr__(self):
        return f"{self.title=}, {self.author=}"
    def __add__(self, other):
        new_title = self.title , other.title
        new_auther = self.author , other.author
        return  new_title,new_auther
#q3
class Contact:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} "
    @full_name.setter
    def full_name(self, full_name):
        parts = full_name.split(' ')
        self.first_name=parts[0]
        self.last_name=parts[1]

#q4
class Calculator:
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def multiply(a, b):
        return a*b
    @staticmethod
    def power(base, exponent):
        return base**exponent
    @staticmethod
    def is_even(number):
        return number%2==0
print(f"2 + 3 = {Calculator.add(2, 3)}")  # אמור להדפיס 5
print(f"4 * 5 = {Calculator.multiply(4, 5)}")  # אמור להדפיס 20
print(f"2^3 = {Calculator.power(2, 3)}")  # אמור להדפיס 8
print(f"7 זוגי? {Calculator.is_even(7)}")  # אמור להדפיס False