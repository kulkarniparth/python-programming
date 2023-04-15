import tkinter as tk


def b1_pressed(event):
    global x1, y1
    x1 = event.x
    y1 = event.y


def b1_moved(event):
    global x1, x2, y1, x2, y2
    x2 = event.x
    y2 = event.y
    c.create_line(x1, y1, x2, y2, width=2, fill=colors[color_index])
    x1, y1 = x2, y2


def b3_pressed(event):
    global color_index
    color_index += 1
    if color_index >= 4: color_index = 0


win = tk.Tk()
win.geometry("500x500")
win.title("Canvas")

x1, y1, x2, y2 = 0, 0, 0, 0
colors = ["black", "red", "blue", "yellow"]
color_index = 0

c = tk.Canvas(win, height=400, width=400, bg="lightgray")
c.bind("<Button-1>", b1_pressed)
c.bind("<B1-Motion>", b1_moved)
c.bind("<Button-3>", b3_pressed)

c.pack()
win.mainloop()
