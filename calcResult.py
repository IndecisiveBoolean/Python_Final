from tkinter import *
import tkinter as tk


def setGameLength(Window, gameTime, sessionAmmount):
    addSessionCount(Window, int(sessionAmmount), int(gameTime))

def addSessionCount(Window, sessions, gameTime):
    newWindow = Toplevel(Window)
    newWindow.title("Result")
    # Create Result Window
    
    estimatedTimePerSession = gameTime/sessions
    estimatedTimePerSession = round(estimatedTimePerSession * 2.0) / 2.0
    # Calculate expected length of sessions in order to beat the game within the desired time.

    tk.Label(newWindow, text="Your estimated commitment is roughly " + str(estimatedTimePerSession) + " hours per session," + "\n" +" over " + str(sessions) + " sessions.").grid(row=1, column=0)
    # Render a new label containing the results of the above calculation and build within second window using grid.