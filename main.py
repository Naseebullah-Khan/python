from tkinter import Tk, Label, Button, Entry, END


def button_clicked():
    my_label.config(text=entry.get())
#
#
# def spin_func():
#     print(spinbox.get())
#
#
# def scale_func(value):
#     print(value)
#
#
# def checkbutton_func():
#     print(check_state.get())
#
#
# def radio_func():
#     print(radio_state.get())
#
#
# def listbox_func(event):
#     print(listbox.get(listbox.curselection()))


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=400)
window.config(padx=30, pady=30)

# Creating Label
my_label = Label(text="My first Label", font=("Arial", 24, "bold"))
my_label.config(padx=25, pady=25)
# my_label.pack(expand=1)
# my_label.pack(side="right")
# my_label["text"] = "New Text"
# OR
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Creating Button
my_button = Button(text="Click me", command=button_clicked)
my_button.config(padx=25, pady=25)
# my_button.pack()
# my_button.place(x=150, y=40)
my_button.grid(column=1, row=1)
button = Button(text="Click")
# button.pack()
# button.place(x=150, y=40)
button.grid(column=2, row=0)

# Creating Entry or TextField
entry = Entry(width=40)
entry.insert(END, string="Some text to begin with.")
# entry.pack()
# entry.place(x=200, y=70)
entry.grid(column=3, row=4)

# # Creating TextBox
# text = Text(width=30, height=4)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0", END))
# text.pack()
# # Creating SpinBox
# spinbox = Spinbox(from_=0, to=10, width=10, command=spin_func)
# spinbox.pack()
# # Creating Scale
# scale = Scale(from_=0, to=10, width=10, command=scale_func)
# scale.pack()
# # Creating CheckButton
# check_state = IntVar()
# checkbutton = Checkbutton(text="Is On? ", variable=check_state, command=checkbutton_func)
# checkbutton.pack()
# # Creating RadioButton
# radio_state = IntVar()
# radio1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_func)
# radio2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_func)
# radio1.pack()
# radio2.pack()
# # Creating ListBox
# listbox = Listbox(height=5)
# names = ["Ahmad", "Mahmod", "Arash", "Naqeeb"]
# for name in names:
#     listbox.insert(names.index(name), name)
# listbox.bind("<<ListboxSelect>>", listbox_func)
# listbox.pack()
window.mainloop()
