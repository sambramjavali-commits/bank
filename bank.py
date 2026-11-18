import sys

def bankoper(initialbal, deposit, withdraw):
    totalBal = initialbal + deposit
    updatebal = totalBal - withdraw
    return totalBal, updatebal


if __name__ == "__main__":
    initialbal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalBal, updatebal = bankoper(initialbal, deposit, withdraw)

    print("Total balance:", totalBal)
    print("Updated balance:", updatebal)