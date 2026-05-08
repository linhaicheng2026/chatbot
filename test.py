import sys,pyperclip
if len(sys.argv[1])<2:
    sys.exit()
password={'qq':'2342dfdsf','email':'3fdfsdf'}
account=sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
print('you are already copy the password')
    



