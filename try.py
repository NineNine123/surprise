import tkinter as tk
from tkinter import messagebox

def show_surprise():
    messagebox.showinfo("Surprise!", "Gotcha! You're too cute to fall for this 😂")

root = tk.Tk()
root.title("Surprise Button")

button = tk.Button(root, text="Click here to see a surprise", command=show_surprise)
button.pack(padx=20, pady=20)

root.mainloop()

