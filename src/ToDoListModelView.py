import tkinter as Tk
import ToDoListView as Tdview


class ModelView():
    def __init__(self):
        self.root = Tk.Tk()
        self.view = Tdview.View(self.root)

    def run(self):
        self.root.title("To Do List")
        self.root.mainloop()