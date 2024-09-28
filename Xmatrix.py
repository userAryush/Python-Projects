#In this program player have to choose a box in 3X3 matrix and try to fill it in less move
def play_game():
    
    mat = [[1,1,1],
           [1,1,1],
           [1,1,1]]
    moves=0
    e=0
    while True:
        
        choose = int(input("Enter the cell(1-9)"))
        if choose>=1 and choose<=9:
            row = (choose-1)//3
            col = (choose-1)%3
            if mat[row][col]=="X":
                print("Already ocupied")
                moves+=1
            else:
                mat[row][col]="X"
                for i in mat:
                    print(f"|{i}|")
                moves+=1
            all_x = all(mat[i][j] == "X" for i in range(3) for j in range(3))
                
            if all_x:
                break
            
        else:
            print("Invalid input!!Chooose only between 1-9")
    print(f"Number of moves played:{moves}")
play_game()
