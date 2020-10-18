# Vardit Lifshin ID 308011402

# I chose Freshmarket company.
# KPI I used are taken from:
# https://www.datapine.com/kpi-examples-and-templates/human-resources#overtime-hours
# https://www.datapine.com/kpi-examples-and-templates/fmcg
# https://www.datapine.com/kpi-examples-and-templates/retail#total-volume-of-sales

import datetime
import os
import matplotlib.pyplot as plt
import pickle
import random
import numpy as np
from matplotlib import ticker

# global constants
WHOLE = 100
CATEGORIES = ('Home Appliance & Housewares', 'Fruits & Vegetables', 'Dry Products', 'Beverages',
              'Refrigerator Products')


# This function contains the menu for the whole program
def main():
    try:
        print("Welcome to Freshmarket!")
        print("\nWhat would you like to do? ")
        print("To workers, press 1")
        print("To products, press 2")
        print("To statistics, press 3")
        print("To finish, press 0")
        choice1 = int(input())

        while choice1 >= 0:
            if choice1 > 3 or choice1 < 0:
                raise ValueError
            elif choice1 == 0:
                print("Good bye!")
                break
            elif choice1 == 1:
                print("\nWorkers:")
                print("To insert new worker/s, press 1")
                print("To get worker details, press 2")
                print("To update worker job, press 3")
                print("To update worker phone number, press 4")
                print("To update worker branch, press 5")
                print("To update worker end date of work, press 6")
                print("To delete worker, press 7")
                print("To get all workers details, press 8")
                print("To delete all workers, press 9")
                print("To go back to main menu, press 0")
                choiceW = int(input())
                while choiceW != 0:
                    try:
                        workers_file = open('dict_workers.dat', 'rb')
                        workers_dic = pickle.load(workers_file)
                        workers_file.close()
                    except OSError:
                        workers_file = open('dict_workers.dat', 'wb')
                    except EOFError:
                        workers_dic = {}
                    if choiceW<0 or choiceW>9:
                        raise ValueError()
                    if choiceW == 1:
                        add_new_worker(workers_dic)
                    else:
                        if choiceW <= 2 or choiceW <= 7:
                            print("Enter the worker ID: ")
                            id_n = str(input())
                            checkId = id_n.isnumeric()
                            if checkId is False:
                                raise ValueError()
                            found = check_if_id_exist(workers_dic, id_n)
                            if found is False:
                                raise ValueError()
                            else:
                                if choiceW == 2:
                                    get_worker_details(workers_dic, id_n)
                                elif choiceW == 3:
                                    update_worker_job(workers_dic, id_n)
                                elif choiceW == 4:
                                    update_worker_phone(workers_dic, id_n)
                                elif choiceW ==5:
                                    update_branch(workers_dic, id_n)
                                elif choiceW == 6:
                                    update_end_date(workers_dic, id_n)
                                elif choiceW == 7:
                                    delete_worker(workers_dic, id_n)
                        elif choiceW == 8:
                            get_all_workers(workers_dic)
                        elif choiceW == 9:
                            delete_all_workers(workers_dic)

                    output_file = open('dict_workers.dat', 'wb')
                    pickle.dump(workers_dic, output_file)
                    output_file.close()
                    print("\nWorkers:      What would you like to do next?")
                    print("To insert new worker/s, press 1")
                    print("To get worker details, press 2")
                    print("To update worker job, press 3")
                    print("To update worker phone number, press 4")
                    print("To update worker branch, press 5")
                    print("To update worker end date of work, press 6")
                    print("To delete worker, press 7")
                    print("To get all workers details, press 8")
                    print("To delete all workers, press 9")
                    print("To go back to main menu, press 0")
                    choiceW = int(input())

            elif choice1 == 2:
                print("\nProducts:")
                print("To insert new product, press 1")
                print("To get product details, press 2")
                print("To update number of units in stock, press 3")
                print("To update product price, press 4")
                print("To update number of sold products, press 5")
                print("To update number of returns, press 6")
                print("To delete product, press 7")
                print("To get all products details, press 8")
                print("To delete all products, press 9")
                print("To go back to main menu, press 0")
                choiceP = int(input())
                while choiceP !=0:
                    if choiceP == 1:
                        add_new_product()
                    elif 1 < choiceP <= 7:
                        code = str(input("Enter product bar code: "))
                        if choiceP == 2:
                            get_p_details(code)
                        if choiceP == 3:
                            update_units(code)
                        if choiceP == 4:
                            update_price(code)
                        if choiceP == 5:
                            update_sold(code)
                        if choiceP == 6:
                            update_return(code)
                        if choiceP == 7:
                            delete_product(code)
                    elif choiceP == 8:
                        get_all_p()
                    elif choiceP == 9:
                        delete_all_products()
                    else:
                        raise ValueError()
                    print("\nProducts:    What would you like to do next?")
                    print("To insert new product, press 1")
                    print("To get product details, press 2")
                    print("To update number of units in stock, press 3")
                    print("To update product price, press 4")
                    print("To update number of sold products, press 5")
                    print("To update number of returns, press 6")
                    print("To delete product, press 7")
                    print("To get all products details, press 8")
                    print("To delete all products, press 9")
                    print("To go back to main menu, press 0")
                    choiceP = int(input())

            elif choice1 == 3:
                print("\nStatistics:")
                print("To see the average time workers stay in the company, press 1")
                print("To see volume of sales per category, press 2")
                print("To see the rate of return, press 3")
                print("To go back to main menu, press 0")
                choiceS = int(input())
                while choiceS!=0:
                    count = 0
                    if choiceS == 1 and count==0:
                        workers_file = open('dict_workers.dat', 'rb')
                        workers_dic = pickle.load(workers_file)
                        workers_file.close()
                        show_avg_time_stay(workers_dic)
                    if choiceS == 2 and count==0:
                        get_num_sold_per_c()
                    if choiceS ==3 and count==0:
                        rate_of_return()
                    elif choiceS>3 or choiceS<0:
                        raise ValueError()
                    count+=1
                    print("\nStatistics:     What would you like to do next?")
                    print("To see the average time workers stay in the company, press 1")
                    print("To see volume of sales per category, press 2")
                    print("To see the rate of return, press 3")
                    print("To go back to main menu, press 0")
                    choiceS = int(input())

            print("\n\nWhat would you like to do next? ")
            print("To workers, press 1")
            print("To products, press 2")
            print("To statistics, press 3")
            print("To finish, press 0")
            choice1 = int(input())
            if choice1 < 0:
                raise ValueError

    except ValueError:
        print("Number of main choice must be a number between 0 to 3.")
        print("Number of choice in workers area must be a number between 0 to 8.")
        print("Number of choice in products area must be a number between 0 to 9.")
        print("Number of main choice must be a number between 0 to 3.")
        print("Worker id must contain numbers only. ")
        print("worker id not found. ")


