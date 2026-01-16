import pytest
from app import hello, factorial

def test_hello():
    assert hello() == "Hello from CI/CD!"

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)
