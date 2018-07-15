#Author: Jackson Ross jrr4557
#Homework 2 - Song Sales
#Due Date: 09/14/17
#Description: This program calculates the bill for a customer using their membership status and number of songs purchased. Non-members are offered membership.


#prompt user for name, number of songs purchased, and their membership status
customer_name = input('Enter your first and last name: ')
songs_purchased = int(input('Enter the number of songs purchased: '))
membership_type = input('Enter your membership status (R for Regular; P for Premium): ')


#if the user is not a member, ask if they would like to become a member
if(membership_type == 'R'):
    subscribe = input('Would you like to become a member for $9.95? (Y for Yes; N for No) ')
    if(subscribe == 'Y' ):
        membership_fee = 9.95
        print('Congratulations and thank you for your membership purchase!')
        membership_type = 'P'
    else:
        print('Thank you for your response.')
        membership_fee = 0
else:
    membership_fee = 0


#Use the user input to determine the price they pay and the number of free songs they get
if(membership_type == 'R'):
    if(songs_purchased < 10):
        song_price = 1.39
        free_songs = 0
    elif(songs_purchased <= 15):
        song_price = 1.34
        free_songs = 1
    else:
        song_price = 1.29
        free_songs = 2
elif(membership_type == 'P'):
    if(songs_purchased < 12):
        song_price = 1.29
        free_songs = 0
    elif(songs_purchased <= 18):
        song_price = 1.24
        free_songs = 2
    else:
        song_price = 1.19
        free_songs = 4


#calculate totals before printing
total_songs = songs_purchased + free_songs
total_cost = songs_purchased * song_price
tax_owed = .0825 * total_cost
total_owed = tax_owed + total_cost + membership_fee


#print the billing summary to the screen
print()
print('Customer Name: ', customer_name)

if(membership_type == 'P'):
    print('Customer Type: Premium')
elif(membership_type == 'R'):
    print('Customer Type: Regular')

print('Number of Songs Received:', total_songs)
print('Pre-Tax Total: $', format(total_cost, '.2f'), sep='')
print('Sales Tax: $', format(tax_owed, '.2f'), sep='')

#do not print a membership fee if they did not become a member during the transaction
if(membership_fee != 0):
    print('Membership Fee: $', membership_fee, sep='')

print('Total Amount Due: $', format(total_owed, '.2f'), sep='')