# This function gets the workers dictionary, gets it's details from the user,
# and adds a new worker to the workers dictionary
def add_new_worker(workers_dic):
    try:
        num_guests = int(input('How many new workers would you like to insert? '))
        for x in range(0, num_guests):
            id_num = str(input('Enter the ID number of the ' + str(x + 1) + ' worker (at least 2 digits): '))
            l = len(id_num)
            checkId = id_num.isnumeric() and l >= 2
            if checkId is False or check_if_id_exist(workers_dic, id_num) is True:
                raise ValueError()
            else:
                workers_dic[id_num] = {}
                name = str(input('Enter name (letters only): '))
                checkName = all(x.isalpha() or x.isspace() for x in name)
                if checkName is False:
                    raise ValueError()
                else:
                    workers_dic[id_num]['name'] = name

                job = str(input('Enter job (letters only): '))
                checkJob = all(x.isalpha() or x.isspace() for x in job)
                if checkJob is False:
                    raise ValueError()
                else:
                    workers_dic[id_num]['job'] = job

                phone_num = str(input('Enter phone number: '))
                checkPhone = phone_num.isnumeric()
                if checkPhone is False:
                    raise ValueError()
                else:
                    workers_dic[id_num]['phone'] = phone_num

                branch = str(input('Enter branch (letters only): '))
                checkBranch = all(x.isalpha() or x.isspace() for x in branch)
                if checkBranch is False:
                    raise ValueError()
                else:
                    workers_dic[id_num]['branch'] = branch

                date_entry = input('Enter the date the worker started working in YYYY-MM-DD format ')
                year, month, day = map(int, date_entry.split('-'))
                date_start = datetime.date(year, month, day)
                workers_dic[id_num]['start date'] = date_start

                date_entry = '0001-01-01'
                year, month, day = map(int, date_entry.split('-'))
                date_end = datetime.date(year, month, day)
                workers_dic[id_num]['end date'] = date_end

                workers_dic[id_num]['password'] = create_password(id_num)

        print("The new worker\s was\were added to the workers file")
    except IOError:
        print("An error occurred trying to get the input")
    except ValueError:
        print("The type of input is illegal")
        print("The id must contain numbers only. ")
        print("The id number can be used only once. ")
    except:
        print("An error occurred.  ")


