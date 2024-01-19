import tkinter as tk
from tkinter import END, messagebox, ttk

tk=tk.Tk()
tk.title("Practica Python")
tk.config(width=300, height=300)

lbName= ttk.Label(tk, text="Ingrese su nombre:").place(x=10, y=20)
txName= ttk.Entry()
txName.place(x=115, y=20)
def ver():
    messagebox.showinfo(message="Hola: "+str(txName.get()),title="message")

btview=ttk.Button(tk,text="ver", command=ver)
btview.place(x=30, y=40)

tk.mainloop()