import tkinter as tk


def set_occupation():
    print("hello")
    print("Selected profession is " + rb_names[rb_selected.get()])


# declaration of window

win = tk.Tk()
win.geometry("400x300")
win.title("Radio Button")

L1 = tk.Label(win, text="Enter Occupation")
L1.pack()

rb_names = ("Student", "Job", "Retired", "Businessman")
rb_values = (0, 1, 2, 3)
rb_selected = tk.IntVar(win, 1)

for i in range(4):
    rb = tk.Radiobutton(win, text=rb_names[i], variable=rb_selected, value=rb_values[i])
    rb.pack(anchor=tk.W)

submit_button = tk.Button(win, text="Submit", command=set_occupation)
submit_button.pack()
win.mainloop()
