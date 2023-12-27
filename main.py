MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What will you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 -" + str(MAX_LINE) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number.")
    return amount



def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    totalBet = bet * lines
    print(f"you are beting ${bet} on ${lines} lines your total bet is ${totalBet}")


main()
