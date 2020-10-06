from tkinter import *
from tkinter import font as f

window = Tk()
window.title('Calculator')

#font of our window application
helv12 = f.Font(family='Helvetica', size=12, weight='bold')

#Entry box
entry = Entry(window,borderwidth=5,width=40)
# entry.insert(0,'0')
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#operations
def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def clear():
    entry.delete(0,END)

def add():
    first_number = entry.get()
    global num1
    global math
    math = "addition"
    num1 = int(first_number)
    entry.delete(0,END)

def substract():
    first_number = entry.get()
    global num1
    global math
    math = "substraction"
    num1 = int(first_number)
    entry.delete(0,END)

def multiply():
    first_number = entry.get()
    global num1
    global math
    math = "multiplication"
    num1 = int(first_number)
    entry.delete(0,END)

def divide():
    first_number = entry.get()
    global num1
    global math
    math = "division"
    num1 = int(first_number)
    entry.delete(0,END)

def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if(math == "addition"):
        entry.insert(0,num1 + int(second_number))
    if(math == "substraction"):
        entry.insert(0,num1 - int(second_number))
    if (math == "multiplication"):
        entry.insert(0,num1 * int(second_number))
    if (math == "division"):
        entry.insert(0,num1/int(second_number))

#define digits
digit_btn_1 = Button(window,text='1',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(1))
digit_btn_2 = Button(window,text='2',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(2))
digit_btn_3 = Button(window,text='3',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(3))

digit_btn_4 = Button(window,text='4',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(4))
digit_btn_5 = Button(window,text='5',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(5))
digit_btn_6 = Button(window,text='6',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(6))

digit_btn_7 = Button(window,text='7',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(7))
digit_btn_8 = Button(window,text='8',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(8))
digit_btn_9 = Button(window,text='9',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(9))

digit_btn_0 = Button(window,text='0',padx=20,pady=10,font=helv12,borderwidth=3,bg='#fff',command=lambda: button_click(0))


#putting digits on screen
digit_btn_1.grid(row=1,column=0)
digit_btn_2.grid(row=1,column=1)
digit_btn_3.grid(row=1,column=2)
digit_btn_4.grid(row=2,column=0)
digit_btn_5.grid(row=2,column=1)
digit_btn_6.grid(row=2,column=2)
digit_btn_7.grid(row=3,column=0)
digit_btn_8.grid(row=3,column=1)
digit_btn_9.grid(row=3,column=2)
digit_btn_0.grid(row=4,column=1)

#operators buttons
button_add = Button(window,text='+',padx=20,pady=10,font=helv12,borderwidth=3,command=add)
button_substract = Button(window,text='-',padx=21,pady=10,font=helv12,borderwidth=3,command=substract)
button_multiply = Button(window,text='*',padx=20,pady=10,font=helv12,borderwidth=3,command=multiply)
button_divide = Button(window,text='/',padx=20,pady=10,font=helv12,borderwidth=3,command=divide)
button_clear = Button(window,text='C',padx=17,pady=10,font=helv12,borderwidth=3,command=clear)
button_percentage = Button(window,text='=',padx=18,pady=10,font=helv12,borderwidth=3,command=equal)

#putting operator buttons on screen
button_add.grid(row=4,column=0)
button_substract.grid(row=4,column=2)
button_multiply.grid(row=1,column=3)
button_divide.grid(row=2,column=3)
button_clear.grid(row=3,column=3)
button_percentage.grid(row=4,column=3)



window.mainloop()