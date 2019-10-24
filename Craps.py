#Tyler Vasquez
#Craps
#Oct 24, 2019

import random


def create():
   bank = int(input("How much would you like to enter into the bank?: "))
   return bank


def roll():
   dice = random.randint(1,6) + random.randint(1,6)
   return dice


def play_game():
   bank = create()
   bet = int(input("How much would you like to bet?: "))
   while bet < 0:

       print("Invalid input, try again:")
       bet = int(input())
   dice1 = roll()
   while bank > 0 and bet > 0:
       if dice1 == 7 or dice1 == 11:
           print(f"You Win with a roll of {dice1}!")
           bank = bank + bet
           print(f"Bank = {bank}")
           return
       elif dice1 == 2 or dice1 == 3 or dice1 == 12:
           print(f"You Lost with a roll of {dice1}! :( Maybe next time!")
           bank = bank - bet
           print(f"Bank = {bank}")
           return
       else:
           point = dice1
           print(f"Your point is {point}")
           dice2 = roll()
           while point != dice2 and dice2 != 7:
               print(f"You rolled a {dice2}.")
               dice2 = roll()
               if dice2 == point:
                   print(f"You Win with a roll of {dice2}!")
                   bank = bank + bet
                   print(f"Bank = {bank}")
                   return
               else:
                   print(f"You Lost a roll of {dice2}! :( Maybe next time!")
                   bank = bank - bet
                   print(f"Bank = {bank}")
                   return


play_game()
choice = input("Would you like to play again?: ")
if choice == 'yes':
   play_game()
