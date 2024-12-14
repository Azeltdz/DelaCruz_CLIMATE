from tkinter import *           # tkinter file
from tkinter import messagebox  # message box
from time import *              # time module
import climateDatabase          # import database python file

# Defining colors
colors = {
    "background": "#011627",    # Background Color
    "text": "#050606",          # Text Color (White)
    "gray": "#333334",          # Lightgray Text Color
    "primary": "#4ac5ca",       # Primary Color (dark)
    "secondary": "#8aecf0",     # Secondary color (second dark)
    "accent": "#42f7fe",        # Accent color (lightest)
}

class Climate:
    def __init__(self, window):
        self.window = window
        self.window.title("Climate Learning and Informative Management for Atmospheric Typhoons and Events") # Title of the window
        self.window.geometry("1250x650+50+25") # size of the window
        self.window.config(bg=colors['background']) # background color of the window
        self.window.resizable(0, 0) # cannot resize window

        self.topFrame = Frame(self.window, bg=colors["primary"])
        self.topFrame.pack(fill=X)
        self.topFrame2 = Frame(self.window, bg=colors["background"])
        self.topFrame2.pack(fill=X)

        Label(self.topFrame, text='CLIMATE', bg=colors["primary"], font='Arial 20 bold').pack(side=LEFT, padx=10)
        Button(self.topFrame, text='LOG OUT', bg=colors["primary"], font='Arial 14', bd=0, cursor='hand2').pack(side=RIGHT, padx=5, pady=5)
        Button(self.topFrame, text='HELP', bg=colors["primary"], font='Arial 14', bd=0, cursor='hand2').pack(side=RIGHT, padx=5, pady=5)
        Button(self.topFrame, text='TYPHOON', bg=colors["primary"], font='Arial 14', bd=0, cursor='hand2').pack(side=RIGHT, padx=5, pady=5)
        Button(self.topFrame, text='ARTICLE', bg=colors["primary"], font='Arial 14', bd=0, cursor='hand2').pack(side=RIGHT, padx=5, pady=5)
        Button(self.topFrame, text='ABOUT', bg=colors["primary"], font='Arial 14', bd=0, cursor='hand2').pack(side=RIGHT, padx=5, pady=5)

        Label(self.topFrame2, text='Hello', bg=colors["primary"], font='Arial 14 bold').pack()

        # # Left Frame
        # self.leftFrame = Frame(self.window, bg=colors['background'])
        # self.leftFrame.place(relx=.02, rely=.53, relwidth=.15, relheight=.86, anchor=W)
        # # Right Frame
        # self.rightFrame = Frame(self.window, bg='green', bd=6, relief=RIDGE)
        # self.rightFrame.place(relx=.98, rely=.53, relwidth=.8, relheight=.86, anchor=E)
        # # ============================= LEFT FRAME ===========================================================
        # Label(self.leftFrame, text='CLIMATE', bg=colors['background'], font=('Helvetica', 20, 'bold')).pack()
        # # Time
        # self.time_label = Label(self.leftFrame,font=("Verdana",18), bg=colors['background']) # time
        # self.time_label.pack()
        # self.updateTime() # Clock Function
        # # Home Button
        # self.homeButton = Button(self.leftFrame, text='HOME', bg='red', activebackground='aqua', cursor='hand2')
        # self.homeButton.place(relx=.5, rely=.19, relwidth=1, relheight=.1, anchor=CENTER) 
        # # Aritcle Button
        # self.articleButton = Button(self.leftFrame, text='ARTICLE', bg='blue', activebackground='aqua', cursor='hand2')
        # self.articleButton.place(relx=.5, rely=.31, relwidth=1, relheight=.1, anchor=CENTER)
        # # Typhoon Button
        # self.typhoonButton = Button(self.leftFrame, text='TYPHOON', bg='blue', activebackground='aqua', cursor='hand2')
        # self.typhoonButton.place(relx=.5, rely=.43, relwidth=1, relheight=.1, anchor=CENTER)
        # # Calculator Button
        # self.calculatorButton = Button(self.leftFrame, text='CALCULATOR', bg='blue', activebackground='aqua', cursor='hand2')
        # self.calculatorButton.place(relx=.5, rely=.55, relwidth=1, relheight=.1, anchor=CENTER)
        # # Help Button
        # self.helpButton = Button(self.leftFrame, text='HELP', bg='blue', activebackground='aqua', cursor='hand2')
        # self.helpButton.place(relx=.5, rely=.67, relwidth=1, relheight=.1, anchor=CENTER)
        # # Log Out button
        # self.logOutButton = Button(self.leftFrame, text='LOG OUT', bg='blue', activebackground='aqua', cursor='hand2')
        # self.logOutButton.place(relx=.5, rely=.93, relwidth=1, relheight=.1, anchor=CENTER)

    def buttonClick(self):
        for widget in self.leftFrame.winfo_children(): # Iterate through all children of the parent widget
            if isinstance(widget, Button): # Check if the widget is a button
                if widget.cget("bg") == "red":  # Check if the button's background is red
                    widget.config(bg='blue') # Change the background color to the new color
        for widget in self.rightFrame.winfo_children(): # Iterate through all children of the parent widget
            widget.destroy() # Destroy all widgets
    def updateTime(self):
        self.time_label.config(text=strftime("%I:%M:%S %p"))
        self.after_id = self.window.after(1000, self.updateTime) # Update every 1 second

if __name__ == "__main__":
    window = Tk()
    app = Climate(window)
    window.mainloop()