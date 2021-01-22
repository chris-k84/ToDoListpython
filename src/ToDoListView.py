import tkinter as Tk

class View():
    def __init__(self, master):
        master.title("Python To Do List")
        listFrame = Tk.Frame(master)
        inputFrame = Tk.Frame(master)

        listFrame.grid(row=1,column=1)
        inputFrame.grid(row=1, column=2)

        tasknamelabel = Tk.Label(inputFrame,text= "Task Name")
        descriptionlabel = Tk.Label(inputFrame, text= "Task Description")
        self.TaskName = Tk.StringVar()
        self.TaskDescription = Tk.StringVar()
        taskentry = Tk.Entry(inputFrame,textvariable=self.TaskName)
        descriptionentry = Tk.Entry(inputFrame,textvariable=self.TaskDescription)
        
        tasknamelabel.grid(row=1, column=1) 
        descriptionlabel.grid(row=2, column=1)
        taskentry.grid(row=1, column=2)
        descriptionentry.grid(row= 2, column=2)

        self.taskListView = Tk.Listbox(listFrame)
        self.AddButton = Tk.Button(listFrame, text="Add")
        self.RemoveButton = Tk.Button(listFrame, text="Remove")
        
        self.taskListView.grid(row=1, column=1, columnspan=2)
        self.AddButton.grid(row=2,column=1)
        self.RemoveButton.grid(row=2, column=2)
        
        

        

