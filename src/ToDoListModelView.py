import tkinter as Tk
import ToDoListView as Tdview
import ToDoListModel as TdModel


class ModelView():
    def __init__(self):
        self.root = Tk.Tk()
        self.view = Tdview.View(self.root)
        self.view.AddButton.bind("<Button>",self.add)
        self.view.RemoveButton.bind("<Button>", self.remove)
        self.TaskList = []
        self.view.taskListView.insert(Tk.END,self.TaskList)

    def run(self):
        self.root.title("To Do List")
        self.root.mainloop()

    def add(self, event):
        task = TdModel.ToDoListItem
        task.taskname = self.view.TaskName.get()
        task.taskdescription = self.view.TaskDescription.get()
        #self.TaskList.append(task)
        test = task.taskname + " " + task.taskdescription
        self.TaskList.append(test)
        self.view.taskListView.insert(Tk.END, "{:1}{:5}".format(task.taskname, task.taskdescription) )

    def remove(self, event):
        index = self.view.taskListView.curselection()
        self.TaskList.remove(index)
        self.view.taskListView.delete(index)

