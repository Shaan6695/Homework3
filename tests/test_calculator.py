'''My Calculator Test'''
from calculator import add, subtract, multiply

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Testing1 that subtrdaction function works '''    
    assert subtract(2,2) == 0

def test_multiply():
    """Testing multiply"""
    assert multiply(2,2) == 4
    