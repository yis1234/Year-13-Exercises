from tkinter import *
root = Tk()

root.title("My first window")


# window.geometry - to set size of 600px wide x 200px tall
root.geometry("600x200")  # string using 'x' not '*' - no spaces either side
root.maxsize(800, 400)  # int values - ses max resizeable dimensions

greeting = Label(text="Hello, Tkinter")


greeting.pack()

root.mainloop()