import tkinter as tk

from window_mover import WindowMover

root = tk.Tk()
root.configure(bg='gray')
root.geometry("500x500")

lable = tk.Label(root, text='Cool Lable', fg='white', bg='gray')
lable.pack()

WindowMover(root, [lable])

running = True
while running:
    root.update()

root.destroy()