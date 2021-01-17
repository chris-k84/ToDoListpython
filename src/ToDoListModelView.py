import tkinter as Tk
import ToDoListView as Tdview


if __name__ == '__main__':
    master = Tk.Tk()
    view = Tdview.View(master)
    master.mainloop()