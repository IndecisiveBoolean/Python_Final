from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
# from main import closeFile

def setGameLength(Window, gameTime, sessionAmmount, Tauntimage):
    addSessionCount(Window, int(sessionAmmount), int(gameTime), Tauntimage)

def addSessionCount(Window, sessions, gameTime, Tauntimage):
    newWindow = Toplevel(Window)
    newWindow.title("Result")
    newWindow.geometry("469x136")
    # Create Result Window

    responseFrame = Frame(newWindow, relief="raised", borderwidth=5)
    responseFrame.grid(column=0, row=0)
    
    estimatedTimePerSession = gameTime/sessions
    estimatedTimePerSession = round(estimatedTimePerSession * 2.0) / 2.0
    # Calculate expected length of sessions in order to beat the game within the desired time.

    tk.Label(responseFrame, text="Your estimated commitment is roughly " + str(estimatedTimePerSession) + " hours per session," + "\n" +" over " + str(sessions) + " sessions.").grid(column=1, row=0, padx=10, pady=(10, 10))
    # Render a new label containing the results of the above calculation and build within second window using grid.

    # Creation and placement of second image
    sassyImageLabel = Label(responseFrame, image=Tauntimage)
    sassyImageLabel.grid(column=0, row=0, padx=10, pady=(10, 10))