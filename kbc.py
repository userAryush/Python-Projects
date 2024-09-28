print("Welcome to Ko Banxa Crorepati!!!!!!!!!!!!!!")

def questions(qsn):
    money = 0
    level = [1000, 2000, 3000]
    correctans = ['b', 'b', 'a']

    for i in range(len(level)):
        question, options = list(qsn.items())[i]       
        #.items() method would return view object that displays a list of the dictionary's key-value tuple pairs.              
# ([("What is the capital of France?", "a) Berlin b) Paris"),
#   ("What is 2 + 2?", "a) 3 b) 4"),
#  ("Which is a fruit?", "a) Apple b) Carrot") ])  ----- ani tespaxi converting it to list to iterate by index
        
        print(f"---------Question for Rs{level[i]}--------")
        print(f"Question: {question}")
        print(f"Options: {options}")

        ans = input("Enter the correct answer (a, b): ").strip().lower()
        
        if ans == correctans[i]:
            print(f"You have won Rs{level[i]}")
            money += level[i]
            print("Your account:", money)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif ans not in ['a', 'b']:
            print("Invalid input!! Choose from the options.")
            break
        else:
            print("Incorrect answer")
            break
    return money

# Example usage:
qsn = {
    "What is the capital of France?": "a) Berlin b) Paris",
    "What is 2 + 2?": "a) 3 b) 4",
    "Which is a fruit?": "a) Apple b) Carrot"
}

take=questions(qsn)
print(f"Congratulations you are taking Rs{take} with you")
                    
                


