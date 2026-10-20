#🔒🔑 Password Checker!

#📦 Variables
symbols = '!@#$%^&*()_+~{}|[]><?'

#👉 User Inputs
print('✅ Creating new account')

Username = input('Username: ')
password = input('Password: ')

print('-' * 50)

#📦 Placeholders

check_length = False
check_digit  = False
check_upper  = False
check_lower  = False
check_symbol = False
check_no_spaces = False

#🔐 Security Checks

#✔️ Length (Minimum 8 characters)

if len(password) >= 8:
    check_length = True

#✔️ Contains no spaces
if ' ' not in password:
    check_no_spaces = True

for char in password:

    #✔️ Contains at least one digit

    if char.isdigit():
        check_digit = True

    #️️️✔️ Contains at least one uppercase character

    elif char.isupper():
        check_upper = True

    #✔️ Contains at least one lowercase character

    elif char.islower():
        check_lower = True

    #✔️ Contains at least one special character

    elif char in symbols:
        check_symbol = True

# Display Results

checks = [
    check_length,
    check_digit,
    check_upper,
    check_lower,
    check_symbol,
    check_no_spaces
]

if all(checks):
    print('✅ Password is very strong!')
else:
    print('Password is very weak!')

    if not check_length:
        print('❌ - At least 8 characters are required.')

    if not check_digit:
        print('❌ - At least 1 digit is required.')

    if not check_upper:
        print('❌ - At least 1 uppercase letter is required.')

    if not check_lower:
        print('❌ - At least 1 lowercase letter is required.')

    if not check_symbol:
        print(f'❌ - At least 1 symbol is required. ({symbols})')

    if not check_no_spaces:
        print('❌ - Should contain no spaces.')