# This function gets the workers dictionary and the worker id, checks if the id exist in the dictionary and returns
# True if the id exist and False if not.
def check_if_id_exist(workers_dic, id_num):
    try:
        found = False
        for id in workers_dic.keys():
            if id == id_num:
                found = True
        return found
    except:
        print("An error occurred.")


# This function gets the workers dictionary and the worker id, and updates the worker job to the dictionary
def update_worker_job(workers_dic, id_num):
    try:
        job = str(input('Please insert the new job: '))
        checkJob = job.isalpha()
        if checkJob is False:
            raise ValueError()
        else:
            workers_dic[id_num]['job'] = job

        print("The new job for the worker was updated. ")

    except ValueError:
        print("The job must contain letters only. ")


# This function gets the workers dictionary and the worker id, and updates the worker phone to the dictionary
def update_worker_phone(workers_dic, id_num):
    try:
        phone_num = str(input('Please insert the new phone number: '))
        checkP = phone_num.isnumeric()
        if checkP is False:
            raise ValueError()
        else:
            workers_dic[id_num]['phone'] = phone_num

        print("The new phone number for the worker was updated. ")

    except ValueError:
        print("The phone number must contain numbers only. ")


# This function gets the workers dictionary and the worker id, and updates the worker branch to the dictionary
def update_branch(workers_dic, id_num):
    try:
        branch = str(input('Enter branch (letters only): '))
        checkBranch = all(x.isalpha() or x.isspace() for x in branch)
        if checkBranch is False:
            raise ValueError()
        else:
            workers_dic[id_num]['branch'] = branch
        print("The new branch for the worker was updated. ")
    except ValueError():
        print("The branch must contain letters and spaces only. ")


# This function gets the workers dictionary and the worker id, and updates the date the worker left the company
def update_end_date(workers_dic, id_num):
    try:
        date_entry = input('Enter the date the worker stopped working in YYYY-MM-DD format ')
        year, month, day = map(int, date_entry.split('-'))
        date_end = datetime.date(year, month, day)
        if (date_end-workers_dic[id_num]['start date']).days<0:
            raise ValueError
        else:
            workers_dic[id_num]['end date'] = date_end
            print("The end date was updated. ")
    except ValueError:
        print("End date must be late than start date. ")
    except:
        print("An error occurred trying to update end of working date. ")

# This function gets the workers dictionary, and prints the worker details, as they were saved
# in the dictionary
def get_all_workers(workers_dic):
    try:
        for id, info in workers_dic.items():
            print("\nWorker ID: ", id, ",", end=" ")
            for key in info:
                if key == "password":
                    print(key, ":", info[key])
                else:
                    print(key, ":", info[key], ",", end=" ")
            print("")
    except:
        print("Something went wrong. ")


# This function gets the workers dictionary and the worker id, and prints all workers details, as they were saved
# in the dictionary
def get_worker_details(workers_dic, id_num):
    try:
        dicti=workers_dic[id_num]
        print("Worker id: ", id_num, ",", end=" ")
        for key in dicti.items():
            if key[0] == 'password':
                print(key[0], ":", key[1])
            else:
                print(key[0], ":", key[1], ",", end=" ")
        print("")

    except:
        print("Something went wrong. ")


# This function gets the workers dictionary and the worker id, and deletes the worker from the dictionary
def delete_worker(workers_dic, id_num):
    try:
        del workers_dic[id_num]
        print("The worker was deleted. ")

    except ValueError:
        print("The phone number must contain numbers only. ")


