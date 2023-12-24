main_menu = ["Drinks", "Chips"] 
drinks_dict = {'Water':2, 'Mountain Dew':1.5, 'Juice':3} 
chips_dict = {'Pringles':7, 'Lays':0.5, 'Cheetos':1}
total = 0

def main_menu_func():
    print(main_menu)
    x = str(input("Select your preferred category. Type NONE to finish."))
    if( x == 'drinks'):
        print(drinks_func())
    elif ( x == 'chips'):
        print(chips_func())
    else:
        print("Please pick up your items and don't forget your change.")
        print(change_func())

def another_drink():
    x = (input("Are you looking to purchase another drink? Type YES or NO: "))
    if (x == 'YES'):
        print(drinks_func())
    else:
        print(main_menu_func())

def another_chips():
    x = (input("Are you looking to purchase another chips? Type YES or NO: "))
    if (x == 'YES'):
        print(chips_func())
    else:
        print(main_menu_func())

def drinks_func():
    global total  # Use the global keyword to modify the global variable

    print(drinks_dict)
    print("Type in the drink you want. If you do not want a drink type NONE:")
    drink = str(input())
    
    if drink == 'Water':
        drink_cost = 2
        total += drink_cost  # Add the cost to the total
        print(another_drink())
    elif drink == 'Mountain Dew':
        drink_cost = 1.5
        total += drink_cost
        print(another_drink())
    elif drink == 'Juice':
        drink_cost = 3
        total += drink_cost
        print(another_drink())
    elif drink == 'NONE':
        print(main_menu_func())
    else:
        print("Please enter a valid response")
        print(drinks_func())

def chips_func():
    global total

    print(chips_dict)
    print("Please type in the chips you want")
    chips = str(input())
    
    if chips == 'Pringles':
        chips_cost = 7
        total += chips_cost
        print(another_chips())
    elif chips == 'Lays':
        chips_cost = 0.5
        total += chips_cost
        print(another_chips())
    elif chips == 'Cheetos':
        chips_cost = 1
        total += chips_cost
        print(another_chips())
    else:
        print("The response you entered isn't valid. Try again.")
        print(chips_func())

def change_func():
        print("Thank you for buying Seans vending machine.")
        ## recalculate the overall cost
        change = coins - total
        print("You paid", coins, "and you bought with", str(total), ". Your change is: ", (change))


print('Welcome to Seans vending machine. Help yourself to our selection of snacks and drinks.')
coins = (float(input('Please enter your coins: ')))

coin_type = (str(input('Are your coins AEDs? Please type YES or NO: ')))
if (coin_type == "YES"): 
    print("You entered", str(coins), "Dirhams. Please select the category you want.")
    print(main_menu)
    print("Please type in the category you want:")
    category_selection = str(input())
    if(category_selection == 'Drinks'):
        print(drinks_func())
    elif(category_selection == 'Chips'):
        print(chips_func())
    else:
        print("Invalid response.")


#total = (drink_cost + chips_cost + candy_cost)

else:         
    print('We only accept AED.')