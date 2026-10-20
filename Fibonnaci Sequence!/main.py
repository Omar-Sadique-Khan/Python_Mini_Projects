# 🔢 Fibonacci Sequence (e.g., 0 1 1 2 3 5 8 13 21 34, etc.)

# 🫈🔢 Big number's name list
number_names = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]


x = 0
y = 1

for i in range(int(input("Select a number: "))): # The for-loop runs through user Input.

    num = f"{x: ,d}"
    count_commas = num.count(",")
    large_num = number_names[count_commas]

    print(num, large_num)

    z = x + y

    x = y
    y = z
