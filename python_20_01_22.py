import tkinter as tk
from tkinter import messagebox

def callback(input_str):
    if input_str.isdigit():
        if int(input_str) > 120:
            return False
        else:
            return True
    elif input_str == "":
        return True
    else:
        return False


def get_info():
    print("hello")
    name = name_var.get()
    age = age_var.get()
    address = address_text.get("1.0", tk.END)
    name_var.set("")
    age_var.set(25)
    address_text.delete("1.0", tk.END)
    name_entry.focus()

    # CMD prompt output

    # print(name)
    # print(age)
    # print(address)

    # Message field widget (multiline widget as opposed to label widget, which is a single line widget)

    # feedback_msg.config(text=name+"\n"+str(age)+"\n"+address)

    # Messagebox pop-up
    messagebox.showinfo(title="result", message=name+"\n"+str(age)+"\n"+address)


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
feedback_msg = tk.Message(win, font=("Aerial", 15), text="")

# registering a call back method
reg = win.register(callback)
# assigning callback method to age_entry field
age_entry.config(validate="key", validatecommand=(reg, "%P"))

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
feedback_msg.grid(row=6, column=0)

# main program loop
win.mainloop()
