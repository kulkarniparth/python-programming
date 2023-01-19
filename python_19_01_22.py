import tkinter as tk


def get_info():
    print("hello")
    name = name_var.get()
    age = age_var.get()
    address = address_text.get("1.0", tk.END)
    name_var.set("")
    age_var.set(25)
    address_text.delete("1.0", tk.END)
    name_entry.focus()


# declaration of window
win = tk.Tk()
win.geometry("400x300")
win.title("Information Entry")

# initialization of name, age data variables
name_var = tk.StringVar(value="")
age_var = tk.IntVar(value=25)

# initialization of the label variables
name_label = tk.Label(win, text="Name")
address_label = tk.Label(win, text="Address")
age_label = tk.Label(win, text="Age")

# initialization of Entry fields
name_entry = tk.Entry(win, width=30, font=("Aerial", 15), textvariable=name_var)
address_text = tk.Text(win, height=3, width=30, font=("Aerial", 15))
age_entry = tk.Entry(win, width=30, font=("Aerial", 15), textvariable=age_var)

# initialization of submit button
submit_button = tk.Button(win, text="Submit", command=get_info)

# laying out the components in grid
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
address_text.grid(row=1, column=1)
age_label.grid(row=2, column=0)
age_entry.grid(row=2, column=1)
submit_button.grid(row=4, column=0)

# main program loop
win.mainloop()
