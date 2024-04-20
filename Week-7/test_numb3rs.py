from numb3rs import validate

def test_ip_valid1():
    assert validate("1.2.3.4") == True
def test_ip_valid2():
    assert validate("255.255.255.255") == True
def test_ip_invalid1():
    assert validate("300.2.3.4") == False
def test_ip_invalid2():
    assert validate("1.1.1.1000") == False
def test_ip_invalid3():
    assert validate("-1.1.1.1") == False
def test_ip_invalid3():
    assert validate("cat") == False