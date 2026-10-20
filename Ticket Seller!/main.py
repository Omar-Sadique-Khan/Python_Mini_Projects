# 😊 Ticket Seller!
# A simple Python Project for beginners to practice loops!

tickets = 100 # 👍Set any value you want

while True:
    n = int(input('Buy Tickets: '))

    # ✅ Ensure enough tickets to sell
    if tickets - n < 0:
        print('⚠️ Not enough tickets. Try again.')
        continue

    # 💸Sell Tickets
    tickets -= n
    print(f'Tickets Left: {tickets}')

    if tickets == 0:
        print('Sold Out!')
        break