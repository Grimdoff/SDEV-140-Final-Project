#Program Name: Restraunt Front End
#Author: Jonathan Engle
#Program goal is to create an app that allows for customers to enter information and it form and display a que that the staff can edit and change
#Python 3.10
#12/13/2021 V0.2

#various imports pretty well self defined
from tkinter import *
import sqlite3


#setup tkinter main screen
root=Tk()
root.title("Main Screen")
root.geometry("800x600")

#Create Database
CustomerInfo = sqlite3.connect('Customer_book.db')

# Create cursor
c = CustomerInfo.cursor()
  

# Create table
'''
c.execute( """CREATE TABLE Customer (

		PartyName text,
		PartySize integer,
		PhoneNumber integer
		)""")
'''


#Creates the Customer facing portion of the progrm
def Waitlist():
    #Creates the main window
    root=Tk()
    root.title("Seating List")
    root.geometry("800x600")

    #Allows for customers to submit their information
    def submit():
        #Connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')
        #Create cursor
        c = CustomerInfo.cursor()

        #Inserts values into table
        c.execute("INSERT INTO Customer VALUES (:Party_name, :Party_Size, :Phone_Number)",
                {
                    'Party_name': Party_name.get(),
                    'Party_Size': Party_Size.get(),
                    'Phone_Number': Phone_Number.get(),

                })


        #Commit Changes
        CustomerInfo.commit()

        #Close Connection 
        CustomerInfo.close()

        #Clears the text boxes
        Party_name.delete(0, END)
        Party_Size.delete(0, END)
        Phone_Number.delete(0, END)

    #Shows the current people in the wait list
    def query():
        #Connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')
        #Create cursor
        c = CustomerInfo.cursor()

        #Query the database
        c.execute("SELECT *, oid FROM Customer")
        records = c.fetchall()
        # print(records)

        #Goes through results
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[3]) + "\n"

        #create label
        query_label = Label(root, text=print_records)
        query_label.grid(row=1, column=10, columnspan=2)

        #Commit Changes
        CustomerInfo.commit()


    #Create entry boxes
    Party_name = Entry(root, width=30)
    Party_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    Party_Size = Entry(root, width=30)
    Party_Size.grid(row=1, column=1)
    Phone_Number = Entry(root, width=30)
    Phone_Number.grid(row=2, column=1)

    #Create labes
    Party_name_label = Label(root, text="Please enter your party name: ")
    Party_name_label.grid(row=0, column=0, pady=(10, 0))
    Party_Size_label = Label(root, text="Please enter the number of people in your party: ")
    Party_Size_label.grid(row=1, column=0)
    Phone_Number_label = Label(root, text="Please enter a phone number that we can contact you at")
    Phone_Number_label.grid(row=2, column=0)

    # Create buttons
    submit_btn = Button(root, text="Submit", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    query_btn = Button(root, text="Show List", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    #Commit Changes
    CustomerInfo.commit()

    #Creates the exit Button
    Button(root, text="x", command=root.destroy).grid(row=1, column=10)



#Creates The staff side of the program
def Staff():
    #Sets up the window
    root=Tk()
    root.title("Administration")
    root.geometry("800x600")

    #Allows for the database information to be updated by the edit command
    def update():
        #connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')
        # Create cursor
        c = CustomerInfo.cursor()

        #retrieves ID from Entry box
        record_id = delete_box.get()

    
        #updates the record based on the entered information
        c.execute("""UPDATE Customer SET
            Party_Name = :Name,
            Party_Size = :Size,
            Phone_Number = :Number,
            Current_Time = :Time,
            WHERE oid = :oid""",
            {
            'Name': Party_name_editor.get(),
            'Size': Party_Size_editor.get(),
            'Number': Phone_Number_editor.get(),
            'oid': record_id
            })


        #Commit changes to the database
        CustomerInfo.commit()

        #Close connection to the database
        CustomerInfo.close()

        root.destroy()
        root.deiconify()
    
    #Allows for Database results to be shown
    def query():

        #Connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')

        #Create cursor
        c = CustomerInfo.cursor()
  
        #Query the database
        c.execute("SELECT *, oid FROM Customer")
        records = c.fetchall()


        #Goes through results
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[3]) + "\n"

        #creates labels
        query_label = Label(root, text=print_records)
        query_label.grid(row=3, column=8, columnspan=2, pady=10, padx=10, ipadx=143)

        #Commit Changes
        CustomerInfo.commit()

    #Allows staff to edit customer information in the database
    def edit():
        
        #Intialize window
        root=Tk()
        root.title("Customer Correction")
        root.geometry("800x600")

        #Connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')

        #Create cursor
        c = CustomerInfo.cursor()

        #retrieve the value entered in the entry box
        record_id = delete_box.get()

        #Query the database
        c.execute("SELECT * FROM Customer WHERE oid = " + record_id)
        records = c.fetchall()
        
        #Create Global Variables for text box names
        global Party_name_editor
        global Party_Size_editor
        global Phone_Number_editor
        

        #Creates entry boxers
        Party_name_editor = Entry(root, width=30)
        Party_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        Party_Size_editor = Entry(root, width=30)
        Party_Size_editor.grid(row=1, column=1)
        Phone_Number_editor = Entry(root, width=30)
        Phone_Number_editor.grid(row=2, column=1)
        
        
        #Creates labels
        Party_name_label = Label(root, text="Please enter your party's name: ")
        Party_name_label.grid(row=0, column=0, pady=(10, 0))
        Party_Size_label = Label(root, text="Please enter how many people are in your party: ")
        Party_Size_label.grid(row=1, column=0)
        Phone_Number_label = Label(root, text="Please enter a phone number so that we may call you when your table is ready: ")
        Phone_Number_label.grid(row=2, column=0)
        
        

        #Goes through results
        for record in records:
            Party_name_editor.insert(0, record[0])
            Party_Size_editor.insert(0, record[1])
            Phone_Number_editor.insert(0, record[2])


        
        # Creates button to save entries in table
        edit_btn = Button(root, text="Save Record", command=update)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    #Gives the program the ability to delete an entry on the table
    def delete():

        #Connects to the database
        CustomerInfo = sqlite3.connect('Customer_book.db')

        #Create cursor
        c = CustomerInfo.cursor()

        #Delete a record
        c.execute("DELETE from Customer WHERE oid = " + delete_box.get())

        delete_box.delete(0, END)

        #Commit Changes
        CustomerInfo.commit()

    # This definition I could not get to work
    '''def Clear_All():
        #Setup up window
        root=Tk()
        root.title("Confirmation")
        root.geometry("800x600")

        #create labels
        CLEAR_ALL_label = Label(root, text="please enter Yes to clear entire waitlist: ")
        CLEAR_ALL_label.grid(row=1, column=0, pady=5)

        #create entry box
        CLEAR_ALL_BOX = Entry(root, width=30)
        CLEAR_ALL_BOX.grid(row=1, column=2, pady=5)

        #create variable from entry box
        CLEAR = CLEAR_ALL_BOX.get()

        #Create button
        Button(root, text="Confirm?", command=CLEAR ).grid(row=1, column=10)

        #add a confirmation check before clearing all data
        if CLEAR == "y" or "yes":
            #Connects to the database
            CustomerInfo = sqlite3.connect('Customer_book.db')
            #Create cursor
            c = CustomerInfo.cursor()

            #Delete a record
            c.execute("DELETE from Customer WHERE oid = *")

            delete_box.delete(0, END)

            #Commit Changes
            CustomerInfo.commit()
        else:
            END

        #Create exit
        Button(root, text="Exit", command=root.destroy).grid(row=0, column=10)
'''
        


    #Entry box setup
    delete_box = Entry(root, width=30)
    delete_box.grid(row=2, column=1, pady=5)

    #label for entry box
    delete_box_label = Label(root, text="Please enter a party ID number to correct or to remove from the waitlist: ")
    delete_box_label.grid(row=2, column=0, pady=5)

    #Various buttons excuting the commands based the of the definitions
    delete_btn = Button(root, text="Remove party from the waitlist", command=delete)
    delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)  
    edit_btn = Button(root, text="Correct party entry", command=edit)
    edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    query_btn = Button(root, text="Show List", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    '''
    CLEAR_ALL_btn = Button(root, text="CLEAR WAITLIST", command=Clear_All)
    CLEAR_ALL_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    '''
   

    #Commit Changes
    CustomerInfo.commit()
    Button(root, text="x", command=root.destroy).grid(row=1, column=10)



#Connects to the database
CustomerInfo = sqlite3.connect('Customer_book.db')

#Create cursor
c = CustomerInfo.cursor()

#Selects all values from database
c.execute("SELECT *, oid FROM Customer")

#creates a variable equal to the values
records = c.fetchall()


#Creates a printed listed of the seating order
print_records = ''
for record in records:
    print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[3]) + "\n"


#Various Labels
query_label = Label(root, text=print_records)
query_label.grid(row=3, column=8, columnspan=2, pady=10, padx=10, ipadx=143)

#Main Menu Buttons
Staff_btn = Button(root, text="Staff", command=Staff)
Staff_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
Waitlist_btn = Button(root, text="Customer", command=Waitlist)
Waitlist_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit Changes
CustomerInfo.commit()

#Keeps main window open
root.mainloop()
