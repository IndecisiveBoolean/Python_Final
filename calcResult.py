# """
# Author:  Josh Fowler
# Date written: 10/12/23
# Assignment:   Module 08 - Final-submodule
# Short Desc:   This module handles the calculations of the given values from the MAIN module.
# """

from tkinter import *
import tkinter as tk

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




    
    ##### A working GUI tkinter application with at least two windows.  - 50 points

    ##### Implementing a modular approach in your application.  - 10 points

    ##### Consistent clear navigation throughout the GUI application.  - 10 points

    ##### Use at least two images in your application(images should have alternate text).  - 10 points

    ##### Include at least three labels. - 10 points

    #### Include at least three buttons. - 10 points

    #### Include at least three call-back functions with each button, including the exit button. - 20 points

    # Implement secure coding best practices, including input validation to check if the user entered the correct data type, make sure the entry box is not empty, etc.  - 10 points
