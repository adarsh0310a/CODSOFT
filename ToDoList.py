# TASK 1 - CODSOFT INTERNSHIP - ADARSH CHAUBEY - A GUI-BASED APPLICATION(TO-DO-LIST) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


import tkinter
from tkinter import *
from datetime import datetime
 
# CEARTING THE MAIN WINDOW
 
root = Tk()
root.title("To-Do-List")
root.geometry("500x650+500+100")
root.resizable(False, False)

# FUNTION TO ADD A TASK TO THE LIST

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
            task_list.append(task)
            listbox.insert(END, task)

task_list = []  # intialising an empty list to store vaious tasks

def openTaskFile():  # this opens and reads tasks  from the file
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:  # opens the taskfile in  reading mode
            tasks = taskfile.readlines()      # reads all tasks

            for task in tasks:
                if task != '\n':      # task not available in newline
                    task_list.append(task.strip())  
                    listbox.insert(END, task.strip())  # inserts the task into listbox
    except:
        file = open('tasklist.txt', 'w') # if file does not open, create a new file
        file.close()

# Application icon
Image_icon = PhotoImage(file="Images/tasks.png")
root.iconphoto(False, Image_icon)

# Top bar of application window 
TopImage = PhotoImage(file="Images/title.png")
Label(root, image=TopImage).pack(side="top", pady=0)

dockImage = PhotoImage(file="Images/dock.png")
Label(root, image=dockImage).place(x=30, y=25)

heading = Label(root, text="ALL TASK", font="arial 30 bold", fg="#B4CDCD",bg="#F0F8FF")
heading.place(x=130, y=30)

# Display current date 
current_date = datetime.now().strftime("%Y-%m-%d")
date_label = Label(root, text=f"Date: {current_date}", font="arial 12 bold", fg="white", bg="#EED8AE")
date_label.place(x=350, y=25)

# Frame for task entry
frame = Frame(root, width=500, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)

priority = StringVar()
priority_entry = Entry(frame, width=4, font="arial 20", bd=0)
priority_entry.place(x=260, y=7)


# Button to add task
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#9FB6CD", fg="#fff", bd=0, command=addTask)
button.place(x=400, y=0)

# frame for the LISTBOX
frame1 = Frame(root, bd=3, width=700, height=300, bg="#EEDFCC")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#EEEEE0", fg="black", cursor="sailboat", selectbackground="#CDB7B5")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# delete function
def deleteTask():
    global task_list
    task= str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

            listbox.delete(ANCHOR)    

Delete_icon = PhotoImage(file="Images/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)  # button to delete task

root.mainloop()


























