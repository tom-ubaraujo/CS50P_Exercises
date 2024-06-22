from project import validate_input, gen_password, write_file
import pytest

def test_validate_input():
    assert validate_input(['r']) == ('r', None)
    assert validate_input(['r','test']) == ('r','test')
    assert validate_input(['w']) == ('w', None)
    with pytest.raises(SystemExit) as e:
        validate_input([])
    assert e.type == SystemExit
    assert e.value.code == 1

def test_gen_password():
    assert gen_password() > ""
    assert gen_password(0) == ""

def test_write_file():
    assert write_file("edx.org", "test@google.com", "N?tZa?pYKR8%Q?n") == None

def test_write_file_output(capsys):
    write_file("edx.org", "test@google.com", "N?tZa?pYKR8%Q?n")
    captured = capsys.readouterr()
    assert captured.out == "Password generated: \nService: edx.org\nEmail: test@google.com\nPassword: N?tZa?pYKR8%Q?n\n\n"

def main():
    test_validate_input()
    test_gen_password()
    test_write_file()
    test_write_file_output()

if __name__ == '__main__':
    main()