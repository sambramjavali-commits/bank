def bankoper(initialbal, deposit, withdraw):
    totalBal = initialbal + deposit
    updatebal = totalBal - withdraw
    return totalBal, updatebal


if __name__ == "__main__":
    initialbal = int(input("Enter amount as initial balance: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter withdrawal amount: "))

    totalBal, updatebal = bankoper(initialbal, deposit, withdraw)

    print("Total balance:", totalBal)
    print("Updated balance:", updatebal)