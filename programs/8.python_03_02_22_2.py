import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def alarm_low_updated(val):
    print(sh_var.get())


def alarm_high_updated(val):
    print(val)


def store_parameters():
    messagebox.showinfo("Selection", " Lower limit = " + str(sh_var.get()) + " Higher limit = " + str(sv_var.get()))


win = tk.Tk()
win.geometry("400x300")
win.title("Scales")

sh_var = tk.DoubleVar(win, 45.0)
sv_var = tk.DoubleVar(win, 65.0)
sh_label = tk.Label(win, text="Alarm Low")

sh = ttk.Scale(win, variable=sh_var, from_=35.0, to=95.0, command=alarm_low_updated)
sv = ttk.Scale(win, variable=sv_var, from_=35.0, to=95.0, command=alarm_high_updated)
button = tk.Button(win, text="Submit", command=store_parameters)

sh.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
sv.grid(row=1, column=0, columnspan=2, padx=15, pady=5)
button.grid(row=2, column=0, columnspan=2, ipadx=5, ipady=5)

win.mainloop()