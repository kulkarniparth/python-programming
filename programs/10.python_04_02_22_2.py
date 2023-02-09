import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


def get_text():
    messagebox.showinfo("Scrolled Text Content", )


win = tk.Tk()
win.geometry("400x300")
win.title("ScrolledText")

st_var = tk.StringVar()
st = scrolledtext.ScrolledText(win, width=30, height=4, wrap=tk.WORD, font=("Times New Roman", 15))
submit_button = tk.Button(win, text="Submit", command=get_text)

st.focus()

st.pack(expand=True, pady=10)
submit_button.pack(expand=True, pady=10)

win.mainloop()
