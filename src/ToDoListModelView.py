import tkinter as Tk
import ToDoListView as Tdview
import ToDoListModel as TdModel


class ModelView():
    def __init__(self):
        self.root = Tk.Tk()
        self.view = Tdview.View(self.root)
        self.view.AddButton.bind("<Button>",self.add)
        #self.view.RemoveButton.bind("<Button>", self.remove)
        self.TaskList = []
        self.Task = TdModel.ToDoListItem

    def run(self):
        self.root.title("To Do List")
        self.root.mainloop()

    def add(self, event):
        self.Task.taskname = self.view.TaskName.get()
        self.Task.taskdescription = self.view.TaskDescription.get()
        self.TaskList.append(self.Task)

    def remove(self, event):
        self.TaskList.remove(self.view.taskListView.curselection)

