from tkinter import *
import tkinter as tk
import os

def clickedSignup():
    def close():
        screen1.destroy()
    global screen1
    global Username
    global Password
    screen1 = Tk()
    screen1.geometry("300x300")
    lbl = Label(screen1, text="enter details below").place(x=100, y=2)
    lb1 = Label(screen1, text="username:").place(x=35, y=30)
    Username = Entry(screen1,)
    Username.place(x=97, y=30)
    lbl2 = Label(screen1, text="password:").place(x=35, y=50)
    Password = Entry(screen1)
    Password.place(x=97, y=50)
    register = Button(screen1, text="register", command=register1).place(x=120, y=80)
    quitb = Button(screen1, text="close", command=close)
    quitb.place(x=250, y=270)
    quitb.config(height=1, width=5)
    screen1.mainloop()
def register1():
    Username_info = Username.get()
    Password_info = Password.get()
    file = open(Username_info+".txt", "w")
    file.write(Username_info+"\n")
    file.write(Password_info)
    Username.delete(0, END)
    Password.delete(0, END)
    file.close()
    print(Username_info)
    print(Password_info)
    print(file)
    label2 = Label(screen1, text="registration succesful you can close the window now", fg="green").place(x=7, y=105)
def verify():
    username_var = Username1.get()
    password_var = Password1.get()
    username_r = username_var + ".txt"


    Username1.delete(0, END)
    Password1.delete(0, END)
    print(username_var)
    print(password_var)
    list_of_dir = os.listdir()
    print(list_of_dir)
    if username_r in list_of_dir:
        print("it is")
        file1 = open(username_r, "r")
        verification = file1.read().splitlines()
        if password_var in verification:
            print("good to go")
            lbl = Label(screen2, text="good to go", fg="green").place(x=115, y=105)
        else:
            print("password not recognized")
            lbl = Label(screen2, text="password not recognized", fg="red").place(x=85, y=105)
    else:
        print("username not found")
        lbl = Label(screen2, text="user not found", fg="red").place(x=110, y=105)


def clickedlogin():
    global screen2
    global Password1
    global Username1
    def close():
        screen2.destroy()
    screen2 = Tk()
    screen2.title("login")
    screen2.geometry("300x300")
    quitb = Button(screen2, text="close", command=close)
    quitb.place(x=250, y=270)
    quitb.config(height=1, width=5)
    lbl = Label(screen2, text="enter your login info").place(x=90, y=2)
    Username1 = Entry(screen2, )
    Username1.place(x=97, y=30)
    lb1 = Label(screen2, text="username:").place(x=35, y=30)
    lbl2 = Label(screen2, text="password:").place(x=35, y=50)
    Password1 = Entry(screen2)
    Password1.place(x=97, y=50)
    regbut = Button(screen2, text="login", command=verify).place(x=130, y=80)
def mainscreen():
    def close():
        screen.destroy()
    screen = Tk()
    screen.geometry("300x300")
    screen.title("login system GUI")
    Lbutton = Button(screen, text="Login", command=clickedlogin)#login button
    Lbutton.config(width=15, height=2)
    Lbutton.place(x=90, y=50)
    Sbutton = Button(screen, text="signup", command=clickedSignup)
    Sbutton.config(width=15, height=2)
    Sbutton.place(x=90, y=90)
    quitb = Button(screen, text="close", command=close)
    quitb.place(x=250, y=270)
    quitb.config(height=1, width=5)
    screen.mainloop()

mainscreen()
