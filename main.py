import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
from calcResult import addSessionCount, addGameLength

# # A working GUI tkinter application with at least two windows.   50 points
# DONE ^^^^^^^^^^^^^^^^^^^^^

# Implementing a modular approach in your application. 10 points
# Consistent clear navigation throughout the GUI application.   10 points

# Use at least two images in your application(images should have alternate text).  10 points
mainWindow = tk.Tk()
mainWindow.title("How Long To Beat")
mainWindow.geometry("500x300")

# VARIABLES FOR STORAGE
gameLength = int
sessionCount = int


titleLabel = tk.Label(mainWindow, text = "Calculate how long it will take you to beat a game!").grid(column=1, row=1)

########### BUTTONS ### BUTTONS ### BUTTONS ############

gameLengthConfirm = Button(mainWindow, text = "Confirm Game Length", command=addGameLength(gameLength)).grid(column=0, row=2)
sessionEstimationButton = Button(mainWindow, text = "Confirm Sessions", command=addSessionCount(sessionCount)).grid(column=0, row=3)

########### BUTTONS ### BUTTONS ### BUTTONS ############


########### ENTRY ### LABEL ### ENTRY ############

gameLengthEntryLabel = tk.Label(mainWindow, text = "Enter length of game?").grid(column=1, row=2)
gameLengthEntry = tk.Entry(mainWindow, text = "Input the length of your game")
gameLengthEntry.grid(column=1, row=2)

sessionEntryLabel = tk.Label(mainWindow, text = "How many sessions?").grid(column=1, row=3)
sessionCountEntry = tk.Entry(mainWindow, text = "Input your estimated sessions")
sessionCountEntry.grid(column=1, row=3)

########### ENTRY ### LABEL ### ENTRY ############

mainWindow.mainloop()


    
# Array
#  [itemx, [str, def, agi]]

# def createInventory(newWindow):

#     # inventoryItems = [
#     #     item1,
#     #     item2,
#     #     item3,
#     #     item4,
#     #     item5
#     # ]

#     colSelector = 0
#     for x in inventoryItems:
#         print(x)
#         print(inventoryItems)
#         x = Button(newWindow, image = x, height=90, width=90, command = viewInfo).grid(row=0, column=colSelector)


#         colSelector += 1
    
# def viewInfo():
#     infoWinddow = Toplevel()
#     infoWinddow.title("ITEM INFORMATION")
#     infoWinddow.geometry("300x500")
    

# def newWindow():
#     secondWindow = Toplevel()
#     secondWindow.title("Second Window")
#     secondWindow.geometry("500x400")

#     createInventory(secondWindow)


# imageBtn = tk.Label(image = img1Create)
# imageBtn.image = img1Create

# imageBtn.grid(column=1)
# btnOpen1 = Button(mainWindow, text = "Generate Inventory", command=newWindow).grid(row=0, column=0)

# Include at least three labels. 10 points

# Include at least three buttons. 10 points

# Include at least three or actions 20 points

# Implement secure coding best practices, including input validation to check if the user entered the correct data type, make sure the entry box is not empty, etc.   10 points

# Validation testing - 20 points.  Develop an appropriate set of test data to fully validate the program against.