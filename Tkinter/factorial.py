from tkinter import *

def fact(event):
    n = int(input1.get())
    res = 1
    for i in range(1, n + 1):
        res *= i
    input1.delete(0)
    input1.insert(0, res)

root = Tk()
root.geometry('200x200')
root.title('Факторіал числа')

input1 = Entry(root, bd='0')

button1 = Button(root, text='n!', width=5, height=2, bg='#ffffff')
input1.pack()
button1.pack()
button1.bind('<Button-1>', fact)

mainloop()
