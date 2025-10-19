import tkinter as tk
from tkinter import colorchooser

def change_background_color():
    """Opens a color chooser dialog and changes the window background color."""
    color_code = colorchooser.askcolor(title="choose color")
    if color_code:
     root.configure(bg=color_code[1])


root = tk.Tk()
root.title("hello kokila")
root.geometry("400x300")


change_color_button = tk.Button(root, text="Change Background Color", command=change_background_color)
change_color_button.pack(pady=50)


root.mainloop()