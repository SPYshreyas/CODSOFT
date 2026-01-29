from tkinter import *
import json
import os

CONTACT_FILE = "contacts.json"
contacts = []

def load_contacts():
    global contacts
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            contacts = json.load(f)

def save_contacts():
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def edit_contact_window(old_contact, person_frame, detail_window):
    detail_window.withdraw()

    edit_win = Toplevel(root)
    edit_win.title("Edit Contact")
    edit_win.geometry("400x250")

    def back_from_edit():
        edit_win.destroy()
        detail_window.deiconify()

    name_var = StringVar(value=old_contact["name"])
    phone_var = StringVar(value=old_contact["phone"])
    email_var = StringVar(value=old_contact["email"])
    address_var = StringVar(value=old_contact["address"])

    main = Frame(edit_win)
    main.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def row(label, var):
        f = Frame(main)
        f.pack(fill=X, pady=4)
        Label(f, text=label, width=15, anchor="w").pack(side=LEFT)
        Entry(f, textvariable=var).pack(side=LEFT, fill=X, expand=True)

    row("Name", name_var)
    row("Phone", phone_var)
    row("Email", email_var)
    row("Address", address_var)

    def save_edit():
        old_contact["name"] = name_var.get()
        old_contact["phone"] = phone_var.get()
        old_contact["email"] = email_var.get()
        old_contact["address"] = address_var.get()

        save_contacts()
        refresh_contact_list()

        edit_win.destroy()
        detail_window.destroy()
        root.deiconify()

    btn_frame = Frame(edit_win)
    btn_frame.pack(fill=X, pady=10)

    Button(btn_frame, text="Back", command=back_from_edit).pack(side=LEFT, padx=10)
    Button(btn_frame, text="Save", fg="green", command=save_edit).pack(side=RIGHT, padx=10)

def add_person_row(name,phone,email,address):
    person_frame = Frame(left_frame)
    person_frame.pack(fill=X,padx=4,pady=4)
    person = Label(person_frame,text=f"{name}",font="Arial 12 bold")
    person.pack(side=LEFT,padx=6)
    detail_btn = Button(person_frame,text='DETAILS',command=lambda:contact_detail(
        name,phone,email,address,person_frame
    ))
    detail_btn.pack(side=RIGHT,padx=6)

def persAdd(name,phone,email,address,window):
    contact = {
        "name":name,
        "phone":phone,
        "email":email,
        "address":address
    }
    contacts.append(contact)
    save_contacts()

    add_person_row(name,phone,email,address)
    window.destroy()
    root.deiconify()

def add_contact():
    root.withdraw()
    new_contact = Toplevel()
    new_contact.title('Add New Contact')
    new_contact.geometry('400x250')

    def back_from_newContact():
        new_contact.destroy()
        root.deiconify()
    
    control_frame_2 = Frame(new_contact)
    control_frame_2.pack(fill=X,pady=5)
    back2 = Button(control_frame_2,text="Back",pady=2,padx=15,command=back_from_newContact)
    back2.pack(side=LEFT,padx=10,pady=10)
    new_contact_label = Label(control_frame_2,text="NEW CONTACT",font="Arail 16 bold",borderwidth=2,relief=SOLID,pady=4,padx=25)
    new_contact_label.pack(anchor="center",pady=8)


    full_name = StringVar()
    phone = StringVar()
    email = StringVar()
    address = StringVar()

    add_mainFrame = Frame(new_contact)
    add_mainFrame.pack(fill=BOTH,expand=True,padx=6)
    
    name_frame = Frame(add_mainFrame)
    name_frame.pack(fill=X,padx=30,pady=5)
    name_label = Label(name_frame,text="Enter Full Name :").pack(side=LEFT)
    nameentry = Entry(name_frame,textvariable=full_name).pack(side=LEFT,padx=8)

    phone_frame = Frame(add_mainFrame)
    phone_frame.pack(fill=X,padx=30,pady=5)
    phone_label = Label(phone_frame,text="Enter Phone Number :").pack(side=LEFT)
    phoneentry = Entry(phone_frame,textvariable=phone).pack(side=LEFT,padx=8)
   
    email_frame = Frame(add_mainFrame)
    email_frame.pack(fill=X,padx=30,pady=5)
    email_label = Label(email_frame,text="Enter email :").pack(side=LEFT)
    emailentry = Entry(email_frame,textvariable=email).pack(side=LEFT,padx=8)

    address_frame = Frame(add_mainFrame)
    address_frame.pack(fill=X,padx=30,pady=5)
    address_label = Label(address_frame,text="Enter Address :").pack(side=LEFT)
    addressentry = Entry(address_frame,textvariable=address).pack(side=LEFT,padx=8)
    
    cancel_button = Button(new_contact,text="Cancel", command=back_from_newContact,pady=7,padx=10,foreground='red').pack(side=LEFT,padx=10,pady=10)
    save_button = Button(new_contact,text="Save",pady=7,padx=10,foreground='green',command=lambda:persAdd(
        full_name.get(),phone.get(),email.get(),address.get(),new_contact
    )).pack(side=RIGHT,padx=10,pady=10)
    

