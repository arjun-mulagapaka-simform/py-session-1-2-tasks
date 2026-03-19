import math
class Calculator:
    @staticmethod
    def add_numbers(a,b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError
        return a+b
    
    @staticmethod
    def subtract_numbers(a,b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError
        return a-b
    
    @staticmethod
    def multiply_numbers(a,b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError
        return a*b
    
    @staticmethod
    def divide_numbers(a,b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError
        if b == 0:
            raise ZeroDivisionError
        return a/b
    
    @staticmethod
    def power_numbers(a,b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError
        return a**b
    
    @staticmethod
    def sqrt_number(a):
        if not isinstance(a,(int, float)):
            raise TypeError
        if a < 0:
            raise ArithmeticError
        return math.sqrt(a)