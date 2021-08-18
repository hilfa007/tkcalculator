from tkinter import *
expression=""
window=Tk()

window.maxsize(height=330,width=462)
window.title("calculator")
window.configure(bg="light blue")



equation = StringVar()
textField = Entry(window,font=('times new roman', 18, 'bold'), textvariable=equation,bd=10)
textField.grid(columnspan=4,ipadx=100,ipady=20)



def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equals():
    global expression
    try:
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clr():
    global expression
    expression=""
    equation.set(expression)


bclr = Button(window,text="clear",command=lambda :clr(),height=2,width=5,bd=10)
button7 =Button(window,text="7",command=lambda :press(7),height=3,width=10)
button8 =Button(window,text="8",command=lambda :press(8),height=3,width=10)
button9 =Button(window,text="9",command=lambda :press(9),height=3,width=10)
buttonAdd =Button(window,text="+",command=lambda :press("+"),height=3,width=10)
button4 =Button(window,text="4",command=lambda :press(4),height=3,width=10)
button5 =Button(window,text="5",command=lambda :press(5),height=3,width=10)
button6 =Button(window,text="6",command=lambda :press(6),height=3,width=10)
buttonDiff =Button(window,text="-",command=lambda :press("-"),height=3,width=10)
button1 =Button(window,text="1",command=lambda :press(1),height=3,width=10)
button2 =Button(window,text="2",command=lambda :press(2),height=3,width=10)
button3 =Button(window,text="3",command=lambda :press(3),height=3,width=10)
buttondiv =Button(window,text="/",command=lambda :press("/"),height=3,width=10)
equal = Button(window, text='=',command=lambda :equals(), height=3, width=10)
buttonmul= Button(window, text='x',command=lambda :press("*"), height=3, width=10)
zero= Button(window, text="0",command=lambda :press(0), height=3, width=10)
decimal= Button(window, text=".",command=lambda :press("."), height=3, width=10)
decimal.grid(row=4, column=0)
zero.grid(row=4, column=1)
buttonmul.grid(row=4, column=3)
equal.grid(row=4, column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
buttonAdd.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonDiff.grid(row=2,column=3)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
buttondiv.grid(row=3,column=3)
bclr.grid(row=0,column=3)
Label(window, text = "welcome to tkinter calculator")



window.mainloop()