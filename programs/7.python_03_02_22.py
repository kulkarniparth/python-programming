import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def setpoint_updated():
    print(sb_var.get())


def setpoint_submitted():
    messagebox.showinfo("Selection", "setpoint = " + str(sb_var.get()))


win = tk.Tk()
win.geometry("400x300")
win.title("Spin Box")

sb_var = tk.DoubleVar(win, 55.0)

sb_label = tk.Label(win, text="Set Point")
sb = ttk.Spinbox(win, width=10, textvariable=sb_var, state="readonly", from_=45.0, to=75.0, increment=0.5,
                 command=setpoint_updated)
button = tk.Button(win, text="Submit", command=setpoint_submitted)

sb_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
sb.grid(row=1, column=0, columnspan=2, padx=15, pady=5)
button.grid(row=2, column=0, columnspan=2, ipadx=5, ipady=5)

win.mainloop()
