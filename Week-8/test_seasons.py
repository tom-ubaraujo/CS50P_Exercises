from seasons import gen_text

def test_gen_text():
    assert gen_text(1054080) == "One million, fifty-four thousand eighty minutes"


def main():
    test_gen_text()

if __name__ == '__main__':
    main()