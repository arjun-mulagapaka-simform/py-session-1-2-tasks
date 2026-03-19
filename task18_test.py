import pytest
from task18 import Calculator

@pytest.mark.parametrize("a,b,output",[
    (1,2,3),
    (-1,1,0),
    (0,0,0)
])
def tests_for_add(a,b,output):
    assert Calculator.add_numbers(a,b) == output
    
def tests_for_exception_add():
    with pytest.raises(TypeError):
        Calculator.add_numbers("2",4)

@pytest.mark.parametrize("a,b,output",[
    (1,2,-1),
    (-1,1,-2),
    (5.5,4,1.5)
])
def tests_for_subtract(a,b,output):
    assert Calculator.subtract_numbers(a,b) == output

def tests_for_exception_subtract():
    with pytest.raises(TypeError):
        Calculator.subtract_numbers("2",4)

@pytest.mark.parametrize("a,b,output",[
    (1,2,2),
    (-1,1,-1),
    (0,0,0)
])
def tests_for_multiply(a,b,output):
    assert Calculator.multiply_numbers(a,b) == output
    
def tests_for_exception_multiply():
    with pytest.raises(TypeError):
        Calculator.multiply_numbers("2",4)

@pytest.mark.parametrize("a,b,output",[
    (2,4,0.5),
    (-1,1,-1),
    (10,2,5)
])
def tests_for_divide(a,b,output):
    assert Calculator.divide_numbers(a,b) == output
    
def tests_for_exception_divide():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(4,0)
    with pytest.raises(TypeError):
        Calculator.divide_numbers("2",4)

@pytest.mark.parametrize("a,b,output",[
    (1,2,1),
    (-1,1,-1),
    (0,0,1)
])
def tests_for_power(a,b,output):
    assert Calculator.power_numbers(a,b) == output
    
def tests_for_exception_power():
    with pytest.raises(TypeError):
        Calculator.power_numbers("2",4)

@pytest.mark.parametrize("a,output",[
    (4,2),
    (9,3),
    (0,0)
])
def tests_for_sqrt(a,output):
    assert Calculator.sqrt_number(a) == output
    
def tests_for_exception_sqrt():
    with pytest.raises(ArithmeticError):
        Calculator.sqrt_number(-2)
    with pytest.raises(TypeError):
        Calculator.sqrt_number("2")