from plates import is_valid

def test_length():
    assert is_valid("co") == True
    assert is_valid("abacat") == True
    assert is_valid("a9") == False
    assert is_valid("macarronada") == False

def test_begin_num():
    assert is_valid("ramen") == True
    assert is_valid("r4men") == False
    assert is_valid("74men") == False

def test_num_mid():
    assert is_valid("soup1") == True
    assert is_valid("so1ps") == False

def test_init_zero():
    assert is_valid("bisco1") == True
    assert is_valid("bisc01") == False

def test_alphanum():
    assert is_valid("bi..to") == False