# This function gets the workers dictionary, and deletes all workers from the dictionary.
def delete_all_workers(workers_dic):
    try:
        workers_dic.clear()
        print("All workers were deleted. ")
    except:
        print("Something went wrong. ")


# This function creates a password for the worker
def create_password(id_num):
    try:
        d12 = str(id_num)[:2]  # Takes the 2 first digits of the id
        d3 = str(random.randint(0, 9))  # Randomly choose a digit
        d4 = str(random.randint(0, 9))  # Randomly choose another digit
        d5 = str(random.randint(0, 9))  # Randomly choose another digit
        password = d12 + d3 + d4 + d5  # Create the password
        print('The worker password is: ' + password)
        return password

    except:
        print('Illegal password.')


# This function calculates the average time workers stay in the company, print it, and show in a bar plot
def show_avg_time_stay(workers_dic):
    try:
        # Counts the number of workers that left the company:
        years_of_end ={}

        for id, info in workers_dic.items():
            for key in info:
                if key == "end date":
                    end = info[key]
                elif key =="start date":
                    start = info[key]
            working_time_in_years = end.year - start.year
            if working_time_in_years>=0:
                if end.month < start.month or (end.month == start.month and end.day < start.day):
                    working_time_in_years -= 1
                if working_time_in_years in years_of_end.keys():
                    years_of_end[working_time_in_years] += 1
                else:
                    years_of_end[working_time_in_years]=1

        # Calculates the percentage of workers who left on each year
        sum_of_left=0  # sums the number of workers that left the company
        years_at_company = []  # Saves the years when the workers left
        perc = []  # Saves the percentage of leaving for each year.
        total_count_years=0
        for id, info in sorted(years_of_end.items()):  # Sorts the key from low to high
            sum_of_left += years_of_end[id]
            years_at_company.append(id)
            total_count_years+=id*info

        for id, info in sorted(years_of_end.items()):
            perc.append(info*WHOLE/sum_of_left)
            years_of_end[id] = id * info / sum_of_left

        avg_working_time = total_count_years/sum_of_left

        print("The average time workers left the company is: ", avg_working_time, " years")
        x=0
        for i in perc:
            print(i, "% of workers who left worked ", years_at_company[x], " year/s at the company.")
            x+=1

        fig, ax = plt.subplots()
        d = np.zeros(len(perc))
        a = plt.subplot2grid((1, 1), (0, 0))
        a.fill_between(years_at_company, perc, where=perc >= d, interpolate=True, color='lightskyblue')
        plt.title('Time to quit job by years', fontsize=14, color='blue', fontweight='bold')
        plt.xlabel('Years at company', fontsize=10, color='blue')
        plt.ylabel('Notices/Rate (%)', fontsize=10, color='blue')
        plt.grid(False)
        plt.plot(years_at_company, perc, marker='.', lw=1, color='black')
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=len(perc)))
        plt.show()

    except:
        print("something went wrong. ")


#
# Products
# This function shows the user all the categories, and user choose the category, and the function returns his choice.
def categories_menu():
    try:
        print('Choose the product category: ')
        c = 1
        for i in CATEGORIES:
            print('For', i, '- enter ', c)
            c += 1
        choice = int(input())
        if choice < 1 or choice > len(CATEGORIES):
            raise ValueError()
        return choice
    except ValueError:
        print('Your choice must be a number between 1 to ', len(CATEGORIES))

