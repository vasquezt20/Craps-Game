#Tyler Vasquez
#Craps
#Oct 24, 2019

import random


def create():
   bank = int(input("How much would you like to put in the bank?: "))
   return bank


def roll():
   dice = random.randint(1,6) + random.randint(1,6)
   return dice

def play_again():
    choice = input("Would you like to play again?: ")
    if choice == 'yes' or 'yeah':
        play_game()
    else:
        return
    return

def play_game():
   bank = create()
   bet = int(input("How much would you like to bet?: "))
   while bet < 0:

       print("Cannot enter, re-try:")
       bet = int(input())
   dice1 = roll()
   while bank > 0 and bet > 0:
       if dice1 == 7 or dice1 == 11:
           print(f"You rolled a {dice1}, Winner!")
           bank = bank + bet
           print(f"Your bank = {bank}")
           play_again()
           return
       elif dice1 == 2 or dice1 == 3 or dice1 == 12:
           print(f"You rolled a {dice1}, Loser!")
           bank = bank - bet
           print(f"Bank = {bank}")
           play_again()
           return
       else:
           point = dice1
           print(f"Your point value is {point}")
           dice2 = roll()
           while point != dice2 and dice2 != 7:
               print(f"You rolled a {dice2}.")
               dice2 = roll()
           if dice2 == point:
               print(f"You rolled a {dice2}, winner!")
               bank = bank + bet
               print(f"Bank = {bank}")
               play_again()
               return
           else:
               print(f"You rolled a {dice2}, Loser!")
               bank = bank - bet
               print(f"Bank = {bank}")
               play_again()
               return
   if bank <= 0:
       print("You have no money left: Game Over!")
       play_again()


play_game()
