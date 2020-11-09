from tkinter import *

window = Tk()
window.title('Simple Calculator')

f_num = 0

def button_click(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current)+str(number))
def clear():
    entry1.delete(0, END)

def add_num():
    num = entry1.get()
    global f_num
    f_num = num
    entry1.delete(0, END)

def get_sum():
    num = entry1.get()
    global f_num
    entry1.delete(0, END)
    sum = int(num) + int(f_num)
    entry1.insert(0, sum)

# Create Input
entry1 = Entry(window, borderwidth=2, width=40)

# Create Buttons
button_1 = Button(window, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(window, text='clear', padx=80, pady=20, command=clear)
button_add = Button(window, text='+', padx=120, pady=20, command=add_num)
button_equal = Button(window, text='=', padx=120, pady=20, command=get_sum)

#Place everything
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0, columnspan=3)
button_equal.grid(row=6, column=0, columnspan=3)


window.mainloop()