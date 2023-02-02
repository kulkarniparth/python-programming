import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def set_month():
    messagebox.showinfo(title="Close Window", message="Month selected is "+month_var.get())


win = tk.Tk()
win.geometry("400x300")
win.title("Combo Box")
win.resizable(False, False)

month_var = tk.StringVar()

title_message = tk.Message(win, text="Select the month of birth", justify=tk.CENTER)
month_label = tk.Label(win, text="Month")
combo_box = ttk.Combobox(win, width=20, textvariable=month_var)
combo_box["values"] = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
combo_box["state"] = "readonly"
combo_box.current(5)
submit_button = tk.Button(win, text="Submit", command=set_month)
# main program loop

title_message.grid(row=0, column=0, columnspan=2)
month_label.grid(row=1, column=1)
combo_box.grid(row=1, column=1)
submit_button.grid(row=2, column=1, columnspan=2)

win.mainloop()
