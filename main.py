import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
import calcResult



mainWindow = tk.Tk()
mainWindow.title("How Long To Beat")
mainWindow.geometry("500x281")
mainWindow.configure()



frame = Frame(mainWindow)
frame.pack()


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
titleLabel = tk.Label(frame, text = "Calculate how long it will take you to beat a game!", bg="black", fg="white").grid(column=1, row=1)




########### ENTRY ### LABEL ### ENTRY ############

gameLengthEntryLabel = tk.Label(frame, text = "Enter length of game?")
gameLengthEntryLabel.grid(column=1, row=2, pady=(40, 0))
gameLengthEntry = tk.Entry(frame, text = "Input the length of your game")
gameLengthEntry.grid(column=1, row=3, pady=(10, 0))

sessionEntryLabel = tk.Label(frame, text = "How many sessions?").grid(column=1, row=4, pady=(10, 0))
sessionCountEntry = tk.Entry(frame, text = "Input your estimated sessions")
sessionCountEntry.grid(column=1, row=5, pady=(10, 0))

########### ENTRY ### LABEL ### ENTRY ############




########### BUTTONS ### BUTTONS ### BUTTONS ############

calculateMyTime = Button(frame, text = "Confirm Game Length", command=lambda: calcResult.setGameLength(mainWindow, gameLengthEntry.get(), sessionCountEntry.get())).grid(column=1, row=6, pady=(30, 0))

########### BUTTONS ### BUTTONS ### BUTTONS ############




mainWindow.mainloop()