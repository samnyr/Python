
from tkinter import *
import os
import sqlite3
import tkinter.messagebox

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def logout():
    screen7.destroy()

def dashboard(): #tehdään dashboard ikkuna johon lisätään notet,,
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Dashboard") 
    screen8.geometry("400x400") 
    Label(screen8, text = "Welcome").pack() 
    Button(screen8, text = "Create a new note").pack()
    Button(screen8, text = "View note").pack()
    Button(screen8, text = "Delete note").pack()
  
def login_success():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Success").pack()
  Button(screen3, text = "OK", command =delete2).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error Wrong Password").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found or Wrong Details").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("User Registered")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

 
  Label(screen1, text = "Registration Success", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_success()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Enter details below (thanks for the details btw)").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username  ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password  ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Tääsklist v6")
  Label(text = "Tääsklist v6", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  def table():
    global screen9
    screen9 = Tk()
    screen9.title("Table")
    screen9.geometry("400x400")
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS tasks")
    sql = '''CREATE TABLE tanks (
        task VARCHAR(255)
    )'''

  screen.mainloop() #pitää sovelluksen yllä

main_screen()