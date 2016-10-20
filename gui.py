from tkinter import *
import one_password

window = Tk()
window.title("one password")
ori_pass = Entry(window, show="*")
service = Entry(window)
length = Entry(window)
show_pass = IntVar()
show_checkbox = Checkbutton(window, text="show password", variable=show_pass)
password = Entry(window)
password_str = ""
def gen_pass():
    global password_str
    length_int = length.get()
    length_int = 10 if length_int == '' else int(length_int)
    password_str = one_password.generate_pass(ori_pass.get(), service.get(), length_int)
    password.delete(0, END)
    if show_pass.get():
        password.insert(END, password_str)
    else:
        password.insert(END, "copied to clipboard")
    window.clipboard_clear()
    window.clipboard_append(password_str)

def switch_show_pass(event):
    password.delete(0, END)
    if not show_pass.get():
        password.insert(END, password_str)
    else:
        password.insert(END, "*" * len(password_str))

Label(window, text="Easy remember passwod").pack()
ori_pass.pack()
Label(window, text="Service").pack()
service.pack()
Label(window, text="Length (default: 10)").pack()
length.pack()
show_checkbox.pack()
Button(window, text="Generate", command=gen_pass).pack()
Label(window, text="Output Password").pack()
password.pack()
ori_pass.bind("<Return>", lambda event: gen_pass())
service.bind("<Return>", lambda event: gen_pass())
length.bind("<Return>", lambda event: gen_pass())
show_checkbox.bind("<Button-1>", switch_show_pass)
window.mainloop()
