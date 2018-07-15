#Author: Jackson Ross jrr4557
#Homework 7 - Customer Analysis
#Due Date: 10/30/17
#Description: This program reads names from a file, stores them in dictionaries, keeps track of the number of purchases through the dictionaries, and stores the unique names in sets. It then can manipulate the sets to return specific customer analysis. 

#create constants for file names
MARKER_FILE_NAME = 'Markers.txt'
PAINT_FILE_NAME = 'Paints.txt'
CANVAS_FILE_NAME = 'Canvas.txt'
MARKER_OUTPUT_NAME = 'MarkerSummary.txt'
PAINT_OUTPUT_NAME = 'PaintSummary.txt'
CANVAS_OUTPUT_NAME = 'CanvasSummary.txt'

#create constants for menu options
ALL_ITEMS = 1
AT_LEAST_ONE = 2
MARKERS_ONLY = 3
PAINTS_ONLY = 4
CANVAS_ONLY = 5
ONE_TYPE_ONLY = 6
MOST_MARKERS = 7
MOST_PAINTS = 8
MOST_CANVAS = 9
EXIT = 10

#display menu function
def print_menu():
    print('CUSTOMER ANALYSIS')
    print('1. Which customers purchased markers, paints, and canvases?')
    print('2. Which customers purchased at least one of the products?')
    print('3. Which customers purchased only markers?')
    print('4. Which customers purchased only paints?')
    print('5. Which customers purchased only canvases?')
    print('6. Which customers purchased only one type of product?')
    print('7. Which customer purchased the most markers?')
    print('8. Which customer purchased the most paints?')
    print('9. Which customer purchased the most canvases?')
    print('10. Exit')
    print()

#pass function a file, set, and dict and have the function parse out the names and then keep a count of their purchases in the dictionary
def process_file(file,dict1,set1):
    
    #read first line and execute a while loop while the line is not blank
    first_line = file.readline().rstrip('\n')
    while first_line != '':
        
        #create a list by splitting the line at the #'s
        line_list = first_line.split('#')

        #create full name variable by combining first and last which have been given uniform capitalization
        first_name = line_list[0].lower().capitalize()
        last_name = line_list[1].lower().capitalize()
        full_name = first_name + ' ' + last_name

        #check to see if the name is already in the dictionary, if not add it, if so add 1 to the dictionary value
        if full_name not in dict1:
            dict1[full_name] = 1
        else:
            dict1[full_name] += 1

        #add full names to the set
        set1.add(full_name)

        #read a new first line for the while loop
        first_line = file.readline().rstrip('\n')
        
#function to find best customer
def get_best_customer(dict1):
    
    #create empty variables
    name = ''
    maximum = 0

    #compare each dict value to the maximum, updating it until the maximum has been found
    for key in dict1:
        if dict1[key] > maximum:
            maximum = dict1[key]
            name = key

    #return the name of the best customer
    return name
    
#function that gets a users menu option and validates input        
def get_user_choice():

    #display menu
    print_menu()

    #take user input
    choice = int(input("What would you like to do? "))

    #validate user input
    while choice < ALL_ITEMS or choice > EXIT:
        print()
        choice = int(input("Invalid menu option. Please select again: "))

    #return user choice
    return choice

#function that prints a set to the screen and a count at the end
def print_set(set1):

    #create empty count variable
    count = 0

    #for each name in the ser, print the name and increase counter
    for name in set1:
        print(name)
        count += 1

    #print count
    print('There are', count, 'customers')
    print()

#function to write output
def print_output(dict1,file):

    #for each full name, write the full name and the dictionary value to the screen
    for key in dict1:
        file.write(key + ' ' + str(dict1[key]) + '\n')

