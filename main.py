import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
import calcResult

mainWindow = tk.Tk()
mainWindow.title("How Long To Beat")
# mainWindow.geometry("300x300")

frame = Frame(mainWindow)
frame.pack()


titleLabel = tk.Label(frame, text = "Calculate how long it will take you to beat a game!").grid(column=1, row=1)




########### ENTRY ### LABEL ### ENTRY ############

gameLengthEntryLabel = tk.Label(frame, text = "Enter length of game?")
gameLengthEntryLabel.grid(column=1, row=2)
gameLengthEntry = tk.Entry(frame, text = "Input the length of your game")
gameLengthEntry.grid(column=1, row=3)

sessionEntryLabel = tk.Label(frame, text = "How many sessions?").grid(column=1, row=4)
sessionCountEntry = tk.Entry(frame, text = "Input your estimated sessions")
sessionCountEntry.grid(column=1, row=5)

########### ENTRY ### LABEL ### ENTRY ############


########### BUTTONS ### BUTTONS ### BUTTONS ############

calculateMyTime = Button(frame, text = "Confirm Game Length", command=lambda: calcResult.setGameLength(mainWindow, gameLengthEntry.get(), sessionCountEntry.get())).grid(column=1, row=6)

########### BUTTONS ### BUTTONS ### BUTTONS ############


mainWindow.mainloop()