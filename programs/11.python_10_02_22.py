import time
import tkinter as tk
from tkinter import messagebox, ttk


def start_job():
    while pb["value"] <= 100:
        value_label.config(text=f"Progress = {pb['value']} %")
        time.sleep(0.5)
        win.update()
        pb["value"] += 10
    messagebox.showinfo("Progress", "Job Completed")
    pb["value"] = 0


win = tk.Tk()
win.geometry("400x300")
win.title("Progress Bar")

pb = ttk.Progressbar(win, orient=tk.HORIZONTAL,length=200, value=0, mode="determinate")

value_label = tk.Label(win)
start_button = tk.Button(win, text="Start", command=start_job)

pb.pack(padx=10, pady=20)
value_label.pack(padx=10, pady=10)
start_button.pack(padx=10, pady=10)

win.mainloop()
