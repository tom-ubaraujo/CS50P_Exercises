import re

"""
re.search() parameters
.       -> any character except a new line
*       -> 0 or more repetitions of characters
+       -> 1 or more repetitions of characters
?       -> 0 or 1 repetitions of characters
{m}     -> m repetitions
{m,n}   -> m-n repetitions
^       -> matches the start of the string
$       -> matches the end of the string

"""

email = input("Inform your email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid!")
else:
    print("Invalid!")