# This function gets from the user all product details and adds new product to the products file
def add_new_product():
    try:
        products_file = open('products_file.txt', 'a')
        filesize = os.path.getsize("products_file.txt")
        if filesize == 0:
            lst = ('bar_code', 'category', 'brand', 'name', 'units', 'price', 'sold')
            products_file.write(str(lst) + '\n')
        n = int(input('Enter number of products to insert : '))
        for i in range(0, n):
            print('product no. ', (i + 1), ' :\n')

            p_bar_code = str(input('Enter product bar code for the product : '))
            checkB = p_bar_code.isnumeric()
            if checkB is False or int(p_bar_code) < 0:
                raise ValueError()
            if check_code(p_bar_code):  # if the bar code is already used
                raise ValueError()

            p_category = categories_menu()  # Insert category

            p_brand = str(input('Enter product brand (letters only): '))
            checkBrand = all(x.isalpha() or x.isspace() for x in p_brand)
            if checkBrand is False:
                raise ValueError()

            p_name = str(input('Enter product name (letters only): '))
            checkName = all(x.isalpha() or x.isspace() for x in p_name)
            if checkName is False:
                raise ValueError()

            p_units = str(input('Enter number of units : '))
            checkUnits = p_units.isnumeric()
            if checkUnits is False or int(p_units) < 0:
                raise ValueError()
            p_units = int(p_units)

            p_price = float(input('Enter price : '))
            if p_price < 0:
                raise ValueError()

            p_num_sold = 0  # Saves the number of units that were sold from the product
            p_num_return=0  # Saves the number of units that were returned to the company from customers

            lst = [p_bar_code, p_category, p_brand, p_name, p_units, p_price, p_num_sold, p_num_return]

            for item in lst:
                products_file.write("%s\n" % item)

            print("The new product was added to the products file")

        products_file.close()
    except IOError:
        print("An error occurred trying to load\write to the file")
    except ValueError:
        print("The type of input is illegal. numbers must be o or bigger")
        print("The bar code is illegal or already in use. numbers must be o or bigger")
    except:
        print("An error occurred while insertions of input")


# This function gets product bar code,
# checks if the product bar code already exist in the products file, and return True is found and False if not.
def check_code(p_bar_code):
    try:
        products_file = open('products_file.txt', 'r')
        # Reads the title
        tmp = str(products_file.readline())
        # Reads the first bar code
        tmp = str(products_file.readline())
        while tmp != '':
            t = tmp.rstrip('\n')
            if t == p_bar_code:
                return True
            tmp = str(products_file.readline())  # Reads the category
            tmp = str(products_file.readline())  # Reads brand
            tmp = str(products_file.readline())  # Reads the name
            tmp = str(products_file.readline())  # Reads the units
            tmp = str(products_file.readline())  # Reads the price
            tmp = str(products_file.readline())  # Reads sold
            tmp = str(products_file.readline())  # Reads return
            tmp = str(products_file.readline())  # Reads the next barcode

        products_file.close()
        return False
    except:
        print("An error occurred.  ")


# This function gets product bar code and updates the number of units in stock for the product
def update_units(p_bar_code):
    try:
        found = False
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())
        # read the bar code
        code = (products_file.readline())
        while code != '':
            code = code.rstrip('\n')
            if code != p_bar_code:
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                for i in range(0, 7):  # Inserts all product details
                    temp_file.write(products_file.readline())

            elif code == p_bar_code:
                found = True
                u = int(input('Enter new number of units: '))
                # Checks if the number of units is legal
                if u < 0:
                    raise ValueError
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                # inserts category
                temp_file.write(products_file.readline())
                # inserts brand
                temp_file.write(products_file.readline())
                # inserts name
                temp_file.write(products_file.readline())
                # inserts units
                newline = (products_file.readline())
                newline = newline.rstrip('\n')
                newline.replace(str(code), '')
                temp_file.write(str(u) + '\n')
                # inserts price
                temp_file.write(products_file.readline())
                # inserts sold
                temp_file.write(products_file.readline())
                # inserts return
                temp_file.write(products_file.readline())

            # Reads the next bar code
            code = products_file.readline()

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        if found:
            print('The file has been updated, and the number of units was updated')
        else:
            print('The product was not found in the file')

    except ValueError:
        print("The number of units must be a number bigger or equals to 0")


# This functions gets the product bar code and prints the product details
def get_p_details(p_bar_code):
    foundP = False
    products_file = open('products_file.txt', 'r')
    # read the title
    code = (products_file.readline())
    # reads the bar code
    code = (products_file.readline())

    while code != '':
        if foundP is False:
            code = code.rstrip('\n')
            cat = products_file.readline()  # reads category
            b = products_file.readline()  # reads brand
            n = products_file.readline()  # reads name
            u = products_file.readline()  # reads units
            p = products_file.readline()  # reads price
            so = products_file.readline()  # reads sold
            r = products_file.readline()  # reads return

            if code == p_bar_code:
                foundP = True
                s = 'Product bar code: ' + str(p_bar_code) + '\ndetails: \n' \
                    + 'Category: ' + str(cat) + 'Brand: ' + b + 'Name: ' + n + 'Units: ' + u + 'Price: ' + p + \
                    'Sold: ' + so + 'Returns: '+ r
                print(s)

            code = products_file.readline()  # reads the next bar code

        else:
            break

    products_file.close()
    if foundP is False:
        print('The product was not found in the file')


