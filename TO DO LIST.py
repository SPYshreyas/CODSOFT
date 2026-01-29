from tkinter import *
i=1
FILE_NAME = "tasks.txt"
def save_tasks():
    tasks = to_do_list.get(0,END)
    with open(FILE_NAME,"w") as file:
        for task in tasks:
            text = task[task.find(".") + 1:]
            file.write(text.strip() + "\n")

def load_tasks():
    global i 
    try:
        with open(FILE_NAME,"r") as file:
            i = 1
            for line in file:
                to_do_list.insert(END,f"{i}.{line.strip()}")
                i+=1
    except FileNotFoundError:
        pass

def addtasks():
    print(taskvalue.get())
    global i 
    to_do_list.insert(END,f"{i}.{taskvalue.get()}")
    taskvalue.set(" ")
    i+=1
    save_tasks()

def delete():
    global i
    index = clearvalue.get() - 1
    to_do_list.delete(index) #delete the desired task

    tasks = to_do_list.get(0,END)
    to_do_list.delete(0,END)
    i=1
    for task in tasks:
        Text = task[task.find(".") + 1:]
        to_do_list.insert(END,f"{i}.{Text}")
        i += 1
    save_tasks()

root = Tk()
height_g=500
breath_g=400
a=height_g  #for the min and max gui window
b=breath_g  #for the min and max gui window
  
root.title("TO DO LIST")
root.geometry(f"{height_g}x{breath_g}")
root.minsize(a,b)
root.maxsize(a,b)

f1=Frame(root,bg='blue',borderwidth=3,padx=110)
f1.grid(row=0,column=0,columnspan=5,pady=8,)
lab1=Label(f1,text="To Do List", bg='lightblue',fg='darkblue',font="comicsansms 19 bold",padx=50,).grid(row=0,column=1,columnspan=4)

taskinput = Label(root,text="ENTER TO DO TASKS :",bg="lightgreen",fg="green",)
taskinput.grid(row=2,column=0)
taskvalue = StringVar()
taskentry = Entry(root,textvariable=taskvalue)
taskentry.grid(row=2,column=1)
Button(text="SUBMIT", command=addtasks,padx=2).grid(row=2,column=2,padx=5) 

clearinput = Label(root,text='Tasks to Delete :',bg='pink',fg='red',)
clearinput.grid(row=3,column=0)
clearvalue = IntVar()
clearentry = Entry(root,textvariable=clearvalue,justify='left')
clearentry.grid(row=3,column=1)
Button(text="CLEAR",command=delete).grid(row=3,column=2,padx=10)

to_do_list = Listbox(root,width=70,height=16)
to_do_list.grid(row=4,column=0,columnspan=4,pady=10,padx=10)

load_tasks()


root.mainloop()