from tkinter import messagebox # this is not a class in tkinter, but tkinter use it as its feature, so it is not included in previous line
import json
from tkinter import *

#* ------------------------------------------------- SAVE PASSWORD ------------------------------------------------- #

class SaveData:
    def __init__(self, website_entry, email_username_entry, password_entry, space_label):
        self.website_entry = website_entry
        self.email_username_entry = email_username_entry
        self.password_entry = password_entry
        self.space_label = space_label
    
    def clear_entry(self):
         # after saved the data into database    
        # write -> clear the website entry field
        self.website_entry.delete(0, END) # remove the current text
        # website_entry.insert(0, "text_here") # insert an specific string to it
        
        # clear the password entry field
        self.password_entry.delete(0, END) # remove the current text
        self.space_label.config(text="") # clear the "your password has been copied" message
    
    def save_data(self):
        '''save the data into a txt file when "Add to database" button is pressed'''
        
        # read -> get the data from the entry fields
        website_input = self.website_entry.get().title()
        email_input = self.email_username_entry.get()
        password_input = self.password_entry.get()
        
        # save the data into a dictionary form to use json to pass the data into "password_database.json" file
        new_data = {
            website_input:{
                "email": email_input,
                "password": password_input,
            }
        }
        
        # prompt out a window dialog, these are the type of pop out windows
        #* ------ they have different logo
        # messagebox.showinfo
        # messagebox.showerror
        # messagebox.showwarning
        #* ------ they have different input button
        # messagebox.askokcancel
        # messagebox.askquestion
        # messagebox.askretrycancel
        # messagebox.askyesno
        # messagebox.askyesnocancel
        
        
        # check if any of the entry field is empty, if so, show warning message
        if len(website_input) == 0 or len(email_input)  == 0 or len(password_input) == 0 :
            messagebox.showwarning(title="Leave no blank", message="You can't leave any entry empty")
            
        # prompt out a small window and asks user for confirmation if they wanna save their data into database 
        else:
            user_confirmation = messagebox.askyesno(title=website_input, message=f"These are the details entered:\n\n--- Email: {email_input}\n" 
                                f"--- Password: {password_input} \n\nAre you sure you wanna save this into database?")
            
            if (user_confirmation): # return True if user press "yes" button
            
            #? check if the json file exist, if yes then read the data from the file
                try:
                    with open("./password_database.json", "r") as data_file:
                        
                        #! json.dump() -> write data (this will overwrite the existing data in json file)
                        # json.dump(new_data, data_file, indent=4) # dump(object_you_wanna_to_save, location_of_the_file, number_of_indentation_space)


                        #! json.load() -> read data
                        python_dict = json.load(data_file) # this will convert the json object into python dictionary
                        # print(python_dict)
                        # for _dict in python_dict.values():
                        #     print(_dict)
                        
                #? if not exist, make a new file and write the new data from the entry into the file
                except FileNotFoundError:
                    with open("./password_database.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4) # dump(object_you_wanna_to_save, location_of_the_file, number_of_indentation_space)
            
                #? if the file is exist, then update the new entry into the json file
                else:
                    #! json.update() -> append the data into existing json, need to perform json.load() before update()
                    with open("./password_database.json", "r") as json_database:  # open and set as read mode the json file 
                        data = json.load(json_database) # read and load the data from json file
                        json_database.close() # close the file
                        if website_input in data: # if the the website is already exist in the record
                            user_ans = messagebox.askyesno(title=f"\"{website_input}\" is existed! " , message=f"Do you wanna to update this existing record?\n\nEmail/Username: {data[website_input]['email']}\nPassword: {data[website_input]['password']}") # adk user whether wanna update/overwrite/cover the current existing record
                            if user_ans: # if user press "yes" means wanna update the existing record
                                python_dict.update(new_data) # this will add the new entry data into the dictionary and use json.dump() to pass it                               
                                with open("./password_database.json", "w") as data_file: # open the file to pass the dictionary
                                    json.dump(python_dict, data_file, indent=4) # dump(object_you_wanna_to_save, location_of_the_file, number_of_indentation_space)
                                self.clear_entry()
                        else:
                            python_dict.update(new_data) # this will add the new entry data into the dictionary and use json.dump() to pass it                               
                            with open("./password_database.json", "w") as data_file: # open the file to pass the dictionary
                                json.dump(python_dict, data_file, indent=4) # dump(object_you_wanna_to_save, location_of_the_file, number_of_indentation_space)
                                self.clear_entry()
                                