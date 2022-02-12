Project 5 : Essentials of Python Programming
Project: Developing ‘Rock, Paper and Scissors’ game using Python programming
Aim: Write a Python program to develop a Rock, Papers and Scissors game to be played against a computer.
##Winning Rules as follows :

                             ###Rock vs paper-> paper wins
                             ###Rock vs scissor-> Rock wins
                             ###paper vs scissor-> scissor wins.
#Import random
import random
#Now we select our choices and we use the if elif condition to set that. Also to we continue the game and quit the game we type it as q.Thus we quit from the game
input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
print()
i_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
  random_index = random.randint(0,2)
  cpu_choice = choices[random_index]

  my_choice = input("Rock, Paper, or Scissors? ").lower()
  while my_choice not in choices:
    my_choice = input("That is not a valid choice. Please try again: ").lower()
  
  print()
  print("My choice:", my_choice)
  print("Computer's choice:", cpu_choice)
  print()

  if my_choice == 'rock':
    if cpu_choice == 'rock':
      print("It's a tie!")
    elif cpu_choice == 'scissors':
      print("You win!")
      i_wins+=1
    elif cpu_choice == 'paper':
      print("You lose!")
      computer_wins+=1
  elif my_choice == 'paper':
    if cpu_choice == 'paper':
      print("It's a tie!")
    elif cpu_choice == 'rock':
      print("You win!")
      i_wins+=1
    elif cpu_choice == 'scissors':
      print("You lose!")
      computer_wins+=1
  elif my_choice == 'scissors':
    if cpu_choice == 'scissors':
      print("It's a tie!")
    elif cpu_choice == 'paper':
      print("You win!")
      i_wins+=1
    elif cpu_choice == 'rock':
      print("You lose!")
      computer_wins+=1

  print()
  print("You have "+str(i_wins)+" wins")
  print("The computer has "+str(computer_wins)+" wins")
  print()

  repeat = input("Play again? (Y/Q) ").lower()
  while repeat not in ['y', 'q']:
    repeat = input("That is not a valid choice. Please try again: ").lower()
  
  if repeat == 'q':
    break

  #print("\n----------------------------\n")

