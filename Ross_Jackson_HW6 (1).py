#Author: Jackson Ross jrr4557
#Homework 6 - Manipulating Lists
#Due Date: 10/22/2017
#Description: This programs reads emplyoee data, stores it in lists, and then
                #manipulates those lists to get summary information for each employee

#declare constants
INPUT_FILE_NAME = 'EmployeeData.txt'
OUTPUT_FILE_NAME = 'EmployeeSummaryData.txt'
LIFE_INSURANCE_RATE = .01
RATE_401K = .05
PPOI_COST = 1875
PPOF_COST = 3890

#define funcation that calculates 401K for each employee based on their salaries
def calc_401k(sal_list):
    #create empty list for use within the function and an index value
    new_list = []
    index = 0

    #for each salary, append the product of the salary and the 401K rate to the temporary list
    for sal in sal_list:
        new_list.append(int(sal) * RATE_401K)
        index += 1

    #return the temporary list so the main function can use the 401K list
    return new_list

#define function that calculates the cost of life insurance for each employee based on their decision (Y/N)
def calc_life_insurance(life_ins_list,sal_list):
    #create empty list for use within the function and an index value
    new_list = []
    index = 0

    #for each employee, determine whether they chose to get life insurance or not
    for choice in life_ins_list:
        #if they did decide to get life insurance, multiply their salary by the life insurance rate and store that value in the temporary list
        if choice == 'Y':
            new_list.append(int(sal_list[index]) * LIFE_INSURANCE_RATE)

        #otherwise, store a 0 in the list for that employee
        elif choice == 'N':
            new_list.append(0)

        #increase the index for the for loop
        index += 1

    #return the temporary list so the main function can use the life insurance cost list
    return new_list

#define function that calculates the cost of health insurance for each employee based on their decision (PPOI/PPOF/None)
def calc_health_insurance(health_ins_list):
    #create empty list for use within the function and an index value
    new_list = []
    index = 0

    #for each employee, determine whether what form of healthcare (if any) they chose
    for choice in health_ins_list:
        #if they chose PPOI, add the PPOI_COST to the list for that employee
        if choice == 'PPOI':
            new_list.append(PPOI_COST)

        #if they chose PPOF, add the PPOF_COST to the list for that employee
        elif choice == 'PPOF':
            new_list.append(PPOF_COST)

        #otherwise, store a 0 in the list for that employee
        elif choice == 'None':
            new_list.append(0)
            
        #increase the index for the for loop
        index += 1

    #return the temporary list so the main function can use the health insurance cost list
    return new_list

#define function that calculates the total of all items within a numerical list and returns the total
def calc_total(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

#define function that takes the sum of each employee's benefits (401K, life insurance, and health insurance)
def calc_total_benefits(list_401k,life_list,health_list):
    #create empty list for use within the function
    new_list = []

    #for each employee, add up their benefits and store it in the temporary list
    for index in range(len(list_401k)):
        total = float(list_401k[index] + life_list[index] + health_list[index])
        new_list.append(total)

    #return the temporary list so that the main function can use the total benefits list
    return new_list   

#define function that writes information to the output file
def write_output(name_list,sal_list,ben_list):
    #open output file in write mode
    summary_file = open(OUTPUT_FILE_NAME,'w')

    #for each name, write a line in the output file with their name, salary, and benefit contributions
    for index in range(len(name_list)):
        name = name_list[index]
        salary = sal_list[index]
        benefits = ben_list[index]
        summary_file.write(name + ' earns $' + str(format(salary,',.0f')) + ' and contributes $' + str(format(benefits,',.2f')) + ' towards benefits.' + '\n')

    #close the output file
    summary_file.close()

def main():
    #create employee counter
    employee_count = 0

    #create empty lists for modification within main()
    name_list = []
    salary_list = []
    life_insurance_list = []
    health_insurance_list = []

    #open input file in read mode
    employee_file = open(INPUT_FILE_NAME,'r')

    #read the first line of the input file
    first_line = employee_file.readline()

    #if the file is empty, notify the user and do not print any summary info
    if first_line == '':
        print('Input file is empty.')       
    #otherwise, execute a while loop that allows it to keep reading until it finds the end of the document ('first_line != '')
    else:
        while first_line != '':
            #increase employee counter
            employee_count += 1

            #read input file line by line, assigning each value to a specific slot in a specific list after stripping the new line at the end
            name_list.append(first_line.rstrip('\n'))
            salary_list.append(int(employee_file.readline().rstrip('\n')))
            life_insurance_list.append(employee_file.readline().rstrip('\n'))
            health_insurance_list.append(employee_file.readline().rstrip('\n'))

            #get a new 'first_line' for the while loop
            first_line = employee_file.readline()

        #call functions to calculate the individual benefits (401K, life insurance and health insurance)    
        list_401k = calc_401k(salary_list)
        life_insurance_cost_list = calc_life_insurance(life_insurance_list,salary_list)
        health_insurance_cost_list = calc_health_insurance(health_insurance_list)

        #call function to calculate the total benefits of each employee and pass it the list of 401K's, life insurance costs, and health insurance costs
        total_benefits_list = calc_total_benefits(list_401k,life_insurance_cost_list,health_insurance_cost_list)

        #calculate totals using the total function
        total_salary = calc_total(salary_list)
        total_benefits = calc_total(total_benefits_list)
        total_401k = calc_total(list_401k)
        total_life = calc_total(life_insurance_cost_list)
        total_health = calc_total(health_insurance_cost_list)

        #call function to write the outp[ut file after giving it the lists of names, salaries, and total benefits per employee
        write_output(name_list,salary_list,total_benefits_list)

        #print summary info
        print('Number of employees processed:', employee_count)
        print('Total salary paid by UT: $',format(total_salary,','))
        print('Total benefits paid by employees: $',format(total_benefits,',.0f'))
        print('Total 401K paid by employees: $',format(total_401k,',.0f'))
        print('Total life insurance paid by employees: $', format(total_life, ',.0f'))
        print('Total health insurance paid by emplpyees: $', format(total_health, ',.0f'))

    #close employee file
    employee_file.close()

#call main using try with exceptions for unknown input file location and mismatch in number of weeks entered and actual number of weeks worked
try:
    main()
except FileNotFoundError:
    print('Could not find EmployeeData.txt in current directory.')
