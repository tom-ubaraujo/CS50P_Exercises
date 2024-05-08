from um import count

def main():
    test_func_count()

def test_func_count():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1
    assert count("um") == 1
    assert count("that's so yummy") == 0
    assert count("lets um test this") == 1

if __name__ == "__main__":
    main()