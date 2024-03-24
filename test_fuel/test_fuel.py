import pytest
from fuel import convert, gauge

def test_conversion():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_0_div():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("test/test")

