__author__ = "Yusuf Abouelwafa"

import load_data
import sort
import curve_fit
import histogram

base_attributes = ['strength', 'agility', 'stamina', 'personlaity', 'intelligence', 'luck', 'armor']

data_is_loaded = False
invalid_entry = True
program_running = True
will_have_health = True

while program_running:
    while invalid_entry:
        print('The available commands are:\n   L) oad Data\n   S) ort Data\n   C) urve Fit\n   H) istogram\n   E) xit\n')
        command = input('Please type your command: ')
        if command.lower() == 'l' or command.lower() == 's' or command.lower() == 'c' or command.lower() == 'h' or command.lower() == 'e':
            if data_is_loaded == False and command.lower() != 'l' and command.lower() != 'e':
                print('File not loaded\n')
            else: invalid_entry = False
        else:
            print('Invalid command\n')
    invalid_entry = True

    #LOAD DATA
    if command.lower() == 'l':
        file_name = input('Please enter the name of the file: ')
        attribute = input('Please enter the attribute to use as a filter: ')

        while attribute.lower() != 'luck' and attribute.lower() != 'strength' and attribute.lower() != 'weapon' and attribute.lower() != 'occupation' and attribute.lower() != 'all':
            attribute = input('Attribute invalid, please enter a valid attribute: ')

        if attribute.lower() != 'all': 
            if attribute.lower() == 'luck': 
                attribute_value = float(input('Please enter the value of the attribute: '))
            else:
                attribute_value = input('Please enter the value of the attribute: ')
                try:
                    attribute_value = int(attribute_value)
                except:
                    attribute_value = str(attribute_value)

        if attribute.lower() == 'strength'or attribute.lower() == 'luck':
            print('WARNING: Health will not be calculated')
            will_have_health = False
            if attribute.lower() == 'strength':
                loaded_data = load_data.load_data(file_name, (attribute, (attribute_value, attribute_value)))
            else:
                loaded_data = load_data.load_data(file_name, (attribute, attribute_value))
        elif attribute.lower() == 'all':
            loaded_data = load_data.calculate_health(load_data.load_data(file_name, (attribute, 0)))
            will_have_health = True
        else:
            loaded_data = load_data.calculate_health(load_data.load_data(file_name, (attribute, attribute_value)))
            will_have_health = True


        data_is_loaded = True
        print('Data Loaded\n')

    #SORT DATA
    elif command.lower() == 's':
        sorting_attribute = input("Please enter the attribute you want to use for sorting\n'Agility', 'Armor', 'Intelligence', 'Health': ")
        while sorting_attribute != 'Agility' and sorting_attribute != 'Armor' and sorting_attribute != 'Intelligence' and sorting_attribute != 'Health':
            sorting_attribute = input('Invalid Attribute, please enter one of the attributes listed: ')

        order = input('Ascending (A) or Descending (D) order: ')
        while order.lower() != 'a' and order.lower() != 'd':
            order = input('Order is not valid, please enter a valid order: ')

        sorted_data = sort.sort(loaded_data, order.upper(), sorting_attribute)
        display_data = input('Data Sorted. Do you want to display the data? (Y)es / (N)o: ')
        if display_data.lower() == 'y':
            print(sorted_data)
        elif display_data.lower() == 'n': 
            print('You selected not to display:')
    #CURVE FIT
    elif command.lower() == 'c':
        if will_have_health:
            bestfit_attribute = input('Please enter the attribute you want to use to find the best fit for Health: ')
            while bestfit_attribute.lower() not in base_attributes:
                bestfit_attribute = input('Invalide attribure, please enter a valid attribute: ')
            order_of_polynomial = int(input('Please enter the order of the polynomial to be fitted: '))
            print(curve_fit.curve_fit(loaded_data, bestfit_attribute, order_of_polynomial))
        else: print('Cannot find curve fit wihtout a HEALTH key')
    
    #HISTOGRAM
    elif command.lower() == 'h':
        plotting_attribute = input('Please enter the attribute you want to use for plotting: ')
        histogram.histogram(loaded_data, plotting_attribute)

    #QUIT
    elif command.lower() == 'e':
        program_running = False
        

        
