import time
import tkinter as tk
from tkinter import messagebox, ttk


win = tk.Tk()
win.geometry("400x300")
win.title("Progress Bar")

pb = ttk.Progressbar(win, orient=tk.HORIZONTAL,length=200, value=0, mode="indeterminate")

start_button = tk.Button(win, text="Start", command=pb.start)
stop_button = tk.Button(win, text="stop", command=pb.stop)

pb.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
start_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
stop_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

win.mainloop()
