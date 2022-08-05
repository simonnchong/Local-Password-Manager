from tkinter import *
from search_record import SearchRecord
from generate_password import GeneratePassword
from save_record import SaveData


#* ------------------------------------------------- UI SETUP ------------------------------------------------- #

window = Tk() # create the tkinter object
window.title("Local Password Manager") # set the tile of the window
window.config(padx=80, pady=50, bg="white") # padding around the window 

canvas = Canvas(width=200, height=200, bg="white", highlightthickness = 0) # create a canvas and set its size
lock_image = PhotoImage(file = "./logo.png") # load the logo image 
canvas.create_image(100, 100, image = lock_image) # set the position of the image and pass the loaded image object into it
canvas.grid(row=0, column=1, columnspan=2) # set the position of the canvas, columnspan is to expand the element into 2 columns


website_label = Label(text="Website/App:", bg="white") # create a label, set the text and its background color
website_label.grid(row=1, column=0) # set the position 
website_label.config(padx=10, pady=10) # set the padding around the element


website_entry = Entry(width=35) # create a entry (a input field), set the width to 35 pixel
website_entry.grid(row=1, column=1, columnspan=2, sticky="w") # align the element to west which is left side, options = "e", "s", "w", and "n"
website_entry.focus() # place the input cursor in this entry when the program is execute
website_record = SearchRecord(website_entry) # pass the website entry object to SearchRecord class constructor

search_button = Button(text="Search", width=21, command=website_record.search_record) # create a button, set the text in button, width size and the function name will be execute if it is pressed
search_button.grid(row=1, column=2, columnspan=2)  # set the position of the button, columnspan is to expand the element into 2 columns

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(row=2, column=0)
email_username_label.config(padx=10, pady=10)


email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_username_entry.insert(0, "simon@gmail.com") # insert text into the entry
# email_username_entry.insert(END, "simon@gmail.com") # insert text into entry at the end of a field, (in case you already have something in that entry just like you inserted something on previous line)

password_label = Label(text="Key-in Password:", bg="white")
password_label.grid(row=3, column=0)
password_label.config(padx=10, pady=10)

# create an empty space before "Add to database" button
space_label = Label(text="", bg="white")
space_label.grid(row=4, column=1, columnspan=3)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")
generate_password = GeneratePassword(password_entry, space_label)


generate_password_button = Button(text="Generate Password", command=generate_password.generate_password)
generate_password_button.grid(row=3, column=3)


or_label = Label(text="OR", bg="white")
or_label.grid(row=3, column=2)
or_label.config(padx=10, pady=10)

save_record = SaveData(website_entry, email_username_entry, password_entry)

add_button = Button(text="Add to database", width=53, height=2, command=save_record.save_data)
add_button.grid(row=5, column=1, columnspan=3)




window.mainloop() # keep the screen running 
