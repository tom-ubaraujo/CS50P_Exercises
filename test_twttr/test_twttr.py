from twttr import shorten

def test_shorten():
    assert shorten("TOM") == "TM"
    assert shorten("ugleiston") == "glstn"

def test_punctuation():
    assert shorten("TOM?") == "TM?"
    assert shorten("ugleist0n") == "glst0n"