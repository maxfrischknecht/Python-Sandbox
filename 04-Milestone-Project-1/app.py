print("app is starting")

# enter 'X' or 'O'
# player1 = input("Please pick a marker 'X' or 'O' ")

# get position by number
# position = int(input('Please enter a number'))

# STEP 1: Function to draw a board
def display_board(board):
  # clear screen by 100 new lines
  # print('\n'*100)
  print(f"{board[1]} | {board[2]} | {board[3]}")
  print(f"{board[4]} | {board[5]} | {board[6]}")
  print(f"{board[7]} | {board[8]} | {board[9]}")

# STEP 2: Take user input
def player_input():
  # enter 'X' or 'O'
  player1 = input("Please pick a marker 'X' or 'O' ")
  while player1.lower() != "x" and player1.lower() != "o":
    player1 = input("Please pick a marker 'X' or 'O' ")
  else: 
    print(f"You chose {player1.upper()}! Let the battle begin!")

# STEP 3: Place the user input and draw a new board
def place_marker(board, marker, position):
    board[position] = marker

# STEP 4: Check of the there is a winner
def win_check(board, mark):
  if mark == board[1] and mark == board[2] and mark == board[3]:
    return True
  elif mark == board[4] and mark == board[5] and mark == board[6]:
    return True
  elif mark == board[7] and mark == board[8] and mark == board[9]:
    return True
  elif mark == board[1] and mark == board[4] and mark == board[7]:
    return True
  elif mark == board[2] and mark == board[5] and mark == board[8]:
    return True
  elif mark == board[3] and mark == board[6] and mark == board[9]:
    return True
  elif mark == board[1] and mark == board[5] and mark == board[9]:
    return True
  elif mark == board[3] and mark == board[5] and mark == board[7]:
    return True
  else:
    return False

# STEP 5: Randomly select who can start
from random import randrange
def choose_first():
  selected = randrange(2)
  if selected == 0:
    return "Player 1 goes first"
  else: 
    return "Player 2 goes first"

# STEP 6: Check if a space on the board is free
def space_check(board, position):
  if board[position] == 'X' or board[position] == 'O':
    return False
  else:
    return True

# STEP 7: Check if the board is full
def full_board_check(board):
  for place in board:
    if place != 'X' or place != 'O' or place != '#':
      return False
    else:
      return True

test_board = ['#','X','O','X','O','X','O','X','O','X']
# print(full_board_check(test_board))
# print(space_check(test_board, 0))
# print(choose_first())
# print(win_check(test_board, 'X'))
#  place_marker(test_board, 'X', 2)