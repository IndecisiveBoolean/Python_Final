import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
import calcResult

mainWindow = tk.Tk()
mainWindow.title("How Long To Beat")
mainWindow.geometry("500x300")


titleLabel = tk.Label(mainWindow, text = "Calculate how long it will take you to beat a game!").grid(column=1, row=1)


########### ENTRY ### LABEL ### ENTRY ############

gameLengthEntryLabel = tk.Label(mainWindow, text = "Enter length of game?")
gameLengthEntryLabel.grid(column=1, row=2)
gameLengthEntry = tk.Entry(mainWindow, text = "Input the length of your game")
gameLengthEntry.grid(column=1, row=3)

sessionEntryLabel = tk.Label(mainWindow, text = "How many sessions?").grid(column=1, row=4)
sessionCountEntry = tk.Entry(mainWindow, text = "Input your estimated sessions")
sessionCountEntry.grid(column=1, row=5)

########### ENTRY ### LABEL ### ENTRY ############


########### BUTTONS ### BUTTONS ### BUTTONS ############

calculateMyTime = Button(mainWindow, text = "Confirm Game Length", command=lambda: calcResult.setGameLength(mainWindow, gameLengthEntry.get(), sessionCountEntry.get())).grid(column=0, row=3)

########### BUTTONS ### BUTTONS ### BUTTONS ############


mainWindow.mainloop()