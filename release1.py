from tkinter import*
from math import*
root = Tk()
root.title("ПОСТРОЕНИЕ ГРАФИКОВ")
X = 900
Y = 600
x = 5
y = -5
dx = 0.1
y_1 = 10; h = 18
pn_1 = Frame(root, height=70)
pn_2 = Frame(root, height=600, width=900, bg='white')
pn_2.pack(side='top', fill='x')
pn_2.pack(side='bottom', fill='both', expand=1)
c = Canvas(pn_1, height=600, width=900, bg='white')
c.pack(fill='both', expand=1)
lb_mx=Label(pn_1, text='maxx')
lb_mx.place(x=20,y=y_1, width=30, height=h)
ent_mx=Entry(pn_1)
ent_mx.focus()
lb_mx.place(x=55,y=y_1, width=45, height=h)
root.mainloop()
