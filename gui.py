from tkinter import *
import one_password

window = Tk()
window.title("one password")
ori_pass = Entry(window, show="*")
service = Entry(window)
digits = Entry(window)
password = Entry(window)
def gen_pass():
    number_digits = digits.get()
    number_digits = 10 if number_digits == '' else int(number_digits)
    password.delete(0, END)
    password.insert(END, one_password.generate_pass(ori_pass.get(), service.get(), number_digits))

Label(window, text="Easy remember passwod").pack()
ori_pass.pack()
Label(window, text="Service").pack()
service.pack()
Label(window, text="Digits (default: 10)").pack()
digits.pack()
Button(window, text="Generate", command=gen_pass).pack()
Label(window, text="Output Password").pack()
password.pack()
window.mainloop()
