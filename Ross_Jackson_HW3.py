#Author: Jackson Ross jrr4557
#Homework 3 - BBQ Menu
#Due Date: 09/22/17
#Description: This program takes a user's order from the menu (including
#             quantities and sizes), validates the user input, and displays
#             a receipt with all of the order information and totals

#display menu
print('MENU ITEMS                   PRICES')
print('MEAT')
print('1. Brisket - Extra Lean      $15.69 per lb.')
print('2. Brisket - Moist           $16.19 per lb.')
print()
print('SIDE ITEMS')
print('3. Cole slaw                 $1.89 sm  $6.49 lg')
print('4. Potato salad              $1.79 sm  $6.19 lg')
print('5. Complete my order')
print()

#prompt user for name and take first order
customer_name = input('Please enter your name: ')
order = int(input('Please enter the number of the item you wish to purchase: '))

#create 'total' variables for use within loop
total_price = 0
total_weight = 0
total_sides = 0

#validate user input for order (1-5 only)
while order < 1 or order > 5:
    order = int(input('That is not a valid input. Please enter a number 1-5: '))

#if the user orders nothing and hits complete, thank them and end the program there
if order == 5:
    print('\nPurchase cancelled. Thank you for visiting!')
#otherwise do this
else:
    #this will allow the user to press 5 to complete their order
    while order != 5:
        #meat calculations
        if order == 1 or order == 2:
            weight = float(input('How many lbs. would you like? '))
            #validate user input for weight (>0 only)
            while weight <= 0:
                weight = float(input('That is not a valid input. Please enter a positive number: '))
            total_weight += weight
            if order == 1:
                total_price += (weight * 15.69)
            else:
                total_price += (weight * 16.19)
        #side calculations
        else:
            size = input('What size? (S or L) ')
            #validate user input for size ('S' or 'L' only)
            while size != 'S' and size != 'L':
                size = input('Invalid input. Please enter S or L: ')
            quantity = int(input('How many would you like? '))
            #validate user input for quantity (>0 only)
            while quantity < 1:
                quantity = int(input('Invalid input. Please enter a positive number: '))
            if order == 3:
                if size == 'S':                   
                    total_price += (1.89*quantity)
                    total_sides += quantity
                else:
                    total_price += (6.49*quantity)
                    total_sides += quantity
            else:
                if size == 'S':                   
                    total_price += (1.79*quantity)
                    total_sides += quantity
                else:
                    total_price += (6.19*quantity)
                    total_sides += quantity
        #take next order and validate the input (1-5 only)
        order = int(input('Enter the number of the next item: '))
        while order < 1 or order > 5:
            order = int(input('That is not a valid input. Please enter a number 1-5: '))

    #calculate sales tax and the total due after the tax
    sales_tax = .0825 * total_price
    total_due = total_price + sales_tax

    #print receipt
    print()
    print('Name: ',customer_name)
    print('Total Weight:',format(total_weight,'.2f'),'lbs.')
    print('Total Sides: ', total_sides)
    print('Subtotal: $',format(total_price,'.2f'), sep='')
    print('Sales Tax: $',format(sales_tax,'.2f'),sep='')
    print('Total Amount Due: $',format(total_due,'.2f'),sep='')
                
            
    
