users = {'aryush':1234, 'rojan':3030, 'ram':4040}
balance = {'aryush':500000000, 'rojan':1000000, 'ram':8000}

def login(a,b):
    
    if a in users and b == users[a]:
        print("Login successful!!")
        return True
    
    print("Login failed.Try again")
    main()
         
    
def main():

    username = input("Username: ")
    try:
        pin = int(input("Pin: "))
    except ValueError:
        print("Enter number only")
    log = login(username, pin)
    if log == True:
        user_choice=int(input('1. Show Balance\n2.Withdraw balance\nChoose option 1/2 '))
        if user_choice == 1:
            print(f"Your current balance is {balance[username]}")
        elif user_choice == 2:
            try:
                amount = int(input("Enter your amount to withdraw "))
            except ValueError:
                print("Enter number only")
                
            if amount<500:
                print("Amount less than 500 cannot be withdrawn")
                
            elif amount<= balance[username]:
                balance[username]-=amount
                print(f"Rs {amount} withdrawn successfullly. {username.capitalize()} current balance is {balance[username]}\nThankyou for using Aryush Bank ATM")
            else:
                print("Insufficient balance!!")
        
    
    


print("Welcome to login page of Aryush Bank ATM! " )
card = input("Please insert your card (write 'card'): ").lower()

if card == 'card':
    main()
else:
    print("No card inserted. Please try again.")