# This function gets the product bar code and updates the product price
def update_price(p_bar_code):
    try:
        found = False
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())
        # read the bar code
        code = (products_file.readline())
        while code != '':
            code = code.rstrip('\n')
            if code != p_bar_code:
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                for i in range(0, 7):  # Inserts all product details
                    temp_file.write(products_file.readline())

            elif code == p_bar_code:
                found = True
                p = float(input('Enter new price: '))
                # Checks if the price is legal
                if p < 0:
                    raise ValueError
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                # inserts category
                temp_file.write(products_file.readline())
                # inserts brand
                temp_file.write(products_file.readline())
                # inserts name
                temp_file.write(products_file.readline())
                # inserts units
                temp_file.write(products_file.readline())
                # inserts price
                newline = (products_file.readline())
                newline = newline.rstrip('\n')
                newline.replace(str(code), '')
                temp_file.write(str(p) + '\n')

                # inserts sold
                temp_file.write(products_file.readline())
                # inserts returns
                temp_file.write(products_file.readline())

            # Reads the next bar code
            code = products_file.readline()

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        if found:
            print('The file has been updated, and the price was updated')
        else:
            print('The product was not found in the file')

    except ValueError:
        print("The price must be a number bigger or equals to 0")


# This function prints all the products details
def get_all_p():
    products_file = open('products_file.txt', 'r')
    # reads the title
    code = (products_file.readline())
    # reads the bar code
    code = (products_file.readline())

    while code != '':
        code = code.rstrip('\n')
        get_p_details(code)

        for i in range(0, 8):
            code = products_file.readline()

    products_file.close()


# This function gets a product bar code and updates the number of units sold from this product
def update_sold(p_bar_code):
    try:
        found = False
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())
        # read the bar code
        code = (products_file.readline())
        while code != '':
            code = code.rstrip('\n')
            if code != p_bar_code:
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                for i in range(0, 7):  # Inserts all product details
                    temp_file.write(products_file.readline())

            elif code == p_bar_code:
                found = True
                s = int(input('Enter new number of sold units: '))
                # Checks if the number is legal
                if s < 0:
                    raise ValueError
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                # inserts category
                temp_file.write(products_file.readline())
                # inserts brand
                temp_file.write(products_file.readline())
                # inserts name
                temp_file.write(products_file.readline())
                # inserts units
                temp_file.write(products_file.readline())
                # inserts price
                temp_file.write(products_file.readline())
                # inserts sold
                newline = (products_file.readline())
                newline = newline.rstrip('\n')
                newline.replace(str(code), '')
                temp_file.write(str(s) + '\n')
                # inserts returns
                temp_file.write(products_file.readline())

            # Reads the next bar code
            code = products_file.readline()

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        if found:
            print('The file has been updated, and the number of sold units was updated')
        else:
            print('The product was not found in the file')

    except ValueError:
        print("The number must be bigger or equals to 0")


# This function gets a product bar code and updates the number of units that customers returned from this product
def update_return(p_bar_code):
    try:
        found = False
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())
        # read the bar code
        code = (products_file.readline())
        while code != '':
            code = code.rstrip('\n')
            if code != p_bar_code:
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                for i in range(0, 7):  # Inserts all product details
                    temp_file.write(products_file.readline())

            elif code == p_bar_code:
                found = True
                ret = int(input('Enter new number of units returned: '))
                # Checks if the number is legal
                if ret < 0:
                    raise ValueError
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                # inserts category
                temp_file.write(products_file.readline())
                # inserts brand
                temp_file.write(products_file.readline())
                # inserts name
                temp_file.write(products_file.readline())
                # inserts units
                temp_file.write(products_file.readline())
                # inserts price
                temp_file.write(products_file.readline())
                # inserts sold
                sold = int(products_file.readline().rstrip('\n'))
                s= str(sold)+'\n'
                temp_file.write(s)
                if ret>sold:
                    raise ValueError
                else:
                    # inserts returns
                    newline = (products_file.readline())
                    newline = newline.rstrip('\n')
                    newline.replace(str(code), '')
                    temp_file.write(str(ret) + '\n')

            # Reads the next bar code
            code = products_file.readline()

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        if found:
            print('The file has been updated, and the number of returned units was updated')
        else:
            print('The product was not found in the file')

    except ValueError:
        print("The number must be bigger or equals to 0, and lower from the number of sold products.")


