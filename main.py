'''
Python slot machine demo project
Created following tutorial https://www.youtube.com/watch?v=th4OBktqK1I&t=138s
'''
# Import modules
import random

# Define global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Dict for number of symbols on each wheel, not balanced for realistic odds 
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Define function to generate slot machine spins
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Loop through and add possilbe combinations of symbols to list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    # Create nested list of symbols for columns (not rows)
    columns = []
    # Loop to create set of symbols for the rows in each column
    for _ in range(cols):
        # List that will nest in columns var
        column = []
        # Copy of all symbols list, so we can remove selected values
        # Create copy using the slice operator ":" to prevent overwriting original list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # remove choice from copied list
            current_symbols.remove(value)
            # add value to column list
            column.append(value)
        # add column list to columns list outside loop
        columns.append(column)
    
    return columns

# Define function to visualize the columns
def print_slot_machine(columns):
    # Need to transpose data in columns matrix to visualize
    # Loop through columns list and print each row
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        # Print new line after each row        
        print()

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
        amount = input("What would you like to bet on each line? $")
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
    # Call bet function in loop to check bet is within balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

# call main function, allows playing repeatedly
main()
