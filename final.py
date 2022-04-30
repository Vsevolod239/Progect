from math import *
import time
from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime 
current_datetime = datetime.now() #строка 7 получение время
root =Tk()
root.title("Построение графиков функций")
ger=Frame(root,width=150,bg='silver')
ger.pack(side='left',fill='y')
graph=Frame(root,height=600, width=700,bg='bisque2')
graph.pack(side='left',fill='both',expand=3)
c=Canvas(graph, height=640, width=740, bg='whitesmoke')
c.pack(fill='both',expand=3)
c.create_text(669,10,text=str(current_datetime))
c.create_rectangle(702,0,750,15,fill="whitesmoke",outline='whitesmoke')
c.create_rectangle(598,0,655,15,fill="whitesmoke",outline='whitesmoke') #строки 8-18 создание окна
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
k=0 #строки 19-29 присваивание значений дополнительных переменных необходимых для построения осей и графиков
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
c.create_text(maxx//2+12,maxy//2+12,text=str(0)) #строки 30-45 построение осей координат
def nx(x):
    global xmin, xmax,maxx
    return round((x-xmin)/(xmax-xmin)*maxx) 
def ny(y):
    global ymax,ymin,maxy
    return round((y-ymax)/(ymax-ymin)*maxy) 
#строк 46-51 получение значений y и x для построения графика в функциях nx(x) и ny(y) соответственно
def com2():
    c.create_rectangle(598, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    current_datetime = datetime.now() # строка 55 обновление времени
    c.create_text(669, 10, text=str(current_datetime))
    c.create_rectangle(702, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    c.create_rectangle(598, 0, 655, 15, fill="whitesmoke", outline='whitesmoke') #строки 54-58 вывод нового времени : поверх старого значения рисуем прямоугольник цвета холста, затем выводим новое время
    messagebox.showinfo('Справка','1)введите уравнение функции в поле функция в формате y=f(x), \nобязательно писать знак умножения, возведение в степень обозначается двойным знаком умножения\nв качестве аргумента использовать x \n2)подпишите оси в ячейках\n3)нажмите построить график')
#строки 54-59 создание окна справки
    def com1():
    c.create_rectangle(598, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    current_datetime = datetime.now() # строка 63 обновление времени
    c.create_text(669, 10, text=str(current_datetime))
    c.create_rectangle(702, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    c.create_rectangle(598, 0, 655, 15, fill="whitesmoke", outline='whitesmoke') #строки 62-66 вывод нового времени : поверх старого значения рисуем прямоугольник цвета холста, затем выводим новое время
    global fnt
    fnt=ent_f.get()
    yt(y,'red')
def yt(f,gfill):
    x=-4
    k=random.randint(0,5) #строка 72 получение рандомного числа для построения графика случайным цветом
    if k==0:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='yellow')
            x = x + dx
    if k==1:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='blue')
            x = x + dx
    if k==2:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='red')
            x = x + dx
    if k==3:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='green')
            x = x + dx
    if k==4:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='mediumvioletred')
            x = x + dx
    if k==5:
        while x <= 4:
            c.create_line(nx(x), -ny(y(x)), nx(x + dx), -ny(y(x + dx)), width=2, fill='aqua')
            x = x + dx
    #строки 62-96 построение графика 1 из 6 цветов соответствующего числу полученному случайным образом(код в строке 72)
def y(x):
    return eval(fnt)
def on_closing():
    c.create_rectangle(598, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    current_datetime = datetime.now() #строка 102 обновление времени
    c.create_text(669, 10, text=str(current_datetime))
    c.create_rectangle(702, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    c.create_rectangle(598, 0, 655, 15, fill="whitesmoke", outline='whitesmoke') #строки 101-106 вывод нового времени: поверх старого значения рисуем прямоугольник цвета холста, затем выводим новое время
    if messagebox.askokcancel("Выход из приложения","Хотите выйти из приложения?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing) #сторки 100-109 создание окна выхода из приложения
def com4():
    c.create_rectangle(0,0,1000,1000,fill='whitesmoke', outline='whitesmoke')
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
    c.create_rectangle(598, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    current_datetime = datetime.now() #строка 129 обновление времени
    c.create_text(669, 10, text=str(current_datetime))
    c.create_rectangle(702, 0, 750, 15, fill="whitesmoke", outline='whitesmoke')
    c.create_rectangle(598, 0, 655, 15, fill="whitesmoke", outline='whitesmoke') #строки 128-132 вывод нового времени: поверх старого значения рисуем прямоугольник цвета холста, затем выводим новое время
   # строки 110-133 функция очистки: на все поле рисется прямоугольник цвета холста, на котором рисуются графики, затем занаво рисуются оси 
x4=15; h=20
lb_f=Label(ger, text='функция',bg='silver')
lb_f.place(x=x4, y=210, width=50, height=h)
ent_f=Entry(ger)
ent_f.place(x=x4+10, y=240, width=120, height=h)
lb_i=Label(ger, text='y=',bg='silver')
lb_i.place(x=x4-10, y=240, width=15, height=h)
ent_y=Entry(c)
ent_y.place(x=360,y=0,width=50, height=h)
ent_x=Entry(c)
ent_x.place(x=650,y=310,width=50, height=h) #134-144 задание полей для ввода функции и подписей к осям.
bt1=Button(ger, text='построить график',bg='azure',fg='black',command=com1)
bt1.place(x=x4, y=270, width=120, height=h)
bt2=Button(ger, text='справка', command=com2,bg='azure',fg='black')
bt2.place(x=x4, y=300, width=120, height=h)
bt3=Button(ger, text='удалить все',command=com4,bg='azure',fg='black')
bt3.place(x=x4, y=330, width=120, height=h) #строки 145-151 задание кнопок отвечающих за построение графика, очистку и вызов справки
root.mainloop()