# This function gets product bar code and delete it with all its details from the products file
def delete_product(p_bar_code):
    try:
        found = False
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())
        # read the bar code
        code = (products_file.readline())
        while code != '':
            code = code.rstrip('\n')
            if code != p_bar_code:
                # inserts bar code
                output = str(code) + '\n'
                temp_file.write(output)
                for i in range(0, 7):  # Inserts all product details
                    temp_file.write(products_file.readline())

            elif code == p_bar_code:
                found = True
                # read category
                tmp = products_file.readline()
                # read brand
                tmp = products_file.readline()
                # read name
                tmp = products_file.readline()
                # read units
                tmp = products_file.readline()
                # read price
                tmp = products_file.readline()
                # read sold
                tmp = products_file.readline()
                # read returns
                tmp = products_file.readline()

            # Reads the next bar code
            code = products_file.readline()

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        if found:
            print('The file has been updated, and the product was deleted')
        else:
            print('The product was not found in the file')

    except:
        print("An error occurred.")


# This function deletes all products from the products file.
def delete_all_products():
    try:
        products_file = open('products_file.txt', 'r')
        temp_file = open('temp.txt', 'w')
        # read the title
        temp_file.write(products_file.readline())

        products_file.close()
        temp_file.close()
        # remove the original file
        os.remove('products_file.txt')
        # rename temporary file
        os.rename('temp.txt', 'products_file.txt')

        print('The file has been updated, and the product was deleted')

    except:
        print("An error occurred.")


# This function calculates the income from sales per category
def get_num_sold_per_c():
    # Counts number of sold products in each category
    c1 = c2 = c3 = c4 = c5 = 0
    # Sums the money earned from sales in each category
    m1 = m2 = m3 = m4 = m5 = 0

    products_file = open('products_file.txt', 'r')
    # reads the title
    code = (products_file.readline())
    # reads the bar code
    code = (products_file.readline())

    while code != '':
        cat = products_file.readline()  # reads category
        cat = int(cat.rstrip('\n'))
        b = products_file.readline()  # reads brand
        n = products_file.readline()  # reads name
        u = products_file.readline()  # reads units
        p = float(products_file.readline())  # reads price
        so = int(products_file.readline())  # reads sold
        r = int(products_file.readline())  # reads returns

        if cat == 1:
            c1 = c1 + so
            m1 = m1 + (so * p)
        if cat == 2:
            c2 = c2 + so
            m2 = m2 + (so * p)
        if cat == 3:
            c3 = c3 + so
            m3 = m3 + (so * p)
        if cat == 4:
            c4 = c4 + so
            m4 = m4 + (so * p)
        if cat == 5:
            c5 = c5 + so
            m5 = m5 + (so * p)

        code = products_file.readline()  # reads the next bar code

    objects = list(CATEGORIES)

    print('Enter company target sale on each category: ')
    target = []
    for i in objects:
        x = float(input('Category- '+ i+ ' : '))
        target.append(x)

    for i in objects:
        print("The income from category ", i , " is: ", )
        if i == 'Home Appliance & Housewares':
            print(m1, ". The sales target: ", target[0])
            if target[0]<m1:
                print("Target achieved!")
            elif target[0]>m1:
                print("Target not achieved. ")
            elif target[0] == m1:
                print("Sales are equal to target. ")
        if i == 'Fruits & Vegetables':
            print(m2, ". The sales target: ", target[1])
            if target[1] < m2:
                print("Target achieved!")
            elif target[1] > m2:
                print("Target not achieved. ")
            elif target[1] == m2:
                print("Sales are equal to target. ")
        if i == 'Dry Products':
            print(m3, ". The sales target: ", target[2])
            if target[2] < m3:
                print("Target achieved!")
            elif target[2] > m3:
                print("Target not achieved. ")
            elif target[2] == m3:
                print("Sales are equal to target. ")
        if i == 'Beverages':
            print(m4, ". The sales target: ", target[3])
            if target[3] < m4:
                print("Target achieved!")
            elif target[3] > m4:
                print("Target not achieved. ")
            elif target[3] == m4:
                print("Sales are equal to target. ")
        if i == 'Refrigerator Products':
            print(m5, ". The sales target: ", target[4])
            if target[4] < m5:
                print("Target achieved!")
            elif target[4] > m5:
                print("Target not achieved. ")
            elif target[4] == m5:
                print("Sales are equal to target. ")

    fig, ax = plt.subplots()
    plt.title('Sales Volume And Margin by Product Category', fontsize=15, color='blue', fontweight='bold')
    plt.xlabel('\nCategory',fontsize=10, color='blue')
    plt.ylabel('Income (ILS)', fontsize=10, color='blue')
    y_pos = np.arange(len(objects))
    performance = [m1, m2, m3, m4, m5]
    plt.bar(y_pos, performance, align='center', alpha=1, color='lightpink')
    plt.xticks(y_pos, objects, rotation=45, fontsize=9, horizontalalignment='right')
    plt.plot(objects, target, label='Target', color='red', marker='o')
    leg = ax.legend()

    plt.grid(False)
    plt.autoscale()
    plt.show()
    products_file.close()

