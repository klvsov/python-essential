from tkinter import *

root = Tk()

root.title('Що будемо вчити далі?')
def Answer(event):
    global lang
    lang = answer.cget('text')
    res['text'] = 'Молодець! Ти попав і будеш вчити ' + lang

label1 = Label(root, text='Який фреймворк чи бібліотеку будемо вивчати далі?', pady=10)

Framework = IntVar()

answer = Label(root, textvariable=Framework, pady=10)

Django = Radiobutton(root, text='Django', pady=10, variable=Framework, value='Django')
PyGame = Radiobutton(root, text='PyGame', pady=10, variable=Framework, value='PyGame')
Flask = Radiobutton(root, text='Flask', pady=10, variable=Framework, value='Flask')
btn = Button(root, text='Вибрати')
res = Label(root, pady=15)

label1.pack()
Django.pack()
PyGame.pack()
Flask.pack()
btn.pack()
res.pack()
btn.bind('<Button-1>', Answer)
mainloop()
