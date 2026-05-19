from cal import squ
import pytest

def test_positive():
    assert squ(2) == 4
    assert squ(3) == 9   

    
def test_negative():
    assert squ(-2) == 4
    assert squ(-3) == 9

def test_zero():
    assert squ(0) == 0

def test_str():
    with pytest.raises(TypeError):
        squ("cat")
"""
def test_str():
    with pytest.raises(TypeError):
        {(any thing that raises TypeError)}

If anything inside the with block raises a TypeError, the test passes
 — it doesn't have to be squ("cat") specifically.

"""