# This function calculates the rate of returned products from each category, and shows it in a bar plot.
def rate_of_return():
    # Sum of products sold from each category
    s1= s2= s3= s4= s5=0
    # Sum of products returned from each category
    r1= r2= r3= r4= r5=0

    products_file = open('products_file.txt', 'r')
    # reads the title
    code = (products_file.readline())
    # reads the bar code
    code = (products_file.readline())

    while code != '':
        cat = products_file.readline()  # reads category
        cat = int(cat.rstrip('\n'))
        b = products_file.readline()  # reads brand
        n = products_file.readline()  # reads name
        u = products_file.readline()  # reads units
        p = float(products_file.readline())  # reads price
        so = int(products_file.readline())  # reads sold
        r = int(products_file.readline())  # reads returns

        if cat == 1:
            s1 +=so
            r1 += r
        if cat == 2:
            s2 += so
            r2 += r
        if cat == 3:
            s3 += so
            r3 += r
        if cat == 4:
            s4 += so
            r4 += r
        if cat == 5:
            s5 += so
            r5 += r

        code = products_file.readline()  # reads the next bar code

    # Percentage of returns from each category
    p1 = "{:.2f}".format(r1 * WHOLE / s1)
    p2 = "{:.2f}".format(r2 * WHOLE / s2)
    p3 = "{:.2f}".format(r3 * WHOLE / s3)
    p4 = "{:.2f}".format(r4 * WHOLE / s4)
    p5 = "{:.2f}".format(r5 * WHOLE / s5)

    x = ('Home Appliance & Housewares', 'Fruits & Vegetables', 'Dry Products', 'Beverages',
         'Refrigerator Products')
    print("The rate of return from category: ")
    print(x[0], " is: ", p1, "%")
    print(x[1], " is: ", p2, "%")
    print(x[2], " is: ", p3, "%")
    print(x[3], " is: ", p4, "%")
    print(x[4], " is: ", p5, "%")

    y = [float(p1), float(p2), float(p3), float(p4), float(p5)]
    x_pos = [i for i, _ in enumerate(x)]
    fig, ax = plt.subplots()
    rects1 = ax.bar(x_pos, y, color='b')
    for rect in rects1:
        height = float(rect.get_height())
        ax.text(rect.get_x() + rect.get_width() / 2., height+0.1,
                "{:.2f}".format(height)+'%', ha='center', va='bottom', fontsize=8)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, align='center', alpha=1, color='mediumslateblue')
    plt.xlabel('\nCategory', fontsize=10, color='dodgerblue')
    plt.ylabel('Rate of return (%)', fontsize=10, color='dodgerblue')
    plt.xticks(y_pos, x, rotation=45, fontsize=9, horizontalalignment='right')
    plt.title('Return Rate by Product Category', fontsize=15, color='dodgerblue', fontweight='bold')
    plt.show()
    products_file.close()

main()
input()
