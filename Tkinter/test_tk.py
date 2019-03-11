from tkinter import *


def say_hello(event):
    S = input('Пиши сюди: ')
    label['text']= S
root = Tk()
root.title('First window')
root.geometry('300x100+100+100')

label = Label(root)

btn = Button(root, text='Кнопка')
btn.pack(side='top')
label.pack(side='bottom')
btn.bind('<Button-1>',say_hello)

mainloop()
