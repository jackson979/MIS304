#Author: Jackson Ross jrr4557
#Homework 1 - Profit Margin Analysis
#Due Date: 09/11/17
#Description: This program takes in user input on various product details and returns a report on the profit percentage and other information about the product.



#Prompt user for product name
product_name = input("Product Name: ")

#Prompt user for product's original price
original_price = float(input("Product's Original Price: "))

#Prompt user for product cost
product_cost = float(input("Product Cost: "))

#Prompt user for quantity of product sold
quantity_sold = int(input("Quantity Sold: "))

#Prompt user for sales discount on product and convert it into a decimal
sales_discount = float(input("Sales Discount(%): "))/100



#calculate total revenue (original price * quantity sold)
total_revenue = quantity_sold * original_price

#calculate total cost (product cost * quantity sold)
total_cost = product_cost * quantity_sold

#calculate total discount offered (original price * discount)
discount_offered = total_revenue * sales_discount

#calculate total profit (total revenue - total cost - total discount offered)
total_profit = total_revenue - total_cost - discount_offered

#calculate percentage profit for the product (total profit / total revenue)
percentage_profit = (total_profit/total_revenue) * 100



#print a blank line to separate input from output
print()

#display product name
print("Product Name: " + product_name)

#display total revenue
print("Total Revenue: $",format(total_revenue,'.2f'),sep='')

#display total cost
print("Total Cost: $",format(total_cost,'.2f'),sep='')

#display quantity sold
print("Quantity Sold:",quantity_sold)

#display total discount offered
print("Total Discount Offered: $",format(discount_offered,'.2f'),sep='')

#display total profit
print("Total Profit: $",format(total_profit,'.2f'),sep='')

#display percentage profit
print("Percentage Profit: ",format(percentage_profit,'.2f'),"%",sep='')
