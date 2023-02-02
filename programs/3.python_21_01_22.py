import tkinter as tk
from tkinter import messagebox


def close_window():
    print("hello")
    result=messagebox.askyesno(title="Close Window", message="Do you want to close the window?")
    if result:
        print("Bye! Window closing after 1 minute")
        # win.destroy()
        win.after(1000*60, win.destroy)

# declaration of window

win = tk.Tk()
win.geometry("400x300")
win.title("Message Box")

my_button = tk.Button(win, text="Close", command=close_window)
my_button.grid(row=1, column=1)
win.mainloop()
