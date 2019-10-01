
# importing libraries
from guizero import App, TextBox, Text, PushButton, Picture, Window
import sqlite3
    
# Create an app and makes a window
app = App(title='myVET Database', width=500, height=500)


#function which is called when the submit button on the front app is pressed 
def open_customer_window():

   #customer window code and widgets
    customer_window = Window(app, title="Add new customer")
    Text(customer_window, text="Add a customer")
    Text(customer_window, text="First name: ", align="left")
    firstName = TextBox(customer_window, text="Type here", align="left", width=15)
    PushButton(customer_window, text='Add Customer', align="bottom",command=add_new_customer, args=[customer_window,firstName])
    PushButton(customer_window, text='Cancel', align="bottom", command=cancel_customer_window, args=[customer_window])

#end of open_customer_window function

# Hides the customer window if the cancel button pressed
def cancel_customer_window(customer_window):
    customer_window.hide()
# End of cancel customer window function


# Function run when Add Customer button pressed
def add_new_customer(customer_window, firstName):
 
  first_name = firstName.value
  print(first_name) # THIS LINE JUST FOR TESTING
   #NEED SOME CODE HERE TO ADD TO Database
  ##  cursor.execute('''INSERT INTO Owner(firstname, surname, address1, address2, phone) VALUES(?,?,?,?,?)''', (variableOne,variableTwo, variableThree, variableFour, variableFive,))
  customer_window.hide()
# End of cancel customer window function





# Creates the main app page with some widgets
text = Text(app, text="myVET Database")
picture = Picture(app, image="images/vets.png")
submit = PushButton(app, text='Add new customer', command=open_customer_window)



#displays the app
app.display() 



    
