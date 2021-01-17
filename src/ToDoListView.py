import tkinter as Tk

class View():
    def __init__(self, master):
        master.title("Python To Do List")
        self.frame = Tk.Frame(master)
        
        tasknamelabel = Tk.Label(text= "Task Name")
        descriptionlabel = Tk.Label(text= "Task Description")
        self.TaskName = Tk.StringVar()
        self.TaskDescription = Tk.StringVar()
        taskentry = Tk.Entry(textvariable=self.TaskName)
        descriptionentry = Tk.Entry(textvariable=self.TaskDescription)
        
        tasknamelabel.grid(row=1, column=1) 
        descriptionlabel.grid(row=2, column=1)
        taskentry.grid(row=1, column=2)
        descriptionentry.grid(row= 2, column=2)
        

