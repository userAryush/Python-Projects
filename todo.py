# a program where users can add, remove, and view tasks in a to-do list.


def view(view_list):
    if not view_list:
        print("\nYour todo list is empty! Add something on your list now!")
    else:
        for i, todo in enumerate(view_list):
            print(f"{i+1}. {todo}")
         

def add(add_list):
    todo = input("Enter your tasks to be added: ")
    add_list.append(todo)
    print("New task added successfully!")

def remove(remove_list):
    view(remove_list)
    idx = int(input("Enter the index from above list to remove a task!"))
    remove_list.pop(idx-1)
    print("Task removed successfully!")
    

my_list =[]
while True:

    print("\nTODO LIST\n")
    print("1. View tasks\n2. Add tasks\n3. Remove tasks\n")
    
    user_choice = input("Enter your choice(1/2/3) or 'exit' to end : ")
    
    if user_choice == "exit":
        break
    
    elif user_choice =="1":
        view(my_list)
        
    elif user_choice == "2":
        add(my_list)
        
    elif user_choice == "3":
        remove(my_list)
        
    else:
        print("Wrong input! input should be 1/2/3/0")



