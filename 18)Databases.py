from tkinter import *
import sqlite3

root=Tk()



#Create a table
'''
c.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
addresses text,
city text,
state text,
zipcode integer
)""")

'''






f_name=Entry(root,width=30)
f_name.grid(row=0,column=1)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label=Label(root,text="City Name")
city_label.grid(row=3,column=0)
state_label=Label(root,text="State Name")
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

def submit():
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    # Create/Open a database
    conn = sqlite3.connect("address.db")
    # Create a Cursor
    c = conn.cursor()
    #Insert into the table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              }

              )
    # Commit Changes
    conn.commit()
    # Close the Connection
    conn.close()


def query():
    # Create/Open a database
    conn = sqlite3.connect("address.db")
    # Create a Cursor
    c = conn.cursor()
    #Query Database
    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    print(records)
    # Commit Changes
    conn.commit()
    # Close the Connection
    conn.close()


#Create a Submit Button

submit_button=Button(root,text="Add Record to Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a Query Button
query_button=Button(root,text="Show Records",command=query)
query_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=10)




root.mainloop()