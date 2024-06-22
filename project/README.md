# PASSWORD NOTEPAD
### Video Demo:  <URL HERE>
### Description: This is a password generator and a notepad to keep the generated passwords

- We can create passwords and save their entries to a txt file.
- We can read the contents of the notepad to look for all the passwords.
- We can read an especific password entry passing as argument the 'service' name which the password is for.
- The passwords can be created with sizes between 8 and 32 characters. This includes numbers, letters(upper and lower) and special characters.

### Usage:
- To create and keep a password, we execute the program passing the 'w' argument.
    Then it will ask for the email, service and the size of the password you want to create:

    $ python project w

- To search for a password, we pass the argument 'r' and a the name of the password's 'service' you want to find:

    $ python project r edx.org

- To read all the passwords in the notebook we pass the 'r' argument but without especifying a service

    $ python project r

- Note that at least one argument is mandatory, either 'r' or 'w'. Otherwise you will get the error:

    $ Must inform at least one command('r' or 'w')