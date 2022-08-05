from random import randint, choice, shuffle
import pyperclip # for auto copy to clipboard
from tkinter import *


#* ------------------------------------------------- PASSWORD GENERATOR ------------------------------------------------- #

class GeneratePassword:
    def __init__(self, password_entry, space_label):
        self.password_entry = password_entry
        self.space_label = space_label
        
    def generate_password(self):
        '''generate a random password if the user press "Generate Password button'''
        
        # create the compete letter, number and symbol list for generate randomly
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


        # repeat a random number times to random choose letter, number and symbol from the list
        password_letter = [choice(letters) for _ in range(randint(8, 12))]
        password_number = [choice(numbers) for _ in range(randint(1, 5))]
        password_symbol = [choice(symbols) for _ in range(randint(1, 5))]

        # combine all random letter, number and symbol into a single list
        password_list = password_letter + password_number + password_symbol


        # shuffle the list order
        shuffle(password_list)

        # join all the item in the list/tuple into a single string
        password = "".join(password_list)
        
        # insert the randomize password into password entry
        self.password_entry.delete(0, END) # remove the current password, delete(from_0_index, to_last_index)
        self.password_entry.insert(0, password) # insert new randomized password, insert(from_0_index, content)
        
        pyperclip.copy(password) # automatically copy the password to user's clipboard
        self.space_label.config(text="Your random password has been copied to your clipboard!", fg="red") # display the ext to remind user the password has been copied into their clipboard