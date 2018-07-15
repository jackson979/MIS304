#Author: Jackson Ross jrr4557
#Homework 4 - Bank Account Manipulation
#Due Date: 10/09/17
#Description: This program can take user input for a menu and perform various banking operations (deposit, withdraw, and view interest)

#create constants
INT_RATE1 = .02
INT_RATE2 = .035
INT_RATE3 = .05
DEPOSIT = 'D'
WITHDRAW = 'W'
INTEREST = 'I'
EXIT = 'E'


#display menu
def menu():
    print()
    print('LONGHORN BANK MENU')
    print('D. Make a deposit')
    print('W. Make a withdrawal')
    print('I. Calculate interest')
    print('E. Exit')

#prompt user for starting balance and validate
def starting_balance():
    start_bal = float(input('Please enter your starting balance: '))
    while start_bal < 0:
        start_bal = float(input('Invalid input. Please enter a non-negative balance: '))
    return start_bal

#prompt user for menu choice and validate
def menu_option():
    choice = input('Please enter the letter of a menu option: ')
    while choice != DEPOSIT and choice != WITHDRAW and choice != INTEREST and choice != EXIT:
        choice = input('Invalid input. Please enter a valid menu option: ')
    return choice

#calculate interest based on balance
def interest(bal):
    if bal >= 5000:
        interest = INT_RATE3 * bal
        interest_rate = INT_RATE3 * 100
        print('Interest: $', format(interest,',.2f'), ' at ',format(interest_rate,'.1f'),'%',sep='')
    elif bal >=2500:
        interest = INT_RATE2 * bal
        interest_rate = INT_RATE2 * 100
        print('Interest: $', format(interest,',.2f'), ' at ',format(interest_rate,'.1f'),'%',sep='')
    else:
        interest = INT_RATE1 * bal
        interest_rate = INT_RATE1 * 100
        print('Interest: $', format(interest,',.2f'), ' at ',format(interest_rate,'.1f'),'%',sep='')
    
    
#prompt user for withdrawal amount and validate
def withdraw_valid(bal):
    withdraw_amount = float(input('Enter withdrawal amount: '))
    while withdraw_amount <= 0 or withdraw_amount > bal:
        withdraw_amount = float(input('Invalid input. Enter a positive value that does not exceed your balance: '))
    return withdraw_amount

#prompt user for deposit amount and validate
def deposit_valid():
    deposit_amount = float(input('Enter deposit amount: '))
    while deposit_amount <= 0:
        deposit_amount = float(input('Invalid input. Enter a positive deposit value: '))
    return deposit_amount

#print balance
def print_balance(bal):
    print('Balance: $', format(bal,',.2f'), sep='')
    
#print final statement
def statement(bal,dep_ct,dep_tot,with_ct,with_tot):
    print()
    print('# of Deposits: ', dep_ct)
    print('Total Deposit Amount: $',format(dep_tot,',.2f'),sep='')
    print('# of Withdrawals: ', with_ct)
    print('Total Withdrawal Amount: $',format(with_tot,',.2f'),sep='')
    interest(bal)
    print_balance(bal)
 
#define main function
def main():
    
    #create empty variables
    dep_count = 0
    total_dep = 0
    with_count = 0
    total_with = 0

    #prompt user for name and starting balance
    name = input('Please enter your name: ')
    balance = starting_balance()

    #call menu and menu_option functions
    menu()
    menu_choice = menu_option()

    #determine what user does based on menu_option return value
    if menu_choice == EXIT:
        statement(balance,dep_count,total_dep,with_count,total_with)
    else:
        while menu_choice != EXIT:
            if menu_choice == DEPOSIT:
                dep_amt = deposit_valid()
                balance += dep_amt
                dep_count += 1
                total_dep += dep_amt
                print()
                print_balance(balance)
                menu()
                menu_choice = menu_option()
            elif menu_choice == WITHDRAW:
                with_amt = withdraw_valid(balance)
                balance -= with_amt
                with_count +=1
                total_with += with_amt
                print()
                print_balance(balance)
                menu()
                menu_choice = menu_option()
            else:
                print()
                interest(balance)
                menu()
                menu_choice = menu_option()
        statement(balance,dep_count,total_dep,with_count,total_with)

#call main function
main()

