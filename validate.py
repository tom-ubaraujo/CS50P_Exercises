import re

"""
re.search() parameters
.       -> any character except a new line
*       -> 0 or more repetitions
+       -> 1 or more repetitions
?       -> 0 or 1 repetitions
{m}     -> m repetitions
{m,n}   -> m-n repetitions
"""

email = input("Inform your email: ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("valid!")
else:
    print("Invalid!")