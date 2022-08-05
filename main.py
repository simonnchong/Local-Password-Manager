from tkinter import *
from tkinter import messagebox # this is not a class
from random import randint, choice, shuffle
import pyperclip # for auto copy to clipboard
import json

#* ------------------------------------------ SEARCH PASSWORD FROM JSON ------------------------------------------------- #

def search_record():
    '''search the record from database when the search button is pressed'''
    website_entry_input = website_entry.get().title() # get the data from website entry and convert it to title case
    
    if website_entry_input == "": # check if the website entry is empty
        messagebox.showinfo(title="Invalid Input", message="Please insert website/app name you want to search for") # prompt out a info window if the website entry is empty
    else: # if not empty, try to search the record from json file
        try: # catch the error if the json file is not exist
            with open("./password_database.json", "r") as json_database:  # open and set as read mode the json file 
                data = json.load(json_database) # read and load the data from json file
                
        except FileNotFoundError: # if the json file is not exist
            messagebox.showwarning(title="File not found!", message="There is no database is found!")  # prompt out a warning window if the json file is not exist
        
        else: # execute this block of code if the file is exist and able to read
            if website_entry_input in data: # if the user input website is in the database record
                email = data[website_entry_input]['email'] # get the email value from the database
                password = data[website_entry_input]['password']# get the password value from the database
                print("Website/App is found in database")
                messagebox.showinfo(title=f"{website_entry_input.title()}" , message=f"Email/Username: {email} \nPassword: {password} \nAnd the password has been copied to your clipboard!") # prompt out the to display the email and password from database
                pyperclip.copy(password) # automatically copy the password to user's clipboard
            else: # if the website is not found in the database
                messagebox.showinfo(title=f"{website_entry_input} is not found!", message=f"{website_entry_input} is not exist in the current database!") # prompt out a info window to show the particular website/app is not in the database record



#* ------------------------------------------------- PASSWORD GENERATOR ------------------------------------------------- #

def generate_password():
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
    password_entry.delete(0, END) # remove the current password, delete(from_0_index, to_last_index)
    password_entry.insert(0, password) # insert new randomized password, insert(from_0_index, content)
    
    pyperclip.copy(password) # automatically copy 
    space_label.config(text="Your random password has been copied to your clipboard!", fg="red")




#* ------------------------------------------------- SAVE PASSWORD ------------------------------------------------- #

def save_data():
    '''save the data into a txt file when "Add to database" button is pressed'''
    
    # get the data from the entry fields
    website_input = website_entry.get().title()
    email_input = email_username_entry.get()
    password_input = password_entry.get()
    
    # save the data into a dictionary to use json to send the data into "password_database.json"
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
    
    
    # check if the entry field is empty, if so, show warning message
    if len(website_input) == 0 or len(email_input)  == 0 or len(password_input) == 0 :
        messagebox.showwarning(title="Leave no blank", message="You can't leave any entry empty")
        
    # prompt out a small window and asks user for confirmation if they wanna save their data into database 
    else:
        user_confirmation = messagebox.askyesno(title=website_input, message=f"These are the details entered: \n--- Email: {email_input}\n" 
                              f"--- Password: {password_input} \nAre you sure you wanna save this into database?")
        
        if (user_confirmation): # return True if user press yes button
            # create the file if not exist, append the data into it
        
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
                    
            #? if not exist, make a new file and write the new data from the entry
            except FileNotFoundError:
                with open("./password_database.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
        
            #? if exist update the new entry into the json file
            else:
                #! json.update() -> append the data into existing json, need to perform json.load() before update()
                python_dict.update(new_data)
                
                with open("./password_database.json", "w") as data_file:
                    json.dump(python_dict, data_file, indent=4) # dump(object_you_wanna_to_save, location_of_the_file, number_of_indentation_space)

            
            
        # clear the entry field
        website_entry.delete(0, END) # remove the current text
        # website_entry.insert(0, "text_here") # insert an specific string to it
        
        password_entry.delete(0, END) # remove the current text

    
    

#* ------------------------------------------------- UI SETUP ------------------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=50, bg="white") # padding around the window 

canvas = Canvas(width=200, height=200, bg="white", highlightthickness = 0) # size of canvas
lock_image = PhotoImage(file = "./logo.png")
canvas.create_image(100, 100, image = lock_image) # position of the image
canvas.grid(row=0, column=1, columnspan=2) # columnspan is to place the element into 2 columns


website_label = Label(text="Website/App:", bg="white")
website_label.grid(row=1, column=0)
website_label.config(padx=10, pady=10)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w") # align the element to west which is left side, options = "e", "s", "w", and "n"
website_entry.focus()

search_button = Button(text="Search", width=21, command=search_record)
search_button.grid(row=1, column=2, columnspan=2)

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(row=2, column=0)
email_username_label.config(padx=10, pady=10)


email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_username_entry.insert(0, "simon@gmail.com") # insert text into entry at the beginning
# email_username_entry.insert(END, "simon@gmail.com") # insert text into entry at the end of a field, (in case you already have something in that entry just like you inserted something on previous line)

password_label = Label(text="Key-in Password:", bg="white")
password_label.grid(row=3, column=0)
password_label.config(padx=10, pady=10)


password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=3)


or_label = Label(text="OR", bg="white")
or_label.grid(row=3, column=2)
or_label.config(padx=10, pady=10)


# create an empty space before "Add to database" button
space_label = Label(text="", bg="white")
space_label.grid(row=4, column=1, columnspan=3)


add_button = Button(text="Add to database", width=53, height=2, command=save_data)
add_button.grid(row=5, column=1, columnspan=3)





window.mainloop()