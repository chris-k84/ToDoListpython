import tkinter as Tk
import ToDoListView as Tdview
import ToDoListModel as TdModel
import json


class ModelView():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.onClose)
        self.view = Tdview.View(self.root)
        self.view.AddButton.bind("<Button>",self.add)
        self.view.RemoveButton.bind("<Button>", self.remove)
        self.TaskList = []
        self.onStart()

    def run(self):
        self.root.title("To Do List")
        self.root.mainloop()

    def add(self, event):
        task = TdModel.ToDoListItem
        task.taskname = self.view.TaskName.get()
        task.taskdescription = self.view.TaskDescription.get()
        test = task.taskname + " " + task.taskdescription
        self.TaskList.append(test)
        self.view.taskListView.insert(Tk.ACTIVE, "{:<1s}{:>25s}".format(task.taskname, task.taskdescription) )

    def remove(self, event):
        index = self.view.taskListView.curselection()
        size = self.view.taskListView.size()
        if len(index) == 0:
            return
        if (index[0]+1) != size:
            del self.TaskList[index[0]]
            self.view.taskListView.delete(index)

    def onClose(self):
        with open('test.json','w') as fh:
            json.dump(self.TaskList,fh)
        self.root.destroy()

    def onStart(self):
        with open('test.json') as fh:
            self.TaskList = json.load(fh)
        self.view.taskListView.insert(Tk.END,self.TaskList)
        #for task in self.TaskList:


