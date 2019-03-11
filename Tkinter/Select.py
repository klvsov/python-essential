from tkinter import *
def buy():
    select = lshop.curselection()
    for i in select:
        lgoods.insert(END, lshop.get(i))
    select = list(select)
    select.reverse()
    for i in select:
        lshop.delete(i)
def returnGoods():
    select = lgoods.curselection()
    for i in select:
        lshop.insert(END, lgoods.get(i))
    select = list(select)
    select.reverse()
    for i in select:
        lgoods.delete(i)
root = Tk()
shop = ['Яблука', 'Банани', 'Помідори', 'Картопля', 'Морква',
'Ананас', 'Хліб', 'Пиво', 'Молоко', "М'ясо"]
lshop = Listbox(selectmode=EXTENDED)
lshop.pack(side=LEFT)
for i in shop:
    lshop.insert(END, i)
lgoods = Listbox(selectmode=EXTENDED)
lgoods.pack(side=RIGHT)
bbuy = Button(root, text=">>>", command=buy)
bbuy.pack()
breturn = Button(root, text="<<<", command=returnGoods)
breturn.pack()
root.mainloop()
