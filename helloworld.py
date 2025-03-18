'''
Rumplestilkson 
author: Sam McGuire
version: 1

Description:  This is a guessing game based on the tale
of Rumplestilskon.  Users have three chances to guess the 
name randomly selected from the list

'''

# Import library or external code. OS for sleep and clear screen
import os

# Set variables for list, user guess, guess counter 

INT_GUESSREMAINING = 3
bool_endLoop = False
str_userGuess = ''
str_userName = ''

# Creating game functions

def greeting():
    str_userName = input("Hello.  What is your name?")
    print(f"Hello {str_userName}")
    
    
# The Main program
greeting()
