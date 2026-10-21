#➕ Summifier!
#😊 A simple project for summing all the digits in a number until a single digit is outputted.

def get_digital_root(num):
    # Base Case: If the number is already a single digit, return it
    if num < 10:
        return num

    # Step 1: Sum the digits of the current number
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp = temp // 10

    # Step 2: Recursive Call (Pass the new sum back into the function)
    return get_digital_root(digit_sum)


# --- How to run it ---
user_input = int(input("Enter a number: "))
result = get_digital_root(user_input)
print(f"The single-digit result is: {result}")
