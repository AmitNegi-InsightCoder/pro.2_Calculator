from tkinter import *
from tkinter.messagebox import *
import math as m
# some useful variables:
font = ("cooper", 18, 'bold')

# some import functions (for binding buttons with function)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0,END)







def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == 'X':
        textField.insert(END,"*")
        return

    if text == 'AC':
        textField.insert(END, "")
        return

    if text == 'Back':
        textField.insert(END,"")
        return




    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("error...", e)
            showerror("Error",e)
        return



    textField.insert(END,text)






# creating a window
window = Tk()
window.title('my calculator')
window.geometry('475x530')

# picture label
pic = PhotoImage(file="D:\Amit's System\D drive\PROJECTS\calc_youtube\img\cal2R.png")
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP)

# Heading Label
Heading = Label(window, text='AN Calculator', font=font)
Heading.pack(side=TOP)

# text field
textField=Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=15, fill=X, padx=15)

# Buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

# adding button

# btn1 = Button(buttonFrame, text="1", font=font)
# btn1.grid(row=0, column=0)                                          this is one of the method but we will use loop

# btn2 = Button(buttonFrame, text="2", font=font)
# btn2.grid(row=0, column=1)

temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame,text=str(temp), font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
        btn.grid(row=i, column=j, padx=5, pady=5)
        temp +=1
        btn.bind('<Button-1>', click_btn_function)

zerobtn = Button(buttonFrame,text='0', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
zerobtn.grid(row=3, column=0, padx=5, pady=5)

dotbtn = Button(buttonFrame,text='.', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
dotbtn.grid(row=3, column=1, padx=5, pady=5)

equalbtn = Button(buttonFrame,text='=', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
equalbtn.grid(row=3, column=2, padx=5, pady=5)

plusbtn = Button(buttonFrame,text='+', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
plusbtn.grid(row=0, column=3, padx=5, pady=5)

minusbtn = Button(buttonFrame,text='-', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
minusbtn.grid(row=1, column=3, padx=5, pady=5)

multbtn = Button(buttonFrame,text='X', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
multbtn.grid(row=2, column=3, padx=5, pady=5)

dividebtn = Button(buttonFrame,text='/', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
dividebtn.grid(row=3, column=3, padx=5, pady=5)

backbtn = Button(buttonFrame,text='Back', font=font, width=12, relief='ridge', activebackground='orange', activeforeground='white', command=clear)
backbtn.grid(row=4, column=0,columnspan=2, padx=5, pady=5)

Allclrbtn = Button(buttonFrame,text='AC', font=font, width=12, relief='ridge', activebackground='orange', activeforeground='white', command= all_clear)
Allclrbtn.grid(row=4, column=2,columnspan=2,padx=5, pady=5)

# all btn binding with their function
plusbtn.bind('<Button-1>', click_btn_function)
minusbtn.bind('<Button-1>', click_btn_function)
multbtn.bind('<Button-1>', click_btn_function)
dividebtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
backbtn.bind('<Button-1>', click_btn_function)
Allclrbtn.bind('<Button-1>', click_btn_function)
dotbtn.bind('<Button-1>', click_btn_function)
equalbtn.bind('<Button-1>', click_btn_function)

def enterClick(event):
    print("hii..")
    e= Event()
    e.widget = equalbtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)


#########################################################################################################################################
# functions of second video(scientific calculator)
scFrame= Frame(window)
sqrtbtn = Button(scFrame,text='√', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
sqrtbtn.grid(row=0, column=0, padx=5, pady=5)

powbtn = Button(scFrame,text='^', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
powbtn.grid(row=0, column=1, padx=5, pady=5)

factbtn = Button(scFrame,text='x!', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
factbtn.grid(row=0, column=2, padx=5, pady=5)

radbtn = Button(scFrame,text='rad ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
radbtn.grid(row=0, column=3, padx=5, pady=5)

degreebtn = Button(scFrame,text='degree', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
degreebtn.grid(row=1, column=0, padx=5, pady=5)

sinbtn = Button(scFrame,text='sinθ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
sinbtn.grid(row=1, column=1, padx=5, pady=5)

cosbtn = Button(scFrame,text='cosθ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
cosbtn.grid(row=1, column=2, padx=5, pady=5)

tanbtn = Button(scFrame,text='tanθ', font=font, width=5, relief='ridge', activebackground='orange', activeforeground='white')
tanbtn.grid(row=1, column=3, padx=5, pady=5)


def calculate_sc(event):
    print("btn...")
    btn=event.widget
    text=btn["text"]
    print(text)
    ex= textField.get()
    answer=''

    if text == 'rad':
        print("Hello")

    elif text== 'degree':
        print("calculate degree")
        answer=str(m.degrees(float(ex)))

    elif text=='x!':
        print("calculate factorial")
        answer = str(m.factorial(int(ex)))

    elif text=='√':
        print("calculate sqrt")
        answer = str(m.sqrt(int(ex)))

    elif text=='^':
        print("calculate power")
        base,pow = ex.split(",")
        print(base)
        print(pow)
        answer= m.pow(int(base),int(pow))

    elif text=='sinθ':
        print("calculate sinθ")
        answer = str(m.sin(m.radians(int(ex))))

    elif text=='cosθ':
        print("calculate cosθ")
        answer = str(m.sin(m.radians(int(ex))))

    elif text=='tanθ':
        print("calculate tanθ")
        answer = str(m.sin(m.radians(int(ex))))

    textField.delete(0, END)
    textField.insert(0,answer)






normalcalc = True

def sc_click():
    global normalcalc
    if normalcalc:
        #sc...
        buttonFrame.pack_forget()
        #add scFrame
        scFrame.pack(side=TOP, pady=10)
        buttonFrame.pack(side=TOP, padx=2)
        window.geometry('475x630')

        print("show sc")
        normalcalc= False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry('475x530')
        normalcalc=True






# end functions
#binding sc calculator's button
sqrtbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
degreebtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)

fontMenu=('',14)
menubar=Menu(window)
mode=Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="scientific calculator", command=sc_click)

menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)


window.mainloop()
  
