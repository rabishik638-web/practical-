from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Aringar Anna Govt.Arts College")
root.geometry("400x350")


# Course Registration Window
def registration():
    top = Toplevel(root)
    top.title("course registration")
    top.geometry("400x500")

    Label(top, text="Name").place(x=30, y=50)
    Label(top, text="Username").place(x=30, y=90)
    Label(top, text="Gender").place(x=30, y=130)
    Label(top, text="Address").place(x=30, y=170)
    Label(top, text="course selection").place(x=30, y=250)

    Entry(top, width=20).place(x=150, y=50)
    Entry(top, width=20).place(x=150, y=90)

    Radiobutton(top, text="male").place(x=150, y=130)
    Radiobutton(top, text="female").place(x=220, y=130)

    Text(top, height=3, width=25).place(x=150, y=170)

    courses = Listbox(top, height=3)
    courses.insert(END, "Java")
    courses.insert(END, "Python")
    courses.insert(END, "R Programming")
    courses.insert(END, "Image Processing")
    courses.place(x=150, y=250)

    Button(top, text="submit", bg="green", fg="white",
           command=lambda: messagebox.showinfo(
               "submission", "registration successfull!")).place(x=30, y=350)

    Button(top, text="cancel", bg="red", fg="white",
           command=top.destroy).place(x=120, y=350)


# Student Login Window
def login():
    top = Toplevel(root)
    top.title("student login")
    top.geometry("300x200")

    Label(top, text="Username").place(x=30, y=50)
    Label(top, text="Password").place(x=30, y=90)

    username = Entry(top, width=20)
    username.place(x=100, y=50)

    password = Entry(top, width=20, show="*")
    password.place(x=100, y=90)

    def check_login():
        if username.get() == "DHONI" and password.get() == "D@1981":
            top.destroy()
            registration()
        else:
            messagebox.showinfo("Error", "login failed!")

    def clear():
        username.delete(0, END)
        password.delete(0, END)

    Button(top, text="submit", command=check_login,
           bg="red", fg="blue").place(x=30, y=120)

    Button(top, text="clear", command=clear,
           bg="red", fg="blue").place(x=90, y=120)

    Button(top, text="close", command=top.destroy,
           bg="red", fg="blue").place(x=140, y=120)


# Menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="registration", command=registration)
filemenu.add_command(label="sign-in", command=login)
filemenu.add_separator()
filemenu.add_command(label="exit", command=root.destroy)

menubar.add_cascade(label="file", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="undo")
editmenu.add_command(label="redo")
menubar.add_cascade(label="edit", menu=editmenu)

root.config(menu=menubar)

root.mainloop()
