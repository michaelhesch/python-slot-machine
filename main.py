'''
Python slot machine demo project
Created following tutorial https://www.youtube.com/watch?v=th4OBktqK1I&t=138s
'''
# Define global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Define deposit function to get amount from user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Define number of lines to play
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Define bet amount per line
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount    

# Define main function for game
def main():
    # Calls balance function to get balance
    balance = deposit()
    lines = get_number_of_lines()
    



# call main function, allows playing repeatedly
main()
