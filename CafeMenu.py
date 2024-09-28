# 1. Print Menu
# 2. Input order and check availability and add to the bill ask for quantity
# 3. Ask infinitly if you want to order and when it breaks print bill


def Menu():
    print()
    print("------------MENU------------")
    print("1. Momo -- Rs100 \n2. Burger -- Rs200\n3. Pizza -- Rs300")
    print("------------MENU------------")


def order(bill_amount):
    Menu()
    food = input("What would you like to have sir/mam? Please look at our menu and order ").capitalize()
    if food in menu:
        qty =int(input(f"Enter how many {food} would you like to have?"))

        ordered.append(food)
        quantity.append(qty)
        print("Order added")
        bill_amount +=menu[food]*qty

    else:
        print("The food is not available. Please order from the menu. ")
        
    return bill_amount, ordered, quantity



menu = {'Momo':100, 'Burger':200, 'Pizza':300}
ordered =[]
quantity =[]
bill_amount=0
bill=[]
while True:
    bill_amount, ordered_food, food_quantity = order(bill_amount)
    add = input("Do you want to order anythingelse?(y/n) ").lower()
    
    if add == 'n':
        print("--------------BILL--------------")
        print(f"FOOD    || Price*Quantity")
        print(" --------------------------")
        for f in range(len(ordered_food)):
            item = ordered_food[f]
            print(f"{item}    ||     {menu[item]}*{food_quantity[f]}")
        print(" -------------------------- ")
        print(f"Your total bill amount is {bill_amount}")
        print("--------------BILL--------------")
        break
        

    
    