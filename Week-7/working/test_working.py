from working import convert
import pytest

def test_incorrect():
    with pytest.raises(ValueError):
        convert("8 AM - 10 PM")
    with pytest.raises(ValueError):
        convert("08:00 AM - 10:00 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 10 PM")
    with pytest.raises(ValueError):
        convert("8AM to 10PM")
    with pytest.raises(ValueError):
        convert("8 AM to 0 PM")

def test_incorrect_hour():
    with pytest.raises(ValueError):
        convert("14 PM to 18 PM")
    with pytest.raises(ValueError):
        convert("10 PM to 18 AM")

def test_incorrect_min():
    with pytest.raises(ValueError):
        convert("8:60 AM to 7:40 PM")
    with pytest.raises(ValueError):
        convert("8:30 AM to 7:60 PM")

def test_correct():
    assert convert('5 AM to 9 PM') == '05:00 to 21:00'
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def main():
    test_incorrect()
    test_incorrect_hour()
    test_incorrect_min()
    test_correct()

if __name__ == '__main__':
    main()