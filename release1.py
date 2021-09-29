from tkinter import*
from math import*
root = Tk()
root.title("ПОСТРОЕНИЕ ГРАФИКОВ")
X = 900
Y = 600
xm = -5
y = -5
xx = 5
yy = 5
dx = 0.1
y_1 = 10; h = 18
pn_1 = Frame(root, height=70)
pn_2 = Frame(root, height=600, width=900, bg='white')
pn_2.pack(side='top', fill='x')
pn_2.pack(side='bottom', fill='both', expand=1)
c = Canvas(pn_1, height=600, width=900, bg='white')
c.pack(fill='both', expand=1)
lb_mx = Label(pn_1, text='maxx')
lb_mx.place(x=20,y=y_1, width=30, height=h)
ent_mx = Entry(pn_1)
ent_mx.focus()
lb_mx.place(x=55, y=y_1, width=45, height=h)
lb_my = Label(pn_1, text='maxy')
lb_my.place(x=110, y=y_1, width=30, height=h)
ent_my = Entry(pn_1)
ent_my.place(x=155, y=y_1, width=45, height=h)
lb_f = Label(pn_1, text='функция')
lb_f.place(x=310, y=y_1, width=50, height=h)
ent_f = Entry(pn_1)
lb_f.place(x=375, y=y_1, width=200, height=h)
def x(x):
    global xm, X, xx
    return((x-xm)/(X-xm)*xx)
def y(x):
    global ym, Y, yy
    return((y-ym)/(Y-ym)*yy)
root.mainloop()
