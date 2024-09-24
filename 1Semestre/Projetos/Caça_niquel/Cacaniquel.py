import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winning(lines, columns, bet, values):
    winnings = 0
    winning_lines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for col in range(cols): #para cada coluna que o usuario escolher, esse for vai rodar
        column = [] 
        current_symbols = all_symbols[:] #[:] copia a lista
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()

def deposit():
    while True:
        amount = input("Insert the value of your deposit:$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The value must be greater than 0!")
        else:
            print("Please insert a number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please insert a number!")
    return lines

def get_bet():
    while True:
        amount = input("Insert the value of your bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount mus be beetwen ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please insert a number!")
    return amount
   
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to bet on all lines! your current balance is ${balance}")
            get_bet()
        else:
            break
    print(f"You are betting ${bet} on {lines} lines! Total bet = ${bet * lines}")
    
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(lines, slots, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"Winning lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print (f"Your current balance is ${balance}")
        answer = input("Press enter do play (q to quit): ")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"Your final balance is ${balance}")
    
main()