def contact_detail(name,phone,email,address,person_frame):
    root.withdraw()                        

    detail_window = Toplevel(root)
    detail_window.title("Detail")
    detail_window.geometry("400x300")
    
    def back_from_details():
        detail_window.destroy()
        root.deiconify() 
    def delete_contact():
        contacts[:] = [
            c for c in contacts
            if not (c["name"] == name and c["phone"] == phone)
        ]
        save_contacts()

        person_frame.destroy()
        detail_window.destroy()
        root.deiconify()
    def edit_contact():
        for c in contacts:
            if c["name"] == name and c["phone"] == phone:
                edit_contact_window(c, person_frame, detail_window)
                break


    contr_frame = Frame(detail_window,bg='darkgrey')
    contr_frame.pack(fill=X,pady=10,padx=5)

    back_button = Button(contr_frame,text="Back",command=back_from_details)
    back_button.pack(side=LEFT, padx=10, pady=10)
    delete_button = Button(contr_frame,text="Delete",fg='red',command=delete_contact)
    delete_button.pack(side=RIGHT,padx=10,pady=10)

    detail_Frame = Frame(detail_window,bg="grey")
    detail_Frame.pack(fill=BOTH,expand=True)
    
    label2_frame = Frame(detail_Frame,bg="grey")
    label2_frame.pack(fill=X,pady=5)
    label2 = Label(label2_frame,text=(f"{name}"),font="Arial 18 bold",padx=10,pady=5,borderwidth=2,relief="solid")
    label2.pack()
    label3_frame = Frame(detail_Frame,bg="grey")
    label3_frame.pack(fill=X,pady=5)
    label3 = Label(label3_frame,text=(f"Mobile {phone}"),padx=10,pady=5)
    label3.pack(anchor="w",padx=8)
    label4_frame = Frame(detail_Frame,bg="grey")
    label4_frame.pack(fill=X,pady=5)
    label4 = Label(label4_frame,text=(f"Email {email}"),padx=10,pady=5)
    label4.pack(anchor="w",padx=8)
    label5_frame = Frame(detail_Frame,bg="grey")
    label5_frame.pack(fill=X,pady=5)
    label5 = Label(label5_frame,text=(f"Address {address}"),padx=10,pady=5)
    label5.pack(anchor="w",padx=8)
    edit_button = Button(detail_Frame,text="Edit",padx=10,pady=5,command=edit_contact)
    edit_button.pack(side=RIGHT,padx=10,pady=10)

def clear_contact_list():
    for widget in left_frame.winfo_children():
        widget.destroy()
def refresh_contact_list(filtered_contacts=None):
    clear_contact_list()
    data = filtered_contacts if filtered_contacts is not None else contacts

    for c in data:
        add_person_row(c["name"],c["phone"],c["email"],c["address"])

def search():
    query = search_value.get().strip().lower()

    if query == "":
        refresh_contact_list()
        return
    result = []
    for c in contacts:
        if(
            query in c["name"].lower()
            or query in c["phone"].lower()
            or query in c["email"].lower()
        ):
            result.append(c)
    refresh_contact_list(result)

root = Tk()
root.title("CONTACT BOOK")
root.geometry("600x500")

title = Label(root,text="CONTACT BOOK",font="Verdana 24 bold",bg='lightgrey',borderwidth=2,relief=SUNKEN).pack(fill=X,pady=5)

control_frame = Frame(root)
control_frame.pack(fill=X,pady=4)

search_value = StringVar()
searchEntry = Entry(control_frame,textvariable=search_value)
searchEntry.pack(side=LEFT,padx=15)
searchEntry.bind("<KeyRelease>",lambda event:search())
search_button = Button(control_frame,text="Search",padx=8,command=search).pack(side=LEFT)

main_frame = Frame(root,bg="darkgrey")
main_frame.pack(fill=BOTH,expand=True)

list_container = Frame(main_frame)
list_container.pack(side=LEFT,fill=BOTH,expand=True,padx=10,pady=10)

right_frame = Frame(main_frame,bg="darkgrey")
right_frame.pack(side=RIGHT,fill=Y,padx=10,pady=10)

add_button = Button(control_frame,text="New Contact",padx=10,pady=5,command=add_contact)
add_button.pack(side=RIGHT,pady=15,padx=8)

canvas = Canvas(list_container)
canvas.pack(side=LEFT,fill=BOTH,expand=True)

contact_scroll = Scrollbar(list_container,orient=VERTICAL,command=canvas.yview)
contact_scroll.pack(fill=Y,side=RIGHT)

left_frame = Frame(canvas,)
canvas_window = canvas.create_window((0, 0), window=left_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

left_frame.bind("<Configure>", on_frame_configure)

def resize_canvas(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", resize_canvas)

canvas.config(yscrollcommand=contact_scroll.set)

load_contacts()

for c in contacts:
    add_person_row(c["name"], c["phone"], c["email"], c["address"])

root.mainloop()
