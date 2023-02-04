import tkinter as tk
from tkinter import messagebox


def store_list_selections():
    # selected_indices is tuple

    selected_indices = lb.curselection()
    selected_parameters = " ".join([lb.get(i) for i in selected_indices])
    messagebox.showinfo("Selection", selected_parameters)


win = tk.Tk()
win.geometry("400x300")
win.title("ListBox")

plist = ("temperature", "level", "pressure", "speed", "flow", "force")
lb_var = tk.Variable(value=plist)

lb_label = tk.Label(win, text="Parameter List")

lb = tk.Listbox(win, height=8, width=15, listvariable=lb_var, selectmode=tk.MULTIPLE)

submit_button = tk.Button(win, text="Submit", command=store_list_selections)

lb_label.pack(expand=True)
lb.pack(expand=True)
submit_button.pack(expand=True)

win.mainloop()
