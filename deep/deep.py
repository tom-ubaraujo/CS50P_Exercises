answer = input("What is the answer? ").lower().strip()

if answer == '42' or answer == 'forty-two' or answer == 'forty two':
    print('Yes')
else:
    print("No")