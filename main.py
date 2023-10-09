import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  

# # A working GUI tkinter application with at least two windows.   50 points
# DONE ^^^^^^^^^^^^^^^^^^^^^

# Implementing a modular approach in your application. 10 points
# Consistent clear navigation throughout the GUI application.   10 points

# Use at least two images in your application(images should have alternate text).  10 points
mainWindow = tk.Tk()
mainWindow.title("MAIN WINDOW")
mainWindow.geometry("500x500")

# img1 = PhotoImage(file = "coat_1.png")
# img1 = img1.subsample(3, 3)

# GLOBAL VARS TO BYPASS GARBCOLLECT

item1 = str
item2 = str


xSettings = str
x = Button(xSettings)
# CURRENTLY ERRORS DUE TO STR TYPE CAUSING CONFLICT
# BUTTON NEEDS TO BE INSTANTIATED OUTSIDE OF THE FUNCTION so that assigned image value remains persistant after garbage collection.

def createInventory():
    global xSettings
    
    item1 = PhotoImage(file = "coat_1.png")
    item1 = item1.subsample(3, 3)
    item2 = PhotoImage(file = "coat_2.png")
    item2 = item2.subsample(3, 3)

    inventoryItems = [
        item1,
        item2
    ]
    
    colSelector = 0
    for x in inventoryItems:
        print(x)
        print(inventoryItems)
        
        xSettings = "mainWindow, image = x, command=newWindow, height=90, width=90).grid(row=0, column=colSelector"

        colSelector += 1


def newWindow():
    secondWindow = Toplevel()
    secondWindow.title("Second Window")
    secondWindow.geometry("400x400")


# imageBtn = tk.Label(image = img1Create)
# imageBtn.image = img1Create

# imageBtn.grid(column=1)
btnOpen1 = Button(mainWindow, text = "Generate Inventory", command = createInventory).grid(row=0, column=0)


mainWindow.mainloop()









# Include at least three labels. 10 points

# Include at least three buttons. 10 points

# Include at least three call back function with each button, including exit button. 20 points

# Implement secure coding best practices, including input validation to check if the user entered the correct data type, make sure the entry box is not empty, etc.   10 points

# Validation testing - 20 points.  Develop an appropriate set of test data to fully validate the program against.