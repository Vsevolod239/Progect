from math import *
import time
from tkinter import *
from tkinter import messagebox
import random
root =Tk()
root.title("Построение графиков функций")
ger=Frame(root,width=150,bg='silver')
ger.pack(side='left',fill='y')
graph=Frame(root,height=600, width=700,bg='bisque2')
graph.pack(side='left',fill='both',expand=3)
c=Canvas(graph, height=600, width=700, bg='whitesmoke')
c.pack(fill='both',expand=3)
xmin=-5
xmax=5
ymax=5
ymin=-5
maxx=700
maxy=600
dx=0.1
x=0
y=0
x1=0
currentTime = int(time.strftime('%H'))
if currentTime < 12 :
     messagebox.showinfo("",'Good morning')
if currentTime > 12 and currentTime < 18 :
     messagebox.showinfo("",'Good afternoon')
if currentTime > 18 :
     messagebox._show("",'Good evening')
c.create_line(maxx//2,maxy,maxx//2,0,fill='black',arrow=LAST)
c.create_line(0,maxy//2,maxx,maxy//2,fill='black',arrow=LAST)
x=-4
x1=70
x2=600
while x<=4:
    c.create_line(x1,maxy//2,x1,maxy//2+5)
    if x!=0:
        c.create_text(x1,maxy//2+12,text=str(x))
    x1+=70
    x2-=60
    c.create_line(maxx//2,x2,maxx//2+5,x2)
    if x!=0:
        c.create_text(maxx//2+10,x2,text=str(x))
    x+=1
c.create_text(maxx//2+12,maxy//2+12,text=str(0))
def nx(x):
    global xmin, xmax,maxx
    return round((x-xmin)/(xmax-xmin)*maxx)
def ny(y):
    global ymax,ymin,maxy
    return round((y-ymax)/(ymax-ymin)*maxy)
def com1():
    messagebox.showinfo('Справка','1)введите уравнение функции в поле функция\n2)подпишите оси в ячейках\n3)нажмите построить график')
def com2():
    global fnt
    fnt=ent_f.get()
    yt(y,'red')
def yt(f,gfill):
    x=-4
    while x<=4:
        c.create_line(nx(x),-ny(y(x)),nx(x+dx),-ny(y(x+dx)),width=2,fill="red")
        x=x+dx
def y(x):
    return eval(fnt)
def on_closing():

    if messagebox.askokcancel("Выход из приложения","Хотите выйти из приложения?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
def com4():
    c.create_rectangle(0,0,1000,1000,fill='white', outline='white')
    c.create_line(maxx // 2, maxy, maxx // 2, 0, fill='black', arrow=LAST)
    c.create_line(0, maxy // 2, maxx, maxy // 2, fill='black', arrow=LAST)
    x = -4
    x1 = 70
    x2 = 600
    while x <= 4:
        c.create_line(x1, maxy // 2, x1, maxy // 2 + 5)
        if x != 0:
            c.create_text(x1, maxy // 2 + 12, text=str(x))
        x1 += 70
        x2 -= 60
        c.create_line(maxx // 2, x2, maxx // 2 + 5, x2)
        if x != 0:
            c.create_text(maxx // 2 + 10, x2, text=str(x))
        x += 1
    c.create_text(maxx // 2 + 12, maxy // 2 + 12, text=str(0))
x4=15; h=20
lb_f=Label(ger, text='функция',bg='silver')
lb_f.place(x=x4, y=210, width=50, height=h)
ent_f=Entry(ger)
ent_f.place(x=x4, y=240, width=120, height=h)
lb_i=Label(ger, text='y=',bg='silver')
lb_i.place(x=x4-10, y=240, width=15, height=h)
ent_y=Entry(c)
ent_y.place(x=360,y=0,width=50, height=h)
ent_x=Entry(c)
ent_x.place(x=650,y=310,width=50, height=h)
bt1=Button(ger, text='построить график',bg='azure',fg='black',command=com2)
bt1.place(x=x4, y=270, width=120, height=h)
bt2=Button(ger, text='справка', command=com1,bg='azure',fg='black')
bt2.place(x=x4, y=300, width=120, height=h)
bt3=Button(ger, text='удалить все',command=com4,bg='azure',fg='black')
bt3.place(x=x4, y=330, width=120, height=h)
root.mainloop()
