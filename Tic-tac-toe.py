#CSE201-01 Tic-tac-toe Game
#By: Jennifer Walton


def main():

  spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  x_turn = True
  turn_count = 0

  while turn_count != 9:
    
    print_board(spaces)

    if x_turn == True:
      x_num = input("X's turn, choose a number 1-9: ")

      if x_num not in spaces or x_num == "O" or x_num == "X":
        print("\nSorry, invalid move. Choose again.\n")
      elif x_num in spaces:
        spaces[spaces.index(x_num)] = "X"
        if winning("X", spaces):
          print("X Wins!")
          break
        x_turn = False
        turn_count += 1

    elif x_turn == False:
      o_num = input("O's turn, choose a number 1-9: ")

      if o_num not in spaces or o_num == "O" or o_num == "X":
        print("\nSorry, invalid move. Choose again.\n")
      elif o_num in spaces:
        spaces[spaces.index(o_num)] = "O"
        if winning("O", spaces):
          print("O Wins!")
          break
        x_turn = True
        turn_count += 1  

  # draw condition
  if turn_count == 9:
    print("Sorry, it's a draw.")

  play_again = input("\nWant to play again? Y/N ").upper()
  
  if play_again == "Y":
      print("\nGreat!")
      main()
  else:
      print("\nAlright, see ya.")

def print_board(spaces):
  print(f"""
  {spaces[0]} {spaces[1]} {spaces[2]}
  {spaces[3]} {spaces[4]} {spaces[5]}
  {spaces[6]} {spaces[7]} {spaces[8]}
  """)

def winning(player, spaces):
  # rows
  if spaces[0] == player and spaces[1] == player and spaces[2] == player:
    return True
  if spaces[3] == player and spaces[4] == player and spaces[5] == player:
    return True
  if spaces[6] == player and spaces[7] == player and spaces[8] == player:
    return True

  # columns
  if spaces[0] == player and spaces[3] == player and spaces[6] == player:
    return True
  if spaces[1] == player and spaces[4] == player and spaces[7] == player:
    return True
  if spaces[2] == player and spaces[5] == player and spaces[8] == player:
    return True

  # diagonals
  if spaces[0] == player and spaces[4] == player and spaces[8] == player:
    return True
  if spaces[2] == player and spaces[4] == player and spaces[6] == player:
    return True
  
  # it's a draw
  return False
    
# Starts the game
main()









