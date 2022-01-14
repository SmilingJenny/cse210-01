#CSE201-01 Tic-tac-toe Game
#By: Jennifer Walton


#List, variable, or dictionary for game board
spaces = """
  1 2 3 
  4 5 6 
  7 8 9
  """
  
print (spaces)

turn = True
game = 0

while game != 9:
  if turn == True:
    x_num = input("X's turn, choose a number 1-9: ")
    if x_num not in spaces:
      print("Sorry, that number is taken. Choose again." + x_num)
    spaces = spaces.replace(x_num, "X")
    print(spaces)
    turn = False
    game += 1
  elif turn == False:
    o_num = input("O's turn, choose a number 1-9: ")
    spaces = spaces.replace(o_num, "O")
    print(spaces)
    turn = True
    game += 1  

#while if
'''while game != 9:
  if turn == True:
    x_num = input("X's turn, choose a number 1-9: ")
    spaces = spaces.replace(x_num, "X")
    print(spaces)
    turn = False
    game += 1
  elif turn == False:
    o_num = input("O's turn, choose a number 1-9: ")
    spaces = spaces.replace(o_num, "O")
    print(spaces)
    turn = True
    game += 1    
'''

#while
'''
while turn == True:
    x_num = input("X's turn, choose a number 1-9: ")
    spaces = spaces.replace(x_num, "X")
    print(spaces)
    turn = False

while turn == False:
    o_num = input("O's turn, choose a number 1-9: ")
    spaces = spaces.replace(o_num, "O")
    print(spaces)
    turn = True    
'''   
'''
def winner (
    if 
    1, 2, 3, or 4, 5, 6, or 7, 8, 9, or 1, 5, 9 or 3, 5, 7, or 1,2,7 or 2,5,8 or 3,6,9 == "X" 
    print ("Player X Wins!")
    #else if ditto but for O
    #else print ("Sorry, it's a draw. Want to play again?") restart progam 

  )
'''


