import tkinter as tk
from tkinter import simpledialog


def collect_password():
    print("hello")
    password = simpledialog.askstring("askstring", "Enter Password", parent=win, show="*")

    if password != "":
        print(password)
    else:
        print("Password not entered")


def collect_age():
    print("hello")
    age = simpledialog.askinteger("askinteger", "Enter Age", parent=win, minvalue=0, maxvalue=120)

    if age is not None:
        print(age)
    else:
        print("Age not entered")


def collect_cost():
    print("hello")
    cost = simpledialog.askfloat("askfloat", "Enter Cost", parent=win, minvalue=10.0, maxvalue=500.0)

    if cost is not None:
        print(cost)
    else:
        print("Cost not entered")


# declaration of window

win = tk.Tk()
win.geometry("400x300")
win.title("Simple dialog functions")

password_button = tk.Button(win, text="Password", command=collect_password)
age_button = tk.Button(win, text="Age", command=collect_age)
cost_button = tk.Button(win, text="Cost", command=collect_cost)

password_button.pack()
age_button.pack()
cost_button.pack()

win.mainloop()