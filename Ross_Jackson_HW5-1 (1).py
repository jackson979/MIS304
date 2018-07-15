#Author: Jackson Ross jrr4557
#Homework 5 - Reading/Writing Employee Files
#Due Date: 10/16/17
#Description: This program reads an employee file containing names, pay rates, and hours worked of each week,
#               calculates average hours per week and total earned per employee, and writes this information to a file

#define constant for output file name
AVG_FILE = 'EmployeeAverages.txt'

#user input and validation for number of weeks worked
def weeks_validation():
    weeks = int(input('Enter number of weeks worked: '))
    while weeks <= 0:
        weeks = int(input('Invalid input. Please enter a positive value for weeks worked: '))
    return weeks

#calculate average hours worked per week
def avg_hours(hrs, wks):
    avg_hrs = hrs/wks
    return avg_hrs

#calculate weekly pay
def weekly_pay(hrs,rate):
    #take overtime into account
    if hrs > 40:
        pay = (40 * rate) + ((hrs - 40) * (1.5 * rate))
    else:
        pay = hrs * rate
    return pay

#print employee information to output file
def output_file(file_name,l_name,f_name,avg_hrs,tot_pay):
    file_name.write(l_name + ', ' + f_name + ' ' + str(avg_hrs) + ' $' + str(tot_pay) + '\n')

#define main function
def main():

    #create empty employee counter
    employee_count = 0

    #open files
    employee_doc = open('Employees.txt','r')
    averages_doc = open(AVG_FILE,'w')

    #call week input and validation function
    weeks_worked = weeks_validation()
    
    #begin reading input file
    empname = employee_doc.readline().rstrip('\n')
    
    #make sure there is another line to read
    while empname != '':

        #create empty total counters
        total_hours = 0
        total_pay = 0

        #increase employee counter
        employee_count += 1

        

        #read the lines for the first and last names and pay rate
        first_name = empname
        last_name = employee_doc.readline().rstrip('\n')
        pay_rate = float(employee_doc.readline())

        #create loop that only runs for the number of weeks specified
        for weeks in range(weeks_worked):
            #read # of hours from input file and increase total pay counter
            hrs = int(employee_doc.readline())
            total_hours += hrs
            
            #call weekly pay function, giving it total hours and weeks worked
            pay = weekly_pay(hrs,pay_rate)
            total_pay += pay
        #call average hours function, giving it hours and weeks worked, and formatting it
        average_hours = format(avg_hours(total_hours, weeks_worked),'.2f')

        #format total pay before writing
        total_pay = format(total_pay,',.2f')

        #call writing function, giving it the file name, first/last name, average hours, and total pay
        output_file(averages_doc,last_name,first_name,average_hours,total_pay)

        #start next itteration of the while loop if != ''
        empname = employee_doc.readline().rstrip('\n')

    #close files
    employee_doc.close()
    averages_doc.close()

    #print number of employees processed and the output file name
    print('# of Employees Processed:',employee_count)
    print('Output file name:',AVG_FILE)

#call main using try with exceptions for unknown input file location and mismatch in number of weeks entered and actual number of weeks worked
try:
    main()
except FileNotFoundError:
    print('Could not find Employee.txt in current directory.')
except ValueError:
    print('The number of weeks entered by user does not match the number of weeks indicated by the file.')
