from bank import value

def test_lower():
    assert value("HELLO, MR TOM") == 0

def test_20():
    assert value("how you doing?") == 20

def test_100():
    assert value("What's happening?") == 100

def test_incorrect():
    assert value("Testing incorrect") == 100