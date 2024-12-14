from tkinter import *           # tkinter file
from tkinter import messagebox  # message box
from time import *              # time module
from tkinter import ttk         # Themed Tkinter Widgets (combobox)
from textwrap import wrap       # Wrapping long text into multiple lines
import climateDatabase          # import database python file

# Defining colors
colors = {
    "text": "#050606",          # Text Color (black)
    "background": "#f6fafa",    # Background Color
    "primary": "#4ac5ca",       # Primary Color (dark)
    "secondary": "#8aecf0",     # Secondary color (second dark)
    "accent": "#42f7fe",        # Accent color (lightest)
    "gray": "#333334",          # Lightgray Text Color
}
# Climate Learning and Informative Management for Atmospheric Typhoons and Events CLIMATE
# Log In Window
class logIn:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1240x640+10+50")
        self.window.title("Log In Page")
        self.window.resizable(0, 0) # cannot resize window
        # Window Background Image
        self.background = PhotoImage(file='background.png')
        bg_label = Label(self.window, image=self.background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Frame Images for Transparancy
        self.loginbg = PhotoImage(file='loginbg.png') # login form background picture to make it look transparent
        self.clockbg = PhotoImage(file='clockbg.png') # clock background picture to make it look transparent
        # Clock Frame
        self.clockFrame = Frame(self.window)
        self.clockFrame.place(relx=.18, rely=.55, anchor=W)
        self.clockLabel = Label(self.clockFrame, image=self.clockbg)
        self.clockLabel.place(relx=0, rely=0, relheight=1, relwidth=1)
        # Clock Labels
        self.day_label = Label(self.clockFrame,font=("Verdana",25,"bold"), bg=colors['accent']) # Day
        self.day_label.grid(row=0, column=0)
        self.date_label = Label(self.clockFrame,font=("Verdana",30), bg=colors['accent']) # Date
        self.date_label.grid(row=1, column=0)
        self.time_label = Label(self.clockFrame,font=("Verdana",30), bg=colors['accent']) # time
        self.time_label.grid(row=2, column=0)
        self.updateTime() # Clock Function
        # Log In Form Frame
        self.loginFrame = Frame(self.window)
        self.loginFrame.place(relx=.95, rely=.5, width=350, height=450, anchor=E)
        self.loginlabel = Label(self.loginFrame, image=self.loginbg)
        self.loginlabel.place(relx=0, rely=0, relheight=1, relwidth=1)
        # Profile Icon
        self.profile = PhotoImage(file='profile.png')
        Label(self.loginFrame, image=self.profile, bg=colors['accent'], width=100, height=100, bd=0).pack(pady=20)
        # Log In Text
        Label(self.loginFrame, text='Log in to Climate', font='Courier 16 bold', bg=colors['accent']).pack(pady=(0, 5))
        # Username Input Fields
        self.username = Entry(self.loginFrame, width=22, bg=colors['accent'], font='Courier 16 bold', relief=RAISED, fg=colors['gray'])
        self.username.pack(pady=10)
        self.username.insert(0, 'Username')
        self.username.bind('<FocusIn>', lambda event: self.username.delete(0, END) if self.username.get() == 'Username' else None)
        self.username.bind('<FocusOut>', lambda event: self.username.insert(0, 'Username') if not self.username.get() else None)
        # Password Input Fields
        self.password = Entry(self.loginFrame, width=22, bg=colors['accent'], font='Courier 16 bold', relief=RAISED, show='*', fg=colors['gray'])
        self.password.pack(pady=10)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', lambda event: self.password.delete(0, END) if self.password.get() == 'Password' else None)
        self.password.bind('<FocusOut>', lambda event: self.password.insert(0, 'Password') if not self.password.get() else None)
        # Eye Icon Button to show password
        self.hideImage = PhotoImage(file='hide.png') # Hide eye Icon Image
        self.showImage = PhotoImage(file='show.png') # Show eye Icon Image
        self.showButton = Button(self.password, image=self.hideImage, bd=0, bg=colors['accent'], activebackground=colors['accent'], cursor='hand2', pady=5)
        self.showButton.bind('<ButtonPress-1>', lambda event: (self.password.config(show=''), self.showButton.config(image=self.showImage)))
        self.showButton.bind('<ButtonRelease-1>', lambda event: (self.password.config(show='*'), self.showButton.config(image=self.hideImage)))
        self.showButton.place(relx=.97, rely=.5, anchor=E)
        # Login Button
        self.loginBtn = Button(self.loginFrame, width=25, text='Log In', bg=colors['accent'], cursor='hand2', activebackground=colors['primary'], relief=RAISED, command=self.login)
        self.loginBtn.pack(pady=5)
        # Create New Account Button
        self.newBtn = Button(self.loginFrame, width=25, text='Create New Account', bg=colors['accent'], cursor='hand2', activebackground=colors['primary'], relief=RAISED, command=self.newAcc)
        self.newBtn.pack(pady=5)
        # HELP BUTTON
        self.helpBtn = Button(self.loginFrame, width=3, text='?', font='Arial 18 bold', bg=colors['accent'], cursor='hand2', activebackground=colors['accent'], relief=RAISED, command=self.helpWindow)
        self.helpBtn.pack(side=BOTTOM, pady=20)
    # Clock Function
    def updateTime(self):
        self.day_label.config(text=strftime("%A"))
        self.date_label.config(text=strftime("%B %d, %Y"))
        self.time_label.config(text=strftime("%I:%M:%S %p"))
        self.afterId = self.window.after(1000, self.updateTime) # Update every 1 second
    # Display Create New Account Window
    def newAcc(self):
        self.new_window = Toplevel(self.window)
        self.app = newAcc(self.new_window)
    # Display HELP WINDOW
    def helpWindow(self):
        self.helpWind = Toplevel(self.window)
        self.app = Help(self.helpWind)
    # Login Function
    def login(self):
        username = self.username.get()
        password = self.password.get()
        userData, userExists = climateDatabase.checkAccount(username, password)
        if username == 'Username' or password == 'Password' or not username or not password:
            messagebox.showerror("Invalid Input", "PLEASE ENTER BOTH USERNAME AND PASSWORD")
        elif userData:
            messagebox.showinfo("Success!", f"Log In Succesfully!\n\nWelcome Back {username}!")
            self.window.after_cancel(self.afterId) # Stop the auto update clock function
            self.window.destroy()
            main_window = Tk()
            Climate(main_window, userData) # Pass userData to Climate class
            main_window.mainloop()
        else:
            messagebox.showerror("Invalid Input", "INVALID USERNAME OR PASSWORD!")

# New Account Window
class newAcc:
    def __init__(self, window):
        self.window = window
        self.window.title("Sign Up Form")
        self.window.geometry("450x450+500+150")
        self.window.resizable(0, 0)
        self.window.config(bg=colors['secondary'])
        # Sign Up Form Text
        self.signFrame = LabelFrame(self.window, text='Sign Up Form', font='Helvetica 24 bold', bg=colors['primary'], bd=3)
        self.signFrame.place(relx=.5, rely=.5, relwidth=.9, relheight=.9, anchor=CENTER)
        Label(self.signFrame, text='Create New Account', font='Helvetica 20 bold', bg=colors['accent']).pack(pady=10)
        # Full Name Input Fields
        self.realnameFrame = LabelFrame(self.signFrame, text='Real name', font='Helvetica 8 bold', bg=colors['accent'], relief=GROOVE)
        self.realnameFrame.pack()
        self.realname = Entry(self.realnameFrame, width=25, bg=colors['accent'], fg=colors['gray'], font='Helvetica 18 bold', bd=0)
        self.realname.pack()
        # Username Input Fields
        self.newUsername = Entry(self.signFrame, width=25, bg=colors['accent'], fg=colors['gray'], font='Helvetica 18 bold', relief=RAISED)
        self.newUsername.pack(pady=10)
        self.newUsername.insert(0, 'Username')
        self.newUsername.bind('<FocusIn>', lambda event: self.newUsername.delete(0, END) if self.newUsername.get() == 'Username' else None)
        self.newUsername.bind('<FocusOut>', lambda event: self.newUsername.insert(0, 'Username') if not self.newUsername.get() else None)
        # Password Input Fields
        self.newPassword = Entry(self.signFrame, width=25, bg=colors['accent'], fg=colors['gray'], font='Helvetica 18 bold', relief=RAISED, show='*')
        self.newPassword.pack(pady=10)
        self.newPassword.insert(0, 'Password')
        self.newPassword.bind('<FocusIn>', lambda event: self.newPassword.delete(0, END) if self.newPassword.get() == 'Password' else None)
        self.newPassword.bind('<FocusOut>', lambda event: self.newPassword.insert(0, 'Password') if not self.newPassword.get() else None)
        # Eye Image
        self.hideImage = PhotoImage(file='hide.png') # Hide eye Icon Image
        self.showImage = PhotoImage(file='show.png') # Show eye Icon Image
        # Eye Icon Button
        self.showButton = Button(self.newPassword, image=self.hideImage, bd=0, bg=colors['accent'], activebackground=colors['accent'], cursor='hand2', pady=5)
        self.showButton.bind('<ButtonPress-1>', lambda event: (self.newPassword.config(show=''), self.showButton.config(image=self.showImage)))
        self.showButton.bind('<ButtonRelease-1>', lambda event: (self.newPassword.config(show='*'), self.showButton.config(image=self.hideImage)))
        self.showButton.place(relx=.98, rely=.5, anchor=E)
        # Sign Up Button
        Button(self.signFrame, width=25, text='Sign Up', bg=colors['accent'], activebackground=colors['secondary'], cursor='hand2', relief=RAISED, command=self.addAcc).pack(side=BOTTOM, pady=(20,40))
        Label(self.signFrame, text='By Signing Up', font='Arial 12').pack(side=BOTTOM)
    # Function to add inputted values to database
    def addAcc(self):
        realname = self.realname.get()
        username = self.newUsername.get()
        password = self.newPassword.get()
        userData, userExists = climateDatabase.checkAccount(username, password)
        if userExists: # Check if username already exist
            messagebox.showerror("Invalid Input!", "USERNAME ALREADY EXIST!")
            self.window.deiconify()
        elif username == 'Username' or password == 'Password' or not realname or not username or not password:
            messagebox.showerror("Invalid Input", "PLEASE ENTER ALL TEXT FIELD REQURIED!")
            self.window.deiconify() 
        elif len(username) > 12 or len(realname) > 12: # Check if username or realname is more than 12 characters
            messagebox.showerror("Invalid Input!", "YOUR USERNAME OR REAL NAME CAN'T BE MORE THAN 12 CHARACTERS!")
            self.window.deiconify()
        elif ' ' in username: # Check is username has spaces
            messagebox.showerror("Invalid Input!", "YOUR USERNAME CAN't CONTAIN SPACES!")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to Create your Account?'):
                climateDatabase.addNew(username, password, realname)
                messagebox.showinfo("Success!", f"Account {username} has been successfully created!")
                self.window.destroy()
            else: 
                messagebox.showerror('Cancelled', 'YOU FAILED TO CREATE YOUR ACCOUNT!')
                self.window.deiconify()

# Main Window
class Climate:
    def __init__(self, window, userData):
        self.window = window
        self.window.title("Climate Learning and Informative Management for Atmospheric Typhoons and Events | Developed By: Chester Paul D. Dela Cruz") # Title of the window
        self.window.geometry("1250x650+10+10") # size of the window
        self.window.config(bg=colors['background']) # background color of the window
        self.window.resizable(0, 0) # cannot resize window
        # Fetch the username and fullname that sucesfully log in
        self.userData = userData
        # Navigation menu Frame
        self.leftFrame = Frame(self.window, bg=colors['primary'])
        self.leftFrame.pack(side=LEFT, fill=Y, padx=(0, 20))
        # Right Frame
        self.rightFrame = Frame(self.window, bg=colors['background'], bd=0, relief=RIDGE)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 20), pady=10)
        # ====================================== NAVIGATION MENU ======================================
        Label(self.leftFrame, text='CLIMATE', font='Arial 20 bold', bg=colors['accent']).pack(fill=X)
        # Profile who Logged In
        self.profile = PhotoImage(file='profile.png')
        Label(self.leftFrame, image=self.profile, bg=colors['primary'], width=100, height=100, bd=0).pack(pady=10)
        Label(self.leftFrame, text=self.userData[3], font='Arial 12 bold', bg=colors['primary']).pack()
        Label(self.leftFrame, text=self.userData[1], font='Arial 10', bg=colors['primary']).pack()
        # Home Button
        self.homeButton = Button(self.leftFrame, text='HOME', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.home)
        self.homeButton.pack(pady=(15,0))
        # Aritcle Button
        self.articleButton = Button(self.leftFrame, text='ARTICLE', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.article)
        self.articleButton.pack(pady=5)
        # Typhoon Button
        self.typhoonButton = Button(self.leftFrame, text='TYPHOON', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.typhoon)
        self.typhoonButton.pack(pady=5)
        # Calculator Button
        self.calculatorButton = Button(self.leftFrame, text='CALCULATOR', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.calculator)
        self.calculatorButton.pack(pady=5)
        # Time
        self.time_label = Label(self.leftFrame, font="Verdana 16", bg=colors['accent'], relief=GROOVE, bd=4) # time
        self.time_label.pack(padx=5, pady=(20, 0))
        self.updateTime() # Clock Function
        # Log Out button
        self.logOutButton = Button(self.leftFrame, text='LOG OUT', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.logOut)
        self.logOutButton.pack(side=BOTTOM, pady=(5, 10))
        # Help Button
        self.helpButton = Button(self.leftFrame, text='HELP', bg=colors['primary'], width=15, activebackground=colors['accent'], 
                                    cursor='hand2', bd=0, font='Arial 10', anchor=W, padx=5, pady=5, relief=GROOVE, command=self.helpInfo)
        self.helpButton.pack(side=BOTTOM)
        # Home Function
        self.home()
    # Function to change button colors and clear widgets on the right frame when clicked
    def buttonClick(self):
        for widget in self.leftFrame.winfo_children(): # Iterate through all children of the parent widget
            if isinstance(widget, Button): # Check if the widget is a button
                if widget.cget("bg") == colors['accent']:  # Check if the button's background
                    widget.config(bg=colors['primary']) # Change the background color to the new color
        for widget in self.rightFrame.winfo_children(): # Iterate through all children of the parent widget
            widget.destroy() # Destroy all widgets
    # Clock Function
    def updateTime(self):
        self.time_label.config(text=strftime("%I:%M:%S %p"))
        self.after_id = self.window.after(1000, self.updateTime) # Update every 1 second
    # ========================================= Home Function =========================================
    def home(self):
        self.buttonClick()
        self.homeButton.config(bg=colors['accent'])
        data = climateDatabase.count()
        def showUser():
            user = climateDatabase.showUser()
            if not user:
                messagebox.showerror("No Users Found", "NO USERS FOUND")
                return
            length = len(user)
            user_list = "\n".join([user[0] for user in user]) # Loop through usernames
            messagebox.showinfo("User List", f"There are currently {length} usernames\n\n{user_list}")
        # Climate Title
        self.climate = "Climate Learning and Informative Management for Atmospheric Typhoons and Events" 
        self.homeTop = Frame(self.rightFrame, bg=colors['primary'], bd=5, relief=GROOVE)
        self.homeTop.pack(fill=X, pady=(10, 0))
        Label(self.homeTop, font='Arial 18 bold', text=self.climate, bg=colors['primary']).pack()
        # Info Frame
        self.infoFrame = Frame(self.rightFrame, bg=colors['secondary'], bd=5, relief=GROOVE)
        self.infoFrame.place(relx=0, rely=.31, relwidth=.43, relheight=.4, anchor=W)
        Label(self.infoFrame, text="CLIMATE", font='Arial 16 bold', bg=colors['secondary']).pack(padx=5, pady=(5, 0), anchor=CENTER)
        self.infoLabel = Label(self.infoFrame, font='Arial 9', bg=colors['secondary'], justify='center',
            text=("CLIMATE is an educational and interactive system designed to help\n"
                    "users understand the impacts of climate change, with a specific focus on\n"
                    "typhoons. It is a informative system and a user friendly interface with several\n"
                    "features enabling users to explore comprehensive data about typhoons and\n"
                    "their relation to global climate trends. It provides access to a organized\n"
                    "collection of articles on typhoons (from past, current, or future typhoons)\n"
                    "and includes an interactive typhoon database. Users can explore detailed\n"
                    "information about various typhoons, including their names, years, affected\n"
                    "areas, and wind speeds. It has a wind speed calculator that estimates the\n"
                    "strength of a typhoon based on user input using common typhoon\n" 
                    "classification scales like the Saffir-Simpson scale."))
        self.infoLabel.pack(pady=10)
        # User Info Frame
        self.userFrame = Frame(self.rightFrame, bg=colors['secondary'], bd=5, relief=GROOVE)
        self.userFrame.place(relx=0, rely=.63, relwidth=.43, relheight=.2, anchor=W)
        Label(self.userFrame, text=f"Welcome Back {self.userData[3]}!", bg=colors['secondary'], font='Arial 16 bold').pack()
        Label(self.userFrame, text=f"User ID: {self.userData[0]}", bg=colors['secondary'], font='Arial 12').pack(anchor=W)
        Label(self.userFrame, text=f"Username: {self.userData[1]}", bg=colors['secondary'], font='Arial 12').pack(anchor=W)
        Label(self.userFrame, text=f"User Created Date: {self.userData[4]}", bg=colors['secondary'], font='Arial 12').pack(anchor=W)
        # TIme Widget
        self.timeDisplay = Frame(self.rightFrame, bg=colors['primary'], bd=5, relief=GROOVE)
        self.timeDisplay.place(relx=0, rely=.86, relwidth=.43, relheight=.2, anchor=W)
        Label(self.timeDisplay, text="TODAY IS", bg=colors['primary'], font='Arial 20 bold').pack()
        Label(self.timeDisplay, text=strftime("%A, %d %B"), bg=colors['primary'], font='Arial 26 bold').pack()
        # User Count Frame
        self.userCount = Frame(self.rightFrame, bg=colors['accent'], bd=5, relief=GROOVE)
        self.userCount.place(relx=.72, rely=.31, relwidth=.25, relheight=.35, anchor=E)
        Button(self.userCount, text=f"{data[0]} USERS", font='Arial 20 bold', bg=colors['accent'], bd=0, cursor='hand2', command=showUser).pack(fill=BOTH, expand=True)
        # Article Frame
        self.articleCount = Frame(self.rightFrame, bg=colors['accent'], bd=5, relief=GROOVE)
        self.articleCount.place(relx=1, rely=.31, relwidth=.25, relheight=.35, anchor=E)
        Button(self.articleCount, text=f"{data[1]} ARTICLES", font='Arial 20 bold', bg=colors['accent'], bd=0, cursor='hand2', command=self.article).pack(fill=BOTH, expand=True)
        # Tyhoon Frame
        self.typhoonCount = Frame(self.rightFrame, bg=colors['accent'], bd=5, relief=GROOVE)
        self.typhoonCount.place(relx=.72, rely=.77, relwidth=.25, relheight=.35, anchor=E)
        Button(self.typhoonCount, text=f"{data[2]} TYPHOONS", font='Arial 20 bold', bg=colors['accent'], bd=0, cursor='hand2', command=self.typhoon).pack(fill=BOTH, expand=True)
        # Article Bookmark Frame
        self.bookmarkCount = Frame(self.rightFrame, bg=colors['accent'], bd=5, relief=GROOVE)
        self.bookmarkCount.place(relx=1, rely=.77, relwidth=.25, relheight=.35, anchor=E)
        Button(self.bookmarkCount, text=f"{data[3]} BOOKMARKS", font='Arial 20 bold', bg=colors['accent'], bd=0, cursor='hand2', command=self.article).pack(fill=BOTH, expand=True)
    # ========================================= Article Function ========================================= 
    def article(self):  
        self.buttonClick()
        self.articleButton.config(bg=colors['accent'])
        # Add bookmark function
        def addBookmark(article_id, user_id):
            if climateDatabase.isArticleBookmarked(article_id):
                messagebox.showerror("Invalid Input!", "BOOKMARK ALREADY EXIST")
            elif messagebox.askyesno('Confirmation', 'Are you sure you want to BOOKMARK this ARTICLE?'):
                climateDatabase.addArticleBookMark(article_id, user_id)
                messagebox.showinfo("Success!", "Successfully BOOKMARKED the ARTICLE!")
                self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO ADD BOOKMARK')
        # Remove bookmark function
        def removeBookMark(bookmark_id):
            if messagebox.askyesno('Confirmation','Are you sure you want to REMOVE this bookmark?'):
                climateDatabase.removeArticleBookmark(bookmark_id)
                messagebox.showinfo("Success!", "Duccesfully REMOVE the bookmark")
                self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE BOOKMARK')
        # Populate Article
        def populateArticle():
            if climateDatabase.selectArticle():
                messagebox.showerror("Invalid!", "YOU CAN ONLY ADD ARTICLES WHEN IT IS EMPTY !!!")
            elif messagebox.askyesno('Confirmation','Are you sure you want to add 20 Articles?'):
                messagebox.showinfo("Success!", "Succesfully added the Article with 20 articles!")
                climateDatabase.populateArticle()
                self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO ADD 20 ARTICLES')
        # Delete all Article
        def deleteAll():
            if messagebox.askyesno('Confirmation','Are you sure you want to REMOVE ALL the ARTICLE?'):
                if not climateDatabase.selectArticle():
                    messagebox.showerror("Invalid!", "NO ARTICLE FOUND")
                else:
                    climateDatabase.deleteAll()
                    messagebox.showinfo("Success!", "Succesfully REMOVE all the ARTICLE")
                    self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE ALL ARTICLE')
        # delete all bookmark
        def deleteAllBookmark():
            if messagebox.askyesno('Confirmation','Are you sure you want to ALL the BOOKMARK?'):
                if not climateDatabase.selectArticleBookmark():
                    messagebox.showerror("Invalid!", "NO BOOKMARK FOUND")
                else:
                    climateDatabase.deleteAllBookmark()
                    messagebox.showinfo("Success!", "Succesfully remove the all the BOOKMARK")
                    self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE ALL BOOKMARK')
        # Bookmark Article
        def bookmarkArticle():  
            bookmark = climateDatabase.selectArticleBookmark()
            if bookmark:
                for i, row in enumerate(bookmark):
                    gridRow = i // 2
                    gridCol = i % 2 # Alternates between column 0 and 1
                    bookmarkFrame = Frame(self.bookmarkScroll, bd=5, relief=GROOVE)
                    bookmarkFrame.grid(row=gridRow, column=gridCol, sticky=NW, padx=35, pady=(20, 0))
                    # Left table for the title
                    titleLabel = Label(bookmarkFrame, text=row[1], font="Arial 12 bold", wraplength=385, anchor=CENTER, width=43)
                    titleLabel.pack()
                    # Article ID (UPPER LEFT)
                    idBookmark = Label(bookmarkFrame, text=row[0], font='Arial 8 bold')
                    idBookmark.place(x=0, y=0)
                    # Bookmarked ID (UPPER RIGHT)
                    idBookmark = Label(bookmarkFrame, text=row[4], font='Arial 8 bold')
                    idBookmark.place(relx=1, rely=0, anchor=NE)
                    # Wrapped Content
                    articleContent = Label(bookmarkFrame, text=row[2], font="Arial 12", wraplength=385, justify=LEFT, width=43)
                    articleContent.pack()
                    # User who Post it (BOTTOM LEFT)
                    userPost = Label(bookmarkFrame, text=f"POSTED BY: {row[6]} AT {row[3]}", font='Arial 6 bold')
                    userPost.place(relx=0, rely=1, anchor=SW)
                    # User who Bookmark it (BOTTOM RIGHT)
                    userPost = Label(bookmarkFrame, text=f"BOOKMARKED BY: {row[6]} AT {row[5]}", font='Arial 6 bold')
                    userPost.place(relx=1, rely=1, anchor=SE)
                    # Remove Bookmark
                    removeBookmarkButton = Button(bookmarkFrame, text='Remove Bookmark', bg=colors['accent'], cursor= 'hand2', relief=RAISED, command=lambda bookmark_id=row[4]: removeBookMark(bookmark_id))
                    removeBookmarkButton.pack(pady=(10, 25))
            else:
                noBookmark = Label(self.bookmarkScroll, text="BOOKMARK IS EMPTY", bg=colors['secondary'], font="Arial 32 bold")
                noBookmark.grid(row=6, column=0, pady=10, ipadx=350, ipady=60)
        # Display Article
        def displayArticle():
            data = climateDatabase.selectArticle()
            if data:
                for i, row in enumerate(data):
                    gridRow = i // 2
                    gridCol = i % 2 # Alternates between column 0 and 1
                    # Create a new frame for each row
                    articleFrame = Frame(self.contentFrame, bd=5, relief=GROOVE)
                    articleFrame.grid(row=gridRow, column=gridCol, sticky=NW, padx=35, pady=(20, 0))
                    # Left table for the title
                    titleLabel = Label(articleFrame, text=row[1], font="Arial 12 bold", wraplength=385, anchor=CENTER, width=43)
                    titleLabel.pack()
                    # Article ID
                    idArticle = Label(articleFrame, text=row[0], font='Arial 8 bold')
                    idArticle.place(x=0, y=0)
                    # Wrapped Content
                    articleContent = Label(articleFrame, text=row[2], font="Arial 12", wraplength=385, justify=LEFT, width=43)
                    articleContent.pack()
                    # User who Post it
                    userPost = Label(articleFrame, text=f"POSTED BY: {row[4]} AT {row[3]}", font='Arial 8 bold')
                    userPost.place(relx=1.0, rely=1.0, anchor=SE)
                    # Bookmark Button
                    bookmarkButton = Button(articleFrame, text='BOOKMARK', relief=RAISED, bg=colors['accent'], cursor= 'hand2',
                                            command=lambda article_id=row[0], user_id=self.userData[0]: addBookmark(article_id, user_id))
                    bookmarkButton.pack(side=BOTTOM, pady=(10, 25))
            else:
                noArticle = Label(self.contentFrame, text="ARTICLE IS EMPTY", bg=colors['secondary'], font="Arial 32 bold")  
                noArticle.grid(row=0, column=0, pady=10, ipadx=350, ipady=50)
        # Bookmark Frame
        self.bookmarkFrame = Frame(self.rightFrame, bg=colors['background'])
        self.bookmarkFrame.pack(fill=X)
        self.bookmarkTop = Frame(self.bookmarkFrame, bg=colors['primary'], bd=5, relief=GROOVE)
        self.bookmarkTop.pack(fill=X)
        Label(self.bookmarkTop, font='Arial 20 bold', text='BOOKMARK', bg=colors['primary'], justify=CENTER).pack(side=LEFT, padx=(441, 0), pady=10)
        Button(self.bookmarkTop, font='Arial 16 bold', text='❌DELETE', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=deleteAllBookmark).pack(side=RIGHT, padx=20)
        # Articles Frame Section
        self.articleFrame = Frame(self.rightFrame, bg=colors['background'])
        self.articleFrame.pack(fill=X)
        self.aritcleTop = Frame(self.articleFrame, bg=colors['primary'], bd=5, relief=GROOVE)
        self.aritcleTop.pack(fill=X)
        Label(self.aritcleTop, font='Arial 20 bold', text='ARTICLE', bg=colors['primary'], justify=CENTER).pack(side=LEFT, padx=(462, 0), pady=10)
        Button(self.aritcleTop, font='Arial 16 bold', text='📌EDIT', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=self.editArticle).pack(side=RIGHT, padx=20)
        Button(self.aritcleTop, font='Arial 16 bold', text='❌DELETE', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=deleteAll).pack(side=RIGHT)
        Button(self.aritcleTop, font='Arial 16 bold', text='➕ADD', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=populateArticle).pack(side=RIGHT, padx=20)
        # ============================================= Scrollbar Function =============================================
        # Canvas
        self.articleCanvas = Canvas(self.articleFrame, height=360, bg=colors['background'])
        self.articleCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.bookmarkCanvas = Canvas(self.bookmarkFrame, height=200, bg=colors['background'])
        self.bookmarkCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        # # Scrollbar
        self.scrollbar = Scrollbar(self.articleFrame, orient=VERTICAL, command=self.articleCanvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scroll = Scrollbar(self.bookmarkFrame, orient=VERTICAL, command=self.bookmarkCanvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.articleCanvas.configure(yscrollcommand=self.scrollbar.set)
        self.bookmarkCanvas.configure(yscrollcommand=self.scroll.set)
        # Frame inside Canvas for content
        self.contentFrame = Frame(self.articleCanvas, bg=colors['background'])
        self.articleCanvas.create_window((0, 0), window=self.contentFrame, anchor='nw')
        self.contentFrame.bind("<Configure>", lambda e: self.articleCanvas.configure(scrollregion=self.articleCanvas.bbox("all")))
        self.articleCanvas.pack_propagate(False)
        self.bookmarkScroll = Frame(self.bookmarkCanvas, bg=colors['background'])
        self.bookmarkCanvas.create_window((0, 0), window=self.bookmarkScroll, anchor='nw')
        self.bookmarkScroll.bind("<Configure>", lambda e: self.bookmarkCanvas.configure(scrollregion=self.bookmarkCanvas.bbox("all")))
        self.bookmarkCanvas.pack_propagate(False)
        # Display Article and Bookmark
        displayArticle()
        bookmarkArticle()
    # ========================================= Typhoon Function ========================================= 
    def typhoon(self):
        self.buttonClick()
        self.typhoonButton.config(bg=colors['accent'])
        # Populate Typhoon
        def populateTyphoon():
            if climateDatabase.selectTyphoon():
                messagebox.showerror("Invalid!", "YOU CAN ONLY ADD TYPHOON WHEN IT IS EMPTY !!!")
            elif messagebox.askyesno('Confirmation','Are you sure you want to add 10 Typhoons from database?'):
                messagebox.showinfo("Success!", "Succesfully added the typhoon with 20 typhoon!")
                climateDatabase.populateTyphoon()
                self.article()
            else: messagebox.showwarning('Cancelled', 'FAILED TO ADD 20 TYPHOONS')
        # Display Typhoon
        def displayTyphoon(typhoonData):
            if typhoonData:
                for i, row in enumerate(typhoonData):
                    gridRow = i // 2
                    gridCol = i % 2 # Alternates between column 0 and 1
                    # Create a new frame for each row
                    typhoonFrame = Frame(self.typhoonScrollbar, bd=5, relief=GROOVE)
                    typhoonFrame.grid(row=gridRow, column=gridCol, sticky=NW, padx=35, pady=(20, 0))
                    # Typhoon Name
                    nameLabel = Label(typhoonFrame, text=f"Typhoon name\t: {row[1]}", font="Arial 12 bold", width=38, anchor="w")
                    nameLabel.grid(row=0, column=0, sticky="w", padx=30)
                    # Typhoon ID (UPPER LEFT)
                    idTyphoon = Label(typhoonFrame, text=row[0], font='Arial 8 bold')
                    idTyphoon.place(relx=0, rely=0, anchor=NW)
                    # Typhoon year
                    yearLabel = Label(typhoonFrame, text=f"Year Occurred\t: {row[2]}", font="Arial 12", width=38, anchor="w")
                    yearLabel.grid(row=1, column=0, sticky="w", padx=30)
                    # Typhoon Affected Areas
                    affectedLabel = Label(typhoonFrame, text=f"Affected Areas\t: {row[3]}", font="Arial 12", width=38, anchor="w")
                    affectedLabel.grid(row=2, column=0, sticky="w", padx=30)
                    # Typhoon Wind Speed
                    speedLabel = Label(typhoonFrame, text=f"Wind Speed\t: {row[4]}", font="Arial 12", width=38, anchor="w")
                    speedLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 30))
                    # User who Post it (BOTTOM LEFT)
                    userPost = Label(typhoonFrame, text=f"POSTED BY: {row[6]} AT {row[5]}", font='Arial 8 bold')
                    userPost.place(relx=1, rely=1, anchor=SE)
            else:
                noArticle = Label(self.typhoonScrollbar, text="TYPHOON IS EMPTY.", bg=colors['secondary'], font="Arial 32 bold")
                noArticle.grid(row=0, column=0, pady=10, ipadx=350, ipady=50)
        # Delete ALL TYPHOON BUTTON
        def deleteAllTyphoon():
            if messagebox.askyesno('Confirmation','Are you sure you want to ALL the TYPHOON?'):
                climateDatabase.deleteAllTyphoon()
                messagebox.showinfo("Success!", "Succesfully REMOVE the ALL the TYPHOONS")
                self.typhoon()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE ALL THE TYPHOON')
        # Filter Typhoon Function based on key release
        def filterTyphoon(event):
            search_query = self.search.get().strip()
            # Query the database for typhoons starting with the search query
            typhoonData = climateDatabase.selectTyphoon(search_query)
            # Clear existing displayed typhoons
            for widget in self.typhoonScrollbar.winfo_children():
                widget.destroy()
            displayTyphoon(typhoonData)
        # List of Typhoons
        self.typhoonFrame = Frame(self.rightFrame, bg=colors['primary'])
        self.typhoonFrame.pack(fill=BOTH, expand=True)
        self.typhoonTop = Frame(self.typhoonFrame, bg=colors['primary'], bd=5, relief=GROOVE)
        self.typhoonTop.pack(fill=X)
        Label(self.typhoonTop, font='Arial 20 bold', text='TYPHOONS', bg=colors['primary']).pack(side=LEFT, padx=(440, 0), pady=(5, 10))
        Button(self.typhoonTop, font='Arial 16 bold', text='📌EDIT', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=self.editTyphoon).pack(side=RIGHT, padx=20)
        Button(self.typhoonTop, font='Arial 16 bold', text='❌DELETE', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=deleteAllTyphoon).pack(side=RIGHT)
        Button(self.typhoonTop, font='Arial 16 bold', text='➕ADD', bd=3, cursor='hand2', bg=colors['accent'], activebackground=colors['secondary'], relief=RAISED, command=populateTyphoon).pack(side=RIGHT, padx=20)
        # Filter Search Typhoons
        self.search = Entry(self.typhoonTop, font='Arial 16', bd=0)
        self.search.place(relx=.01, rely=.2)
        self.search.insert(0, 'Search Typhoon Names')
        self.search.bind('<FocusIn>', lambda event: self.search.delete(0, END) if self.search.get() == 'Search Typhoon Names' else None)
        self.search.bind('<FocusOut>', lambda event: self.search.insert(0, 'Search Typhoon Names') if not self.search.get() else None)
        self.search.bind("<KeyRelease>", filterTyphoon) # search filter on key release
        # ============================================= Scrollbar Function =============================================
        # # Canvas
        self.typhoonCanvas = Canvas(self.typhoonFrame, bg=colors['background'])
        self.typhoonCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        # # Scrollbar
        self.scrollbar = Scrollbar(self.typhoonFrame, orient=VERTICAL, command=self.typhoonCanvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.typhoonCanvas.configure(yscrollcommand=self.scrollbar.set)
        # # Frame inside canvas for content
        self.typhoonScrollbar = Frame(self.typhoonCanvas, bg=colors['background'])
        self.typhoonCanvas.create_window((0, 0), window=self.typhoonScrollbar, anchor=NW)
        self.typhoonScrollbar.bind("<Configure>", lambda e: self.typhoonCanvas.configure(scrollregion=self.typhoonCanvas.bbox("all")))
        # Display all typhoons
        displayTyphoon(climateDatabase.selectTyphoon())
    # ========================================= Calculator Function ========================================= 
    def calculator(self):
        self.buttonClick()
        self.calculatorButton.config(bg=colors['accent'])
        def convertSpeed(): #Convert Wind Speed
            try:
                speed = float(self.userInput.get())  # Get the input wind speed
                unit = self.unit.get()  # Get the selected input unit
                # Perform conversions based on the selected unit
                if unit == "mph":
                    mph = speed
                    knots = mph * 0.868976
                    mps = mph * 0.44704
                    fps = mph * 1.46667
                    kmh = mph * 1.60934
                elif unit == "knots":
                    knots = speed
                    mph = knots / 0.868976
                    mps = knots * 0.514444
                    fps = knots * 1.68781
                    kmh = knots * 1.852
                elif unit == "mps":
                    mps = speed
                    mph = mps / 0.44704
                    knots = mps / 0.514444
                    fps = mps * 3.28084
                    kmh = mps * 3.6
                elif unit == "fps":
                    fps = speed
                    mph = fps / 1.46667
                    knots = fps / 1.68781
                    mps = fps / 3.28084
                    kmh = fps * 1.09728
                elif unit == "kmh":
                    kmh = speed
                    mph = kmh / 1.60934
                    knots = kmh / 1.852
                    mps = kmh / 3.6
                    fps = kmh / 1.09728
                if (mph >= 157 or knots >=137 or mps >= 70 or kmh >= 252 or fps >= 230): category = "Category 5 - Catastrophic"
                elif (mph >= 130 or knots >= 113 or mps >= 58 or kmh >= 209 or fps >= 190): category = "Category 4 - Devastating"
                elif (mph >= 111 or knots >= 96 or mps >= 50 or kmh >= 178 or fps >= 162): category = "Category 3 - Major Hurricane"
                elif (mph >= 96 or knots >= 83 or mps >= 43 or kmh >= 154 or fps >= 140): category = "Category 2 - Extensive Damage"
                elif (mph >= 74 or knots >= 64 or mps >= 33 or kmh >= 119 or fps >= 108): category = "Category 1 - Minimal Damage"
                else: category = "Tropical Storm or Lower"
                # Display converted values
                self.resultLabel.config(text=f"Wind Speed\t: {speed:.2f} {unit}\n\n"
                                            f"Mph\t\t: {mph:.2f} mph\n"
                                            f"Knots\t\t: {knots:.2f} knots\n"
                                            f"M/s\t\t: {mps:.2f} m/s\n"
                                            f"Ft/s\t\t: {fps:.2f} ft/s\n"
                                            f"Km/h\t\t: {kmh:.2f} km/h\n"
                                            f"Category\t\t: {category} ")
            except ValueError: self.resultLabel.config(text="Invalid input! Please enter a valid number.")
        # Determine the Saffir-Simpson category based on wind speed
        def updateCategory(windSpeed):
            if windSpeed >= 157: category = "Category 5 - Catastrophic"
            elif windSpeed >= 130: category = "Category 4 - Devastating"
            elif windSpeed >= 111: category = "Category 3 - Major Hurricane"
            elif windSpeed >= 96: category = "Category 2 - Extensive Damage"
            elif windSpeed >= 74: category = "Category 1 - Minimal Damage"
            else: category = "Tropical Storm or Lower"
            self.resultScale.config(text=f"Wind Speed: {windSpeed} mph\nSaffir-Simpson Category: {category}") # Update Label
        # Label
        Label(self.rightFrame, text='Wind Speed Calculator', font='Verdana 24 bold', bg=colors['primary'], bd=5, relief=GROOVE).pack(ipadx=300)
        # User Input
        self.inputFrame = Frame(self.rightFrame, bg=colors['primary'])
        self.inputFrame.place(relx=.5, rely=.15, relwidth=1, relheight=.1, anchor=CENTER)
        Label(self.inputFrame, text='Enter a wind speed:', font='Verdana 16', bg=colors['primary']).place(rely=.5, anchor=W)
        self.userInput = Entry(self.inputFrame, font='Verdana 16')
        self.userInput.place(relx=.23, rely=.5, relwidth=.2, relheight=.6, anchor=W)
        # Dropdown Menu Text
        self.unit = StringVar(value="mph")
        self.unit_label = Label(self.inputFrame, text='Select a Unit:', font='Verdana 16', bg =colors['primary'])
        self.unit_label.place(relx=.6, rely=.5, anchor=E)
        # Dropdown Menu
        self.dropdown = ttk.Combobox(self.inputFrame, font='Verdana 16', textvariable=self.unit, state="readonly")
        self.dropdown["values"] = ("mph", "knots", "mps", "fps", "kmh")
        self.dropdown.place(relx=.8, rely=.5, relwidth=.2, relheight=.6, anchor=E)
        # Convert Button
        self.convertBtn = Button(self.inputFrame, text='Convert', font='Verdana 16', command=convertSpeed)
        self.convertBtn.place(relx=.99, rely=.5, relwidth=.1, anchor=E)
        # Result Frame
        self.resultFrame = Frame(self.rightFrame, bg=colors['secondary'])
        self.resultFrame.place(relx=.5, rely=.45, relwidth=1, relheight=.4, anchor=CENTER)
        self.resultLabel = Label(self.resultFrame, text="", font='Verdana 16', bg=colors['secondary'], justify=LEFT)
        self.resultLabel.place(relx=.5, rely=.5, anchor=CENTER)
        # Scale 
        Label(self.rightFrame, text='Drag the scale to explore wind speeds', font='Arial 24 bold', bg=colors['primary'], bd=5, relief=GROOVE).place(relx=.5, rely=.73, anchor=CENTER)
        self.windScale = Scale(self.rightFrame, from_=0, to=300, orient=HORIZONTAL, length=950, tickinterval=10, command=lambda value: updateCategory(int(value)))
        self.windScale.set(((self.windScale['from']-self.windScale['to'])/2)+self.windScale['to'])
        self.windScale.place(relx=.5, rely=.83, anchor=CENTER)
        self.resultScale = Label(self.rightFrame, text="Wind Speed: 0 mph\nSaffir-Simpson Category: Tropical Storm or Lower", bg=colors['primary'], font='Verdana 12', bd=5, relief=GROOVE)
        self.resultScale.place(relx=.5, rely=.95, anchor=CENTER)
    # ========================================= HELP FUNCTION ========================================= 
    def helpInfo(self):
        self.buttonClick()
        self.helpButton.config(bg=colors['accent'])
        self.new_window = Toplevel(self.window)
        Help(self.new_window)
    # ========================================= LOG OUT FUNCTION ========================================= 
    def logOut(self):
        if messagebox.askyesno('Confirmation','Are you sure you want to log out?'):
            messagebox.showinfo("Success", f"Goodbye {self.userData[1]}!\n\nLog Out Sucessfully!")
            self.window.after_cancel(self.after_id)
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        else: 
            messagebox.showwarning('Cancelled', 'Log Out Failed!')
            self.window.deiconify()
            return
    # ========================================= ARTICLE WINDOW ========================================= 
    def editArticle(self):
        self.new_window = Toplevel(self.window)
        Article(self.new_window, self.userData)
    # ========================================= TYPHOON WINDOW ========================================= 
    def editTyphoon(self):
        self.new_window = Toplevel(self.window)
        Typhoon(self.new_window, self.userData)

# Edit Article Window
class Article():
    def __init__(self, window, userData):
        self.window = window
        self.window.geometry("500x550+600+80") # size of the window
        self.window.config(bg=colors['primary']) # background color of the window
        self.window.overrideredirect(True) # User not able to move the window
        # User Data
        self.userData = userData  # Store userData
        # Input Fields
        self.title = Entry(self.window, width=67)
        self.title.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.content = Text(self.window, width=50, height=10)
        self.content.grid(row=4, column=0, padx=20, pady=10)
        self.selectId = Entry(self.window, width=30)
        self.selectId.insert(0, 'Select ID to Delete or Edit')
        self.selectId.bind('<FocusIn>', lambda event: self.selectId.delete(0, END) if self.selectId.get() == 'Select ID to Delete or Edit' else None)
        self.selectId.bind('<FocusOut>', lambda event: self.selectId.insert(0, 'Select ID to Delete or Edit') if not self.selectId.get() else None)
        self.selectId.grid(row=7, column=0, pady=5)
        # Text Labels
        Label(self.window, text='Editing Articles...', font='Verdana 20 bold', bg=colors['accent']).grid(row=0, column=0, ipadx=120)
        self.titleLabel = Label(self.window, text='Article Title', font='Verdana 16 bold')
        self.titleLabel.grid(row=1, column=0, pady=(10, 0))
        self.contentLabel = Label(self.window, text='Article Content', font='Verdana 16 bold')
        self.contentLabel.grid(row=3, column=0, pady=(10, 0))
        # Submit Button
        self.submitBtn = Button(self.window, text='ADD ARTICLE', width=30, command=self.addArticle)
        self.submitBtn.grid(row=6, column=0, pady=10)
        # Delete Button
        self.deleteBtn = Button(self.window, text="DELETE ARTICLE", width=30, command=self.deleteArticle)
        self.deleteBtn.grid(row=8, column=0, pady=10)
        # Update Button
        self.editBtn = Button(self.window, text="EDIT ARTICLE", width=30, command=self.updateArticle)
        self.editBtn.grid(row=9, column=0, pady=10)
        # Exit BUtton
        self.exitBtn = Button(self.window, text="EXIT ARTICLE", width=30, command=self.exitArticle)
        self.exitBtn.grid(row=10, column=0, pady=10)
    # ================================================ ADD ARTICLE ================================================
    def addArticle(self):
        title = self.title.get()
        content = self.content.get("1.0", END).strip()
        if not title or not content:
            messagebox.showerror("Invalid Input!", "PLEASE FILL IN THE TEXT REQUIRED!")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to ADD this ARTICLE?'):
                climateDatabase.addArticle(self.userData[0], title, content)
                messagebox.showinfo("Success!", "Article Added Succesfully")
                self.window.destroy()
            else: 
                messagebox.showwarning('Cancelled', 'FAILED TO ADD AN ARTICLE')
                self.window.deiconify()
    # ================================================ DELETE ARTICLE ================================================
    def deleteArticle(self):
        article_id = self.selectId.get().strip()
        if not climateDatabase.searchArticle(article_id):
            messagebox.showerror("Invalid Input!", "ID NOT FOUND\n\nID IS LOCATED IN THE UPPER LEFT OF EACH ARTICLE")
            self.window.deiconify()
        elif not article_id.isdigit():
            messagebox.showerror("Invalid Input!", "ID MUST BE NUMERIC VALUE")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to DELETE this ARTICLE?'):
                climateDatabase.deleteArticle(article_id)
                messagebox.showinfo("Success!", "Article Deleted Succesfully")
                self.window.destroy()
            else: 
                messagebox.showwarning('Cancelled', 'FAILED TO DELETE ARTICLE')
                self.window.deiconify()
    # ================================================ UPDATE ARTICLE DATA ================================================
    def updateData(self):
        article_id = self.selectId.get()
        title = self.title.get()
        content = self.content.get("1.0", END).strip()
        if not title or not content or not article_id:
            messagebox.showerror("Invalid Input!", "PLEASE FILL IN THE TEXT REQUIRED")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to update this Article?'):
                climateDatabase.updateArticle(article_id, title, content)
                messagebox.showinfo("Success!", "Article Updated Succesfully")
                self.window.destroy()
            else:
                messagebox.showerror('Cancelled', 'FAILED TO UPDATE ARTICLE')
                self.window.deiconify()
    # ================================================ EDIT ARTICLE ================================================
    def updateArticle(self):
        article_id = self.selectId.get().strip()
        # Cancel Button function returns original state
        def cancel():
            if messagebox.askyesno('Confirmation','Are you sure you want to cancel the edit?'):
                self.submitBtn.config(text="ADD ARTICLE", command=self.addArticle)
                self.editBtn.config(text="EDIT ARTICLE", command=self.updateArticle)
                self.selectId.config(state='normal')
                self.title.delete(0, END)
                self.content.delete("1.0", END)
                self.window.deiconify()
            else: self.window.deiconify()
        if not climateDatabase.searchArticle(article_id):
            messagebox.showerror("Invalid Input!", "ID NOT FOUND\n\nID IS LOCATED IN THE UPPER LEFT OF EACH ARTICLE")
            self.window.deiconify()
        elif not article_id.isdigit():
            messagebox.showerror("Invalid Input!", "ID MUST BE NUNMERIC VALUE")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to EDIT this ARTICLE?'):
                data = climateDatabase.searchArticle(article_id)
                for i, row in enumerate(data):
                    self.title.delete(0, END)
                    self.title.insert(0, row[2])
                    self.content.delete("1.0", END)
                    self.content.insert("1.0", row[3])
                    self.submitBtn.config(text="UPDATE ARTICLE", command=self.updateData)
                    self.selectId.config(state='readonly')
                    self.editBtn.config(text="CANCEL EDIT", command=cancel)
                self.window.deiconify()
            else:
                messagebox.showwarning('Cancelled', 'FAILED TO EDIT THE ARTICLE')
                self.window.deiconify()
    # ================================================ EXIT BUTTON ================================================
    def exitArticle(self):
        if messagebox.askyesno('Confirmation','Are you sure you want to EXIT?'):
            messagebox.showinfo("Success!", "Exit Succesfully!")
            self.window.destroy()
        else: 
            messagebox.showwarning('Cancelled', 'Exit Failed!')
            self.window.deiconify()
            return

# Edit Typhoon Window
class Typhoon():
    def __init__(self, window, userData):
        self.window = window
        self.window.geometry("400x400+600+150") # size of the window
        self.window.config(bg=colors['secondary']) # background color of the window
        self.window.overrideredirect(True) # User not able to move the window
        # User Data
        self.userData = userData  # Store userData
        # 10 limit characters
        def limitEntry(entryText):
            if len(entryText) > 20:
                messagebox.showerror("CHARACTER LIMIT REACHED", "ONLY 20 CHARACTERS ARE ALLOWED!")
                self.window.deiconify()
                return False  # Reject input if longer than 20 characters
            return True
        # Input Fields
        self.name = Entry(self.window, width=30, validate="key", validatecommand=(self.window.register(limitEntry), "%P"))
        self.name.grid(row=1, column=1, padx=20, pady=(10, 0))
        self.year = Entry(self.window, width=30, validate="key", validatecommand=(self.window.register(limitEntry), "%P"))
        self.year.grid(row=2, column=1)
        self.affectedAreas = Entry(self.window, width=30, validate="key", validatecommand=(self.window.register(limitEntry), "%P"))
        self.affectedAreas.grid(row=3, column=1)
        self.windSpeed = Entry(self.window, width=30, validate="key", validatecommand=(self.window.register(limitEntry), "%P"))
        self.windSpeed.grid(row=4, column=1)
        self.selectId = Entry(self.window, width=30)
        self.selectId.grid(row=5, column=1)
        self.selectId.insert(0, 'Select ID to Delete or Edit')
        self.selectId.bind('<FocusIn>', lambda event: self.selectId.delete(0, END) if self.selectId.get() == 'Select ID to Delete or Edit' else None)
        self.selectId.bind('<FocusOut>', lambda event: self.selectId.insert(0, 'Select ID to Delete or Edit') if not self.selectId.get() else None)
        self.selectId.grid(row=7, column=0, columnspan=2, pady=5)
        # Labels
        Label(self.window, text='Editing Typhoons...', font='Verdana 20 bold', bg=colors['primary']).grid(row=0, column=0, columnspan=2, ipadx=55)
        self.name_label = Label(self.window, text="Typhoon Name", bg=colors['secondary'], font='Verdana 14')
        self.name_label.grid(row=1, column=0, pady=(10, 0), sticky=W, padx=15)
        self.year_label = Label(self.window, text="Year Occured", bg=colors['secondary'], font='Verdana 14')
        self.year_label.grid(row=2, column=0, sticky=W, padx=15)
        self.affectedAreas_label = Label(self.window, text="Affected Areas", bg=colors['secondary'], font='Verdana 14')
        self.affectedAreas_label.grid(row=3, column=0, sticky=W, padx=15)
        self.windSpeed_label = Label(self.window, text="Wind Speed", bg=colors['secondary'], font='Verdana 14')
        self.windSpeed_label.grid(row=4, column=0, sticky=W, padx=15)
        # Submit Button
        self.submitBtn = Button(self.window, text='ADD TYPHOON', width=30, command=self.addTyphoon)
        self.submitBtn.grid(row=6, column=0, columnspan=2, pady=10)
        # Delete Button
        self.deleteBtn = Button(self.window, text="DELETE TYPHOON", width=30, command=self.deleteTyphoon)
        self.deleteBtn.grid(row=8, column=0, columnspan=2, pady=10)
        # Update Button
        self.editBtn = Button(self.window, text="EDIT TYPHOON", width=30, command=self.updateTyphoon)
        self.editBtn.grid(row=9, column=0, columnspan=2, pady=10)
        # Exit Button
        self.ExitBtn = Button(self.window, text="EXIT", width=30, command=self.exitTyphoon)
        self.ExitBtn.grid(row=10, column=0, columnspan=2, pady=10)
    # ================================================ ADD TYPHOON ================================================
    def addTyphoon(self):
        name = self.name.get()
        year = self.year.get()
        affected = self.affectedAreas.get()
        speed = self.windSpeed.get()
        if not name or not year or not affected or not speed:
            messagebox.showerror("Invalid Input!", "PLEASE FILL IN THE FIELDS REQUIRED!")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to ADD this TYPHOON?'):
                climateDatabase.addTyphoon(self.userData[0], name, year, affected, speed)
                messagebox.showinfo("Success!", "Typhoon Added Succesfully")
                self.window.destroy()
            else: 
                messagebox.showwarning('Cancelled', 'FAILED TO ADD TYPHOON')
                self.window.deiconify()
    # ================================================ DELETE TYPHOON ================================================
    def deleteTyphoon(self):
        typhoon_id = self.selectId.get().strip()
        if not climateDatabase.searchTyphoon(typhoon_id):
            messagebox.showerror("Invalid Input!", "ID NOT FOUND\n\nID IS LOCATED IN THE UPPER LEFT OF EACH TYPHOON")
            self.window.deiconify()
        elif not typhoon_id.isdigit():
            messagebox.showerror("Invalid Input!", "ID MUST BE NUMERIC VALUE")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to DELETE this TYPHOON?'):
                climateDatabase.deleteTyphoon(typhoon_id)
                messagebox.showinfo("Success!", "Typhoon Deleted Succesfully")
            else:
                messagebox.showwarning('Cancelled', 'FAILED TO DELETE TYPHOON')
                self.window.deiconify()
                return
    # ================================================ UPDATE TYPHOON DATA ================================================
    def updateData(self):
        typhoon_id = self.selectId.get()
        name = self.name.get()
        year = self.year.get()
        affected = self.affectedAreas.get()
        speed = self.windSpeed.get()
        if not name or not year or not affected or not speed or not typhoon_id:
            messagebox.showerror("Invalid Input!", "PLEASE FILL IN THE TEXT REQUIRED")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to UPDATE this TYPHOON?'):
                climateDatabase.updateTyphoon(typhoon_id, name, year, affected, speed)
                messagebox.showinfo("Success!", "TYPHOON Updated Succesfully")
                self.window.destroy()
            else:
                messagebox.showwarning('Cancelled', 'FAILED TO UPDATE TYPHOON')
                self.window.deiconify()
    # ================================================ UPDATE TYPHOON ================================================
    def updateTyphoon(self):
        typhoon_id = self.selectId.get().strip()
        # Cancel Button function returns original state
        def cancel():
            if messagebox.askyesno('Confirmation','Are you sure you want to cancel the edit?'):
                self.submitBtn.config(text="ADD TYPHOON", command=self.addTyphoon)
                self.editBtn.config(text="EDIT TYPHOON", command=self.updateTyphoon)
                self.selectId.config(state='normal')
                self.name.delete(0, END)
                self.year.delete(0, END)
                self.affectedAreas.delete(0, END)
                self.windSpeed.delete(0, END)
                self.window.deiconify()
            else: self.window.deiconify()
        if not climateDatabase.searchTyphoon(typhoon_id):
            messagebox.showerror("Invalid Input!", "ID NOT FOUND")
            self.window.deiconify()
        elif not typhoon_id.isdigit():
            messagebox.showerror("Invalid Input!", "ID MUST BE NUMERIC VALUE")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation','Are you sure you want to edit this Article?'):
                data = climateDatabase.searchTyphoon(typhoon_id)
                for i, row in enumerate(data):
                    self.name.delete(0, END)
                    self.name.insert(0, row[2])
                    self.year.delete(0, END)
                    self.year.insert(0, row[3])
                    self.affectedAreas.delete(0, END)
                    self.affectedAreas.insert(0, row[4])
                    self.windSpeed.delete(0, END)
                    self.windSpeed.insert(0, row[5])
                    self.submitBtn.config(text="UPDATE TYPHOON", command=self.updateData)
                    self.selectId.config(state='readonly')
                    self.editBtn.config(text="CANCEL EDIT", command=cancel)
                self.window.deiconify()
            else:
                messagebox.showwarning('Cancelled', 'FAILED TO EDIT TYPHOON')
                self.window.deiconify()
    # ================================================ EXIT BUTTON ================================================
    def exitTyphoon(self):
        if messagebox.askyesno('Confirmation','Are you sure you want to exit?'):
            self.window.destroy()
        else: 
            messagebox.showwarning('Cancelled', 'EXIT FAILED')
            self.window.deiconify()

# Help Window
class Help():
    def __init__(self, window):
        self.window = window
        self.window.geometry("900x550+300+100") # size of the window
        self.window.config(bg=colors['background']) # background color of the window
        self.window.overrideredirect(True) # User not able to move the window
        # Main Frame
        self.mainFrame = LabelFrame(self.window, font='Arial 20 bold', text='SYSTEM INFORMATION', bg=colors['background'], bd=6, relief=RIDGE)
        self.mainFrame.place(relx=.5, rely=.5, relwidth=.95, relheight=.94, anchor=CENTER)
        # Navigation Menu
        self.navigation = Frame(self.mainFrame, bg=colors['background'])
        self.navigation.pack(side=LEFT, fill=Y, padx=(20, 0), pady=10)
        # Text Info Frame
        self.helpFrame = Frame(self.mainFrame, bg=colors['primary'], bd=0, relief=RIDGE)
        self.helpFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        # ==================================================== BUTTONS ==================================================== 
        # Log In Button
        self.logBtn = Button(self.navigation, text='Log In', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'], command=self.logHelp)
        self.logBtn.pack(padx=10, pady=10, anchor=W)
        # Home Button
        self.homeBtn = Button(self.navigation, text='Home', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'], command=self.home)
        self.homeBtn.pack(padx=10, pady=10, anchor=W)
        # Article Button
        self.articlebtn = Button(self.navigation, text='ARTICLES', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'],  command=self.articleHelp)
        self.articlebtn.pack(padx=10, pady=10, anchor=W)
        # Typhoon Button
        self.Typhoonbtn = Button(self.navigation, text='TYPHOONS', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'],  command=self.typhoonHelp)
        self.Typhoonbtn.pack(padx=10, pady=10, anchor=W)
        # Calculator Button
        self.calculatorbtn = Button(self.navigation, text='CALCULATOR', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'],  command=self.calculatorHelp)
        self.calculatorbtn.pack(padx=10, pady=10, anchor=W)
        # Exit Button
        self.exitbtn = Button(self.navigation, text='EXIT', cursor='hand2', bd=3, padx=5, pady=5, width=12,
                            font='Arial 12', relief=RAISED, bg=colors['accent'],  command=self.exitHelp)
        self.exitbtn.pack(side=BOTTOM, padx=10, pady=10, anchor=W)
        # Help Text
        self.mainLabel = Label(self.helpFrame, font='Arial 16', padx=10, bg=colors['primary'], wraplength=600,
                            text=("===============\n====  USER GUIDE  ====\n===============\n\n"
                                    "Welcome User! Navigate through the buttons on the left to know more about the system!"
                            ))
        self.mainLabel.pack()
    # Button Click
    def navigationClick(self):
        for widget in self.navigation.winfo_children(): # Iterate through all children of the parent widget
            if isinstance(widget, Button): # Check if the widget is a button
                if widget.cget("bg") == colors['primary']:  # Check if the button's background
                    widget.config(bg=colors['accent']) # Change the background color to the new color
        for widget in self.helpFrame.winfo_children(): # Iterate through all children of the parent widget
            widget.destroy() # Destroy all widgets
        # ============================================= Scrollbar Function =============================================
        # # Canvas
        self.helpCanvas = Canvas(self.helpFrame, bg=colors['primary'])
        self.helpCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        # # Scrollbar
        self.scrollbar = Scrollbar(self.helpFrame, orient=VERTICAL, command=self.helpCanvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.helpCanvas.configure(yscrollcommand=self.scrollbar.set)
        # # Frame inside canvas for content
        self.helpScrollbar = Frame(self.helpCanvas, bg=colors['primary'])
        self.helpCanvas.create_window((0, 0), window=self.helpScrollbar, anchor=NW)
        self.helpScrollbar.bind("<Configure>", lambda e: self.helpCanvas.configure(scrollregion=self.helpCanvas.bbox("all")))
    # Log in Button
    def logHelp(self):
        self.navigationClick()
        self.logBtn.config(bg=colors['primary'])
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE,
                            text=("===============\n====  LOG IN PAGE  ====\n===============\n"
                                " The Log in Page is the first thing that will open when you run the system. It is where the user" 
                                " will enter his/her username to log in to the system. The log in is connected to the database"
                                " in which it will check if the inputted username and password correctly matched a data in the"
                                " database before being correctly log in to the main system.\n")).pack(padx=20, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"PLEASE ENTER BOTH USERNAME AND PASSWORD\"\n===============\n "
                                " The user did not input anything and just click submit")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"INVALID USERNAME OR PASSWORD!\"\n===============\n "
                                " If the username and password does not exist or not found in the database")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"Log In Succesfully! Welcome Back (User)\"\n===============\n "
                                " If the username and password succesfully been logged in")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE,
                            text=("===============\n====  CREATE NEW ACCOUNT PAGE  ====\n===============\n"
                                " The Sign up Page is the window that will pop up when a user clicks the create new account button." 
                                " It is where the user will enter his/her username to register in the system and creating an account"
                                " It will ask the user to input his/her real name, username, and password to complete the sign up"
                                " It has 4 conditions for a new account to be succesfully created\n")).pack(padx=20, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"ACCOUNT ALREADY EXIST!\"\n===============\n "
                                " The username is already taken and the user needs to change his/her inputted username")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"PLEASE ENTER ALL TEXT FIELD REQURIED!\"\n===============\n "
                                " It did not fill all the text field required to create new account")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"YOUR USERNAME OR REAL NAME CAN'T BE MORE THAN 12 CHARACTERS!\"\n===============\n "
                                " If the username and realname has more than 12 characters")).pack(pady=5)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"Account (User) has been successfully created!\"\n===============\n "
                                " If the user has succesfully created an account")).pack(pady=5)
    # Home Button
    def home(self):
        self.navigationClick()
        self.homeBtn.config(bg=colors['primary'])
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12',
                            text=("===============\n====  HOME PAGE  ====\n===============\n"
                                " The Home Page is the window that will pop up when a user has succesfully logged in." 
                                " It has a navigation menu on the left side where it contains the user's realname and username."
                                " It has 6 button which are the home, article, typhoon, calculator, help and log out."
                                " The home pagge displays the system description and the user profile."
                                " It also display the total count of users, articles, bookmarks, and typhoons.\n\n"
                                " Click the other buttons to navigate more! \n")).pack(padx=15, pady=15)
    # Article Info
    def articleHelp(self):
        self.navigationClick()
        self.articlebtn.config(bg=colors['primary'])
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  ARTICLE PAGE  ====\n===============\n"
                                " The Article Page is the section when you click [ARTICLE] on the navigation menu." 
                                " It is where articles are display in the system. You can create, edit, update, delete and bookmark an article."
                                " It is divided into two parts, the bookmark and article section"
                                "\n\nScroll down to explore more about the ARTICLE PAGE\n")).pack(padx=10, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  BOOKMARK ARTICLE  ====\n===============\n"
                                "\nThe bookmark is shown on the top most layer of the frame and can be removed by pressing the [REMOVE BOOKMARK]"
                                "\nArticle ID is displayed in the upper left while the bookmark ID is displayed on the upper right."
                                "\nPosted by is displayed in the bottom left while bookmark by is displayed in the bottom right."
                                "\n[BOOKMARK] = Add Bookmark (located at the bottom of each an article)" 
                                "\n\n[DELETE] = Delete all existing bookmarks"
                                "\n\n[ADD] = ADD 10 Typhoons that is created by the database" 
                                "\n\nYou can have as much as bookmark as you want!")).pack(padx=10, pady=10)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  ARTICLE BUTTONS  ====\n===============\n"
                                "\n[EDIT] = Edit Article Database located besides the [DELETE] button" 
                                "\n\n[ADD] = ADD 20 Articles that is created by the database (if only the article is empty)" 
                                "\n\n[DELETE] = Delete all existing articles record in the database" )).pack(padx=10, pady=10)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n\"==== EDITING ARTICLE BUTTONS ====\"\n===============\n "
                                "\n[ADD ARTICLE] = Add article to the database"
                                "\n\n[DELETE ARTICLE] = Delete article from the database based on article ID"
                                "\n\n[EDIT ARTICLE] = Edit and update article's title and content based on ID"
                                "\n\n[EXIT] = Exit the edit page of the article")).pack(pady=5)
    # Typhoon info
    def typhoonHelp(self):
        self.navigationClick()
        self.Typhoonbtn.config(bg=colors['primary'])
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  TYPHOON PAGE  ====\n===============\n"
                                " The Typhoon Page is the section when you click [TYPHOON] on the navigation menu." 
                                " It is where typhoons are display in the system. You can create, search, edit, update, delete a typhoon."
                                " \n\nScroll down to explore more about the TYPHOON PAGE\n")).pack(padx=10, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n==== TYPHOON BUTTONS ====\n===============\n"
                                "\n\n[SEARCH] = Search Typhoons by name (located in the top left of the frame)" 
                                "\n\n[ADD] = ADD 10 Typhoons that is created by the database (if only the typhoon is empty)" 
                                "\n\n[EDIT] = Edit Typhoons (located in the top right of the frame)" 
                                "\n\n[DELETE] = Delete all existing typhoons record in the database")).pack(padx=10, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  EDITING TYPHOON BUTTONS  ====\n===============\n"
                                "\n[ADD TYPHOON] = Add typhoon to the database"
                                "\n\n[DELETE TYPHOON] = Delete typhoon from the database based on article ID"
                                "\n\n[EDIT TYPHOON] = Edit and update typhoon's title and content based on ID"
                                "\n\n[EXIT] = Exit the edit page of the typhoon")).pack(pady=5)
    # Calculator Info
    def calculatorHelp(self):
        self.navigationClick()
        self.calculatorbtn.config(bg=colors['primary'])
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  CALCULATOR PAGE  ====\n===============\n"
                                " The Calculator Page is the section when you click [CALCULATOR] on the navigation menu." 
                                " It is a calcultor that estimates the strength of a typhoon based on user input using "
                                " common typhoon classification scales like the Saffir-Simpson scale."
                                " A user can input any number to see the converted value to mph, knots, ft/s, and km/h."
                                " After inputting a wind speed, choosing a unit then pressing convert, it will show the"
                                " converted value of mph, knots, ft/s, and km/h, and it will show the category of the wind speed"
                                " \n\nScroll down to explore more about the CALCULATOR PAGE\n")).pack(padx=10, pady=15)
        Label(self.helpScrollbar, wraplength=600, bg=colors['primary'], font='Arial 12', bd=3, relief=GROOVE, padx=10, pady=10,
                            text=("===============\n====  BUTTON FUNCTIONS  ====\n===============\n"
                                "\n[Enter Wind Speed] = Enter numeric value to convert into"
                                "\n\n[Select a Unit] = Select the unit of the current wind speed"
                                "\n\n[CONVERT] = A Button to show the converted value of the wind speeds"
                                "\n\n[SCALE] = Drag the scale to any number from 1-300 to know the category of the wind speed")).pack(pady=5)
    # EXIT BUTTON
    def exitHelp(self):
        if messagebox.askyesno('Confirmation','Are you sure you want to exit?'):
            self.window.destroy()
        else: 
            messagebox.showwarning('Cancelled', 'Exit Failed!')
            self.window.deiconify()
            return

if __name__ == "__main__":
    window = Tk()
    app = logIn(window)
    window.mainloop()