import tkinter as tk

class ToDoList:
    def __init__(self) :
        #Create  a window
        self.window=tk.Tk()
        self.window.title=("To-Do List")
        #Create  a Frame
        self.input_frame= tk.Frame(self.window)
        self.input_frame.pack(pady=10)
        #Entry box
        self.entry= tk.Entry(self.input_frame,width=35)
        self.entry.pack(side=tk.LEFT,padx=5)
        #Create an Add button
        self.add_button =tk.Button(self.input_frame, text="Add",command=self.add_item)
        self.add_button.pack(side=tk.LEFT,padx=5)
        #Create a Frame to store the events
        self.list_frame=tk.Frame(self.window)
        self.list_frame.pack(pady=10)
        #List Box where items are stored
        self.listbox = tk.Listbox(self.list_frame,selectmode=tk.MULTIPLE, width=45, height=15)
        #Scroll Bar for the List Box
        self.scrollbar=tk.Scrollbar(self.list_frame)
        #config scroll bar
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        #Create Delete Button
        self.delete_button=tk.Button(self.window,text='Delete',command=self.delete_items)
        self.delete_button.pack(pady=10)


        


        self.window.mainloop()
    def add_item(self):
        item=self.entry.get()
        if item:
            self.listbox.insert(tk.END,item)
        self.entry.delete(0,tk.END)
    
    def delete_items(self):
        selected_items=self.listbox.curselection()
        for index in reversed(selected_items):
            self.listbox.delete(index)




if __name__ =="__main__":
    ToDoList()



