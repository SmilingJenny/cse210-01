#CSE201-01 Tic-tac-toe Game
#By: Jennifer Walton


#List, variable, or dictionary for game board
# def winner(player):
#   if "X X X" or """
#   X
#   X
#   X""" :
#     print("X Wins!")
    
#   #1, 2, 3, or 4, 5, 6, or 7, 8, 9, or 1, 5, 9 or 3, 5, 7, or 1,2,7 or 2,5,8 or 3,6,9 == "X" 
#   print ("Player X Wins!")
#   #else if ditto but for O
#   #else print ("Sorry, it's a draw. Want to play again?") restart progam 
  
#   return

spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board(spaces):
  print(f"""
  {spaces[0]} {spaces[1]} {spaces[2]}
  {spaces[3]} {spaces[4]} {spaces[5]}
  {spaces[6]} {spaces[7]} {spaces[8]}
  """)

 
print_board(spaces)

x_turn = True
turn_count = 0

while turn_count != 9:
  if x_turn == True:
    x_num = input("X's turn, choose a number 1-9: ")

    if x_num not in spaces:
      print("\nSorry, that number is taken. Choose again.\n")
      print_board(spaces)
    elif x_num in spaces:
      spaces[spaces.index(x_num)] = "X"
      print_board(spaces)
      x_turn = False
      turn_count += 1

  elif x_turn == False:
    o_num = input("O's turn, choose a number 1-9: ")

    if o_num not in spaces:
      print("\nSorry, that number is taken. Choose again.\n")
      print_board(spaces)
    elif o_num in spaces:
      spaces[spaces.index(o_num)] = "O"
      print_board(spaces)
      x_turn = True
      turn_count += 1  


