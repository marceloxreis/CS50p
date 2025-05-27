amount = 50
while amount > 0:
    money = int(input("Insert Coin: "))
    if money in [5, 10, 25]:  # Only accept valid coin values
        amount -= money
        if amount > 0:
            print(f"Amount Due: {amount}")
        else:
            print(f"Change Owed: {abs(amount)}")
    else:
        print(f"Amount Due: {amount}")
