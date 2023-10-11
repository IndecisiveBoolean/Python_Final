from tkinter import *
import tkinter as tk


def setGameLength(Window, gameTime, sessionAmmount):
    print(Window)
    gameLength = int(gameTime)
    # Store game length from entry passed in via arg
    # print(type(gameLength))
    # Verify Storage
    
    print(str(gameLength) + " hours")

    addSessionCount(Window, int(sessionAmmount), int(gameTime))


def addSessionCount(Window, sessions, gameTime):
    newWindow = Toplevel(Window)
    newWindow.title("Result")
    # Create Result Window
    

    estimatedTimePerSession = gameTime/sessions
    estimatedTimePerSession = round(estimatedTimePerSession * 2.0) / 2.0
    print(estimatedTimePerSession)
    print("Your estimated commitement is " + str(estimatedTimePerSession) + "hrs per session, over " + str(sessions) + " sessions.")
    tk.Label(newWindow, text="Your estimated commitment is roughly " + str(estimatedTimePerSession) + " hours per session," + "\n" +" over " + str(sessions) + " sessions.").grid(row=1, column=0)
