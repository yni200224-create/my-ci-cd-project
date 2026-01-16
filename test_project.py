import pytest
import random
import math
from project import my_start_str, my_factorial

def test_factorial():
    n = random.randint(0, 20)
    assert my_factorial(n) == math.factorial(n)

def test_str():
    assert my_start_str() == "Hello world!"
