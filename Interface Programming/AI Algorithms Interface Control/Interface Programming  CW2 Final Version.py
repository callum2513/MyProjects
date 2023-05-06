# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:19:11 2022

@author: callum
"""

########## COMMENTS REFER TO THE CODE ON THE LINE BELOW THEM ##########

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as font

# Defining Main Window
masterWindow=Tk()
# Title of the Window
masterWindow.title('Gesture Driven Programming')
# Setting the size of the window and its location on screen
masterWindow.geometry("1080x720+600+200")

# Create HelloWorldWindow
helloWorldWindow=Tk()
# Setting the size of the window and its location on screen
helloWorldWindow.geometry("1080x720+600+200")
# Title of the Window
helloWorldWindow.title("Hello World Programme")
# Hides Window, will be shown again when hellow world programme button is clicked
helloWorldWindow.withdraw();

# Create TimerWindow
timerWindow=Tk()
# Setting the size of the window and its location on screen
timerWindow.geometry("1080x720+600+200")
# Title of the Window
timerWindow.title("Timer Programme")
# Hides Window, will be shown again when hellow world programme button is clicked
timerWindow.withdraw();

# Create IFWindow
IFWindow=Tk()
# Setting the size of the window and its location on screen
IFWindow.geometry("1080x720+600+200")
# Title of the Window
IFWindow.title("IF Programme")
# Hides Window, will be shown again when hellow world programme button is clicked
IFWindow.withdraw();


# Font for the button text
buttonFont = font.Font(family='Helvetica', size=12, weight='bold')
# Font for the screen Title
titleFont = font.Font(family='Helvetica', size=20, weight='bold')
# Font for the code 
codeFont = font.Font(family='Helvetica', size=20, weight='bold')

# Open Hello World Programme Button - Located on main menu, prints to console and shows the helloWorldWindow which was previosuly hidden
def btnOpenHelloWorldClick():
    print("You Clicked Hello World Button")
    helloWorldWindow.deiconify();
    helloWorldInstructionLabel = tk.Label(helloWorldWindow, text = "There is a line missing from the code below \n Choose the correct snippet from the buttons on the left \n Then click the check button to complete the code \n\n\nfrom tkinter import * \n from tkinter import ttk \n root = Tk() \n frm = ttk.Frame(root, padding=10) \n frm.grid() \n ------SELECT CORRECT CODE------ \n root.mainloop()")
    helloWorldInstructionLabel.place(x = 400, y = 100)
    
# Open Timer Programme Button - Located on main menu, prints to console and shows the helloWorldWindow which was previosuly hidden
def btnOpenTimerClick():
    print("You Clicked Timer Button")
    timerWindow.deiconify();
    timerInstructionLabel = tk.Label(timerWindow, text = "There is a line missing from the code below \n Choose the correct snippet from the buttons on the left \n Then click the check button to complete the code \n\n\n import time \n for i in range(10,0, -1): \n ------SELECT CORRECT CODE------ \n timelseep(1) \n print ('Countdown Complete')")
    timerInstructionLabel.place(x = 400, y = 100)

# Open IF Statement Programme Button - Located on main menu, prints to console and shows the helloWorldWindow which was previosuly hidden
def btnOpenIFClick():
    IFWindow.deiconify();
    IFInstructionLabel = tk.Label(IFWindow, text = "There is a line missing from the code below \n Choose the correct snippet from the buttons on the left \n Then click the check button to complete the code \n\n\n a = 10 \n b = 20 \n if a < b \n ------SELECT CORRECT CODE------")
    IFInstructionLabel.place(x = 400, y = 100)
    
# Main Menu exit button that destroys the main window and ends programme
def btnExitClick():
    print("You Clicked Exit Button")
    masterWindow.withdraw()
    
# Menu button that that destroys the programme windows and returns to the main menu
def btnToMenuClick():
    print("You Clicked Back to Menu Button")
    helloWorldWindow.withdraw()
    timerWindow.withdraw()
    IFWindow.withdraw()
    
# Menu button that that destroys the programme windows and returns to the main menu
def btnTimerToMenuClick():
    print("You Clicked Back to Menu Button")
    helloWorldWindow.withdraw()
    timerWindow.withdraw()
    IFWindow.withdraw()
    
# Menu button that that destroys the programme windows and returns to the main menu
def btnIFToMenuClick():
    print("You Clicked Back to Menu Button")
    helloWorldWindow.withdraw()
    timerWindow.withdraw()
    IFWindow.withdraw()
    
########################################################################### MAIN MENU ITEMS ##########################################################################   
# Creating Title label and placing it on screen
titleLabel = tk.Label(masterWindow, text = "Please Select One of the Three Programmes below to get started", font = titleFont)
titleLabel.pack();
titleLabel.place(x = 125, y = 35)
    
# Creating Programme One Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnProgrammeOne = Button(masterWindow, text ="Hello World", fg="black", bg="grey", font = buttonFont, command=btnOpenHelloWorldClick)
btnProgrammeOne.place(x= 75, y = 150)
btnProgrammeOne.config(height = 6, width = 24)

# Creating Programme Two Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnProgrammeTwo = Button(masterWindow, text ="Timer", fg="black", bg="grey", font = buttonFont, command=btnOpenTimerClick)
btnProgrammeTwo.place(x= 425, y = 150)
btnProgrammeTwo.config(height = 6, width = 24)

# Creating Programme Three Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnProgrammeThree = Button(masterWindow, text ="If Statement", fg="black", bg="grey", font = buttonFont, command=btnOpenIFClick)
btnProgrammeThree.place(x= 750, y = 150)
btnProgrammeThree.config(height = 6, width = 24)

# Creating Close Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnClose = Button(masterWindow, text ="Exit", fg="black", bg="grey", font = buttonFont, command=btnExitClick)
btnClose.place(x= 415, y = 575)
btnClose.config(height = 6, width = 24)



########################################################################### HELLO WORLD PROGRAMME ##################################################################### 

# Hello World exit button that destroys hello world window and retuns to menu
def btnHelloWorldSnippetOne():
    messagebox.showinfo("Programme Run Successfully", "That Code is Correct! - Hello World")
    
def btnHelloWorldSnippetTwo():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")
    
def btnHelloWorldSnippetThree():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")

#font for code buttons
codeButtonFont = font.Font(family='Helvetica', size=7, weight = 'bold')

# Creating Title label
helloWorldTitleLabel = tk.Label(helloWorldWindow, text = "Select the correct Code Snippet to complete the programme", font = titleFont)
helloWorldTitleLabel.pack(padx = 100, pady = 25);

# Creating CodeSnipppetOne Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnHelloWorldSnippetOne = Button(helloWorldWindow, text ="ttk.Label(frm, text='Hello World!').grid\n(column=0, row=0)", fg="black", bg="grey", font = codeButtonFont, command = btnHelloWorldSnippetOne)
btnHelloWorldSnippetOne.place(x= 25, y = 75)
btnHelloWorldSnippetOne.config(height = 6, width = 30)

# Creating CodeSnipppetTwo Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnHelloWorldSnippetTwo = Button(helloWorldWindow, text ="Label.setText('Hello World')", fg="black", bg="grey", font = codeButtonFont, command = btnHelloWorldSnippetTwo)
btnHelloWorldSnippetTwo.place(x= 25, y = 225)
btnHelloWorldSnippetTwo.config(height = 6, width = 30)

# Creating CodeSnipppetThree Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnHelloWorldSnippetThree = Button(helloWorldWindow, text ="ttk,Label.SetText('Hello World')", fg="black", bg="grey", font = codeButtonFont, command = btnHelloWorldSnippetThree)
btnHelloWorldSnippetThree.place(x= 25, y = 375)
btnHelloWorldSnippetThree.config(height = 6, width = 30)


# Creating Close Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnHelloWorldClose = Button(helloWorldWindow, text ="Menu", fg="white", bg="maroon", font = buttonFont, command=btnToMenuClick)
btnHelloWorldClose.place(x= 25, y = 525)
btnHelloWorldClose.config(height = 6, width = 30)






########################################################################### TIMER PROGRAMME ########################################################################### 
# Showing Message boxes that tell the user if their asnwer is correct or incorrect depending on which snippet the user chooses, e.g. the below code shows that snippet two is the correct code
def btnTimerSnippetOne():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")
    
def btnTimerSnippetTwo():
    messagebox.showinfo("Programme Run Successfully", "That Code is Correct!")
    
def btnTimerSnippetThree():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")

#font for code buttons
codeButtonFont = font.Font(family='Helvetica', size=7, weight = 'bold')

# Creating Title label
timerTitleLabel = tk.Label(timerWindow, text = "Select the correct Code Snippet to complete the programme", font = titleFont)
timerTitleLabel.pack(padx = 100, pady = 25);

# Creating CodeSnipppetOne Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnTimerSnippetOne = Button(timerWindow, text ="printf(i)", fg="black", bg="grey", font = codeButtonFont, command = btnTimerSnippetOne)
btnTimerSnippetOne.place(x= 25, y = 75)
btnTimerSnippetOne.config(height = 6, width = 30)

# Creating CodeSnipppetTwo Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnTimerSnippetTwo = Button(timerWindow, text ="print(i)", fg="black", bg="grey", font = codeButtonFont, command = btnTimerSnippetTwo)
btnTimerSnippetTwo.place(x= 25, y = 225)
btnTimerSnippetTwo.config(height = 6, width = 30)

# Creating CodeSnipppetThree Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnTimerSnippetThree = Button(timerWindow, text ="writeLine(i)", fg="black", bg="grey", font = codeButtonFont, command = btnTimerSnippetThree)
btnTimerSnippetThree.place(x= 25, y = 375)
btnTimerSnippetThree.config(height = 6, width = 30)


# Creating Close Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnTimerClose = Button(timerWindow, text ="Menu", fg="white", bg="maroon", font = buttonFont, command=btnToMenuClick)
btnTimerClose.place(x= 25, y = 525)
btnTimerClose.config(height = 6, width = 30)





########################################################################### IF STATEMENT PROGRAMME #################################################################### 
# Showing Message boxes that tell the user if their asnwer is correct or incorrect depending on which snippet the user chooses, e.g. the below code shows that snippet two is the correct code
def btnIFSnippetOne():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")
    
def btnIFSnippetTwo():
    messagebox.showinfo("Programme Run Failed", "Incorrect: Try Again")
    
def btnIFSnippetThree():
    messagebox.showinfo("Programme Run Successfully", "That Code is Correct!")

#font for code buttons
codeButtonFont = font.Font(family='Helvetica', size=7, weight = 'bold')

# Creating Title label
IFTitleLabel = tk.Label(IFWindow, text = "Select the correct Code Snippet to complete the programme", font = titleFont)
IFTitleLabel.pack(padx = 100, pady = 25);

# Creating CodeSnipppetOne Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnIFSnippetOne = Button(IFWindow, text ="output ('First Condition is true')", fg="black", bg="grey", font = codeButtonFont, command = btnIFSnippetOne)
btnIFSnippetOne.place(x= 25, y = 75)
btnIFSnippetOne.config(height = 6, width = 30)

# Creating CodeSnipppetTwo Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnIFSnippetTwo = Button(IFWindow, text ="else if (b == a)", fg="black", bg="grey", font = codeButtonFont, command = btnIFSnippetTwo)
btnIFSnippetTwo.place(x= 25, y = 225)
btnIFSnippetTwo.config(height = 6, width = 30)

# Creating CodeSnipppetThree Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnIFSnippetThree = Button(IFWindow, text ="print ('First Condition is true')", fg="black", bg="grey", font = codeButtonFont, command = btnIFSnippetThree)
btnIFSnippetThree.place(x= 25, y = 375)
btnIFSnippetThree.config(height = 6, width = 30)

# Creating Close Button, adding text to it and placing it on the window using X&Y coordinates after resizing it
btnIFClose = Button(IFWindow, text ="Menu", fg="white", bg="maroon", font = buttonFont, command=btnToMenuClick)
btnIFClose.place(x= 25, y = 525)
btnIFClose.config(height = 6, width = 30)



# Main Loop method which is an event listening loop, application is now constatly waiting for any event generated on the any of the application elements
masterWindow.mainloop()








