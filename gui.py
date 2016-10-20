from tkinter import *
import one_password

window = Tk()
window.title("one password")
ori_pass = Entry(window, show="*")
service = Entry(window)
digits = Entry(window)
show_pass = IntVar()
show_checkbox = Checkbutton(window, text="show password", variable=show_pass)
password = Entry(window)
def gen_pass():
    number_digits = digits.get()
    number_digits = 10 if number_digits == '' else int(number_digits)
    password_str = one_password.generate_pass(ori_pass.get(), service.get(), number_digits)
    password.delete(0, END)
    if show_pass.get():
        password.insert(END, password_str)
    else:
        password.insert(END, "copied to clipboard")
    window.clipboard_clear()
    window.clipboard_append(password_str)

Label(window, text="Easy remember passwod").pack()
ori_pass.pack()
Label(window, text="Service").pack()
service.pack()
Label(window, text="Digits (default: 10)").pack()
digits.pack()
show_checkbox.pack()
Button(window, text="Generate", command=gen_pass).pack()
Label(window, text="Output Password").pack()
password.pack()
window.mainloop()
