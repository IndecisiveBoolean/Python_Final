# """
# Author:  Josh Fowler
# Date written: 10/12/23
# Assignment:   Module 08 - Final
# Short Desc:   A small program that allows you to estimate the lengths of each gaming session in order to beat the game within a specified session count/restriction.
# """

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
import calcResult

# root window for entire application is created and sized here.
mainWindow = tk.Tk()
mainWindow.title("How Long To Beat")
mainWindow.geometry("500x281")
# mainWindow.configure()


malo_bg = ImageTk.PhotoImage(file="./images/malo_twilight-princess.png")

# Image is opened and resized appropriately
background = Image.open("./images/birdman_oshi-no-ko.png")
background = background.resize((500, 281))

# image converter to PhotoImage for better compatibility with Tkinter
piyo_bg = ImageTk.PhotoImage(background)

# Frame for bg is created
    # Allows bg to be beneath main elements/widgets
frame = Frame(mainWindow, relief="raised", borderwidth=2)
# frame is inserted via pack and set to fill/expand
frame.pack(fill=BOTH, expand=YES)
# frame.pack_propagate(False)

# Label is created to contain bg image
    # Label inserted into window via place.
bg_label = Label(frame, image=piyo_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# header is created
titleLabel = tk.Label(frame, text = "Estimate Stream Session Lengths via Game Length", bg="black", fg="white").grid(column=1, row=1)


########### ENTRY ### LABEL ### ENTRY ############

gameLengthEntryLabel = tk.Label(frame, text = "Enter length of game?")
gameLengthEntryLabel.grid(column=1, row=2, pady=(40, 0))
gameLengthEntry = tk.Entry(frame, text = "Input the length of your game")
gameLengthEntry.grid(column=1, row=3, pady=(10, 0))

sessionEntryLabel = tk.Label(frame, text = "How many sessions?").grid(column=1, row=4, pady=(10, 0))
sessionCountEntry = tk.Entry(frame, text = "Input your estimated sessions")
sessionCountEntry.grid(column=1, row=5, pady=(10, 0))

########### ENTRY ### LABEL ### ENTRY ############

def resetInputs():
    sessionCountEntry.delete(0, END)
    gameLengthEntry.delete(0, END)

# Function to verify datatype in entry fields.
def dataCheck():
    gameLengthCheck = gameLengthEntry.get()
    sessionLengthCheck = sessionCountEntry.get()

    

    if str.isdigit(gameLengthCheck) == True and str.isdigit(sessionLengthCheck) == True:
        calcResult.setGameLength(mainWindow, gameLengthEntry.get(), sessionCountEntry.get(), malo_bg)
    else:
        errorWindow = Toplevel(mainWindow)
        errorWindow.title("ERROR: INPUT NOT VALID")
        errorWindow.geometry("424x75")

        errorMsgFrame = Frame(errorWindow, relief="raised", borderwidth=2)
        errorMsgFrame.grid(column=0, row=0)

        errorResetFrame = Frame(errorWindow, relief="raised", borderwidth=0)
        errorResetFrame.grid(column=0, row=1, pady=(5, 0))

        tk.Label(errorMsgFrame, text="Input not valid, ensure both fields contain ONLY whole numbers and try again.").grid(column=0, row=0)
        closeErrorNotice = tk.Label(errorResetFrame, text = "Try Again").grid(column=0, row=0)
        print("test")
        

##### Unsure of how to get this errorWindow to close (or be destroyed) with a method call. Tkinter seems to be extremely unruly regarding logic flow.

        # closeErrorNotice = Button(errorResetFrame, text = "Try Again", command=lambda: [resetInputs, errorWindow.destroy]).grid(column=0, row=0)

########### BUTTONS ### BUTTONS ### BUTTONS ############

calculateMyTime = Button(frame, text = "Estimate Session Length", command=dataCheck).grid(column=1, row=6, pady=(20, 0))

# Create button to terminate program
exitProgram = Button(frame, text = "EXIT", command=mainWindow.destroy).grid(column=1, row=7, padx=(0, 224), pady=(30, 0))

########### BUTTONS ### BUTTONS ### BUTTONS ############

# function that handles closure/termination of mainWindow instance
def closeFile():
    mainWindow.destroy
    

mainWindow.mainloop()