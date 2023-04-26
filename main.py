# This is a program for a slot machine
# which predicts a win or a loss in play.
import random

MAX_LINES = 3
MAX_BET = 100000
MIN_BET = 5000

ROWS = 3
COLS = 3
# Dictionary to hold the play values for the slot machine
symbol_count = {
    "A":2,
    "B":1,
    "C":3,
    "D":0
}
# Function to check winnings in an instance play
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line +1)
    return winnings, winning_lines

# function to get the slot machine spins
# using the random module to display values randomly
def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)- 1:
                print(column[row], end="|")
            else:
                print(column[row],end="")
        print()

# this allows the player to enter their details
# also checks if they are eligible to play the game
def get_player_details():
    while True:
        full_name = input("What is your name?"+"(Hint:Your full names)")
        date_of_birth = input("In which year were you born?")
        current_age = 2023 - int(date_of_birth)
        nick_name = input("Which nickname do you prefer?")
        if current_age > 18:
            print(f"You're welcome {nick_name}")
            print("This is Fantasy Slot Machine. Terms and Conditions Apply")
            break
        else:
            print(f"Ooops {nick_name}, you're below 18 and not eligible to play this kind of game")
    return nick_name

# this allows the player to enter the amount to deposit
# also checks if the amount is an int or not

def deposit():
    while True:
        amount = input("Enter amount to deposit:  Ugshs")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Minimum deposits should be greater than 0")
        else:
            print("Enter amount in digits")
    return amount
# this allows the player to enter the number of lines to bet on
# also checks if the number is an int or not
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Minimum number of lines is 1")
        else:
            print("Number of lines must be in digits")
    return lines
# this function allows the player to enter the amount to use for betting
# also checks if the amount is an int or not between the max and minimum bet
def get_bet():
    while True:
        bet = input("Enter amount to bet on each line")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Valid bet must be between ugshs{MIN_BET}-ugshs{MAX_BET}")
        else:
            print("Please bet in digits")
    return bet

def game_check(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You have insufficient balance to place your bet. Your current account balance is {balance}.")
            print("Please recharge to play")
        else:
            break

    print(f"You have placed a bet of ugshs{bet} on {lines}lines with a total bet of ugshs{total_bet}")
    slots = get_slot_machine_spins(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print_slot_machine(slots)
    print(f"Congratulations,You have won ugshs{winnings} on lines:", *winning_lines)
    return winnings - total_bet

# main function to run our slot machine
def main():
    names = get_player_details()
    balance = deposit()
    while True:
        print(f"Your current account balance is {balance}")
        spin = input("Press enter button to play(q to quit)")
        if spin == "q":
            break
        balance += game_check(balance)
        print(f"Your remaining balance is {balance}")



main()