#define main function
def main():

    #create empty dicts and sets
    marker_dict = {}
    paint_dict = {}
    canvas_dict = {}

    marker_set = set()
    paint_set = set()
    canvas_set = set()

    #open input and output files
    marker_file = open(MARKER_FILE_NAME,'r')
    paints_file = open(PAINT_FILE_NAME,'r')
    canvas_file = open(CANVAS_FILE_NAME,'r')

    marker_output_file = open(MARKER_OUTPUT_NAME, 'w')
    paint_output_file = open(PAINT_OUTPUT_NAME, 'w')
    canvas_output_file = open(CANVAS_OUTPUT_NAME, 'w')

    #call process file function, passing it the set, dictionary, and file
    process_file(marker_file, marker_dict, marker_set)
    process_file(paints_file, paint_dict, paint_set)
    process_file(canvas_file, canvas_dict, canvas_set)

    #print output files, passing it the dict and output file
    print_output(marker_dict, marker_output_file)
    print_output(paint_dict, paint_output_file)
    print_output(canvas_dict, canvas_output_file)

    #get new menu choice
    menu = get_user_choice()
    print()

    #loop through the menu, comparing user choice to different options
    while menu != EXIT:
        if menu == ALL_ITEMS:
            set1 = marker_set.intersection(canvas_set)
            set2 = set1.intersection(paint_set)
            print('CUSTOMERS PURCHASED MARKERS, PAINTS, AND CANVAS')
            print_set(set2)

        elif menu == AT_LEAST_ONE:
            set1 = marker_set.union(paint_set)
            set2 = set1.union(canvas_set)
            print('CUSTOMERS PURCHASED AT LEAST ONE OF THE PRODUCTS')
            print_set(set2)

        elif menu == MARKERS_ONLY:
            set1 = marker_set.difference(paint_set)
            set2 = set1.difference(canvas_set)
            print('CUSTOMERS PURCHASED ONLY MARKERS')
            print_set(set2)

        elif menu == PAINTS_ONLY:
            set1 = paint_set.difference(marker_set)
            set2 = set1.difference(canvas_set)
            print('CUSTOMERS PURCHASED ONLY PAINTS')
            print_set(set2)

        elif menu == CANVAS_ONLY:
            set1 = canvas_set.difference(marker_set)
            set2 = set1.difference(paint_set)
            print('CUSTOMERS PURCHASED ONLY CANVAS')
            print_set(set2)

        elif menu == ONE_TYPE_ONLY:
            #set1 = marker_set.symmetric_difference(paint_set)
            #set2 = set1.symmetric_difference(canvas_set)
            set0 = set()
            set1 = canvas_set.difference(marker_set)
            set2 = set1.difference(paint_set)
            set3 = paint_set.difference(marker_set)
            set4 = set3.difference(canvas_set)
            set5 = marker_set.difference(paint_set)
            set6 = set5.difference(canvas_set)
            for val in set2:
                set0.add(val)
            for val in set4:
                set0.add(val)
            for val in set6:
                set0.add(val)
            print('CUSTOMERS WHO PURCHASED ONLY ONE TYPE OF PRODUCT')
            print_set(set0)
             
        elif menu == MOST_MARKERS:
            name = get_best_customer(marker_dict)
            print('WHO PURCHASED THE MOST MARKER SETS?')
            print(name, 'purchased', marker_dict[name], 'marker sets.')
            print()

        elif menu == MOST_PAINTS:
            name = get_best_customer(paint_dict)
            print('WHO PURCHASED THE MOST PAINT SETS?')
            print(name, 'purchased', paint_dict[name], 'paint sets.')
            print()

        elif menu == MOST_CANVAS:
            name = get_best_customer(canvas_dict)
            print('WHO PURCHASED THE MOST CANVASES?')
            print(name, 'purchased', canvas_dict[name], 'canvases.')
            print()
        
        menu = get_user_choice()
        print()

    #close input and output files
    marker_file.close()
    paints_file.close()
    canvas_file.close()

    marker_output_file.close()
    paint_output_file.close()
    canvas_output_file.close()

#call main function
main()
