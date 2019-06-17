from tkinter import *

root = Tk()

username = Label(root, text='Username :')
password = Label(root, text='Password :')
userbox = Entry(root)
passbox = Entry(root)

signin = Button(root, text='Sign In')
signup = Button(root, text='Sign Up')

username.grid(row=0, column=0)
password.grid(row=1, column=0)
userbox.grid(row=0, column=1)
passbox.grid(row=1, column=1)


signin.grid(row=2, column=2)
signup.grid(row=2, column=3)

root.mainloop()
