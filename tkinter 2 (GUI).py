from tkinter import *
root = Tk()

root.title("Welcome")
computer = Label(root, bg="green", fg="white",
                text="Computer", font=("Times", 50, "italic"))
science = Label(root, bg="blue", fg="yellow",
                text="Science is", font=("Times", 50, "bold"))
awesome = Label(root, bg="orange", fg="red",
                text="awesome!", font=("Times", 50, "bold"))

computer.pack()
science.pack()
awesome.pack()

root.mainloop()