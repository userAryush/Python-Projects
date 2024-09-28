import random
import string   # to grab every uppercase digit special character

def generate_password(min_length, numbers=True, special_characters=True): #num ra sp chai optional so
    letters = string.ascii_letters      #sab letter
    digits = string.digits      #all digits
    special = string.punctuation #all characters
    
    characters =letters
    if numbers:
        characters +=digits 
    if special_characters:
        characters +=special
        
    pwd = ""
    meets_criteria =False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number   #ya false aaayo vaneta tala etikei ni false huna paro so tala and
        if special_characters:
            meets_criteria = meets_criteria and has_special #both true then true
    return pwd
    

min_length = int(input("Enter the minimum length for password ")) 
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"  #y input garo vane true hunxa 
has_scpecial = input("Do you want to have special characters (y/n)? ").lower() == "y"  
pwd=generate_password(min_length, has_number, has_scpecial)
print(f"The generated password is {pwd}")
    
    