import json
from tkinter import messagebox # this is not a class in tkinter, but tkinter use it as its feature, so it is not included in previous line
import pyperclip # for auto copy to clipboard

#* ------------------------------------------ SEARCH PASSWORD FROM JSON ------------------------------------------------- #

class SearchRecord:
    def __init__(self, website_entry):
        self.website_entry = website_entry
    
    def search_record(self):
        '''search the record from database when the search button is pressed'''
        website_entry = self.website_entry.get().title() # get the data from website entry and convert it to title case
        
        if website_entry == "": # check if the website entry is empty
            messagebox.showinfo(title="Invalid Input", message="Please insert website/app name you want to search for") # prompt out a info window if the website entry is empty
        else: # if not empty, try to search the record from json file
            try: # catch the error if the json file is not exist
                with open("./password_database.json", "r") as json_database:  # open and set as read mode the json file 
                    data = json.load(json_database) # read and load the data from json file
                    
            except FileNotFoundError: # if the json file is not exist
                messagebox.showwarning(title="File not found!", message="There is no database is found!")  # prompt out a warning window if the json file is not exist
            
            else: # execute this block of code if the file is exist and able to read
                if website_entry in data: # if the user input website is in the database record
                    email = data[website_entry]['email'] # get the email value from the database
                    password = data[website_entry]['password']# get the password value from the database
                    print("Website/App is found in database")
                    messagebox.showinfo(title=f"\"{website_entry}\"" , message=f"--- Email/Username: {email} \n--- Password: {password} \n\nThe password has been copied to your clipboard!") # prompt out the to display the email and password from database
                    pyperclip.copy(password) # automatically copy the password to user's clipboard
                else: # if the website is not found in the database
                    messagebox.showinfo(title=f"\"{website_entry}\" is not found!", message=f"{website_entry} is not exist in the current database!") # prompt out a info window to show the particular website/app is not in the database record
