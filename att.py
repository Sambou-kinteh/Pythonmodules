from tkinter import Tk, StringVar, ttk
from tkinter import*
import time
import datetime
from tkinter import messagebox

root = Tk()
root.title('Attendance Register')
root.geometry('1350x650+0+0')
root.configure(background='black')
#----------------------------------Frames--------------------------------------#
LeftMayFrame = Frame(root, width=1000, height=650, bd=8, relief='raise')
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root, width=350, height=650, bd=8, relief='raise')
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=8, relief='raise')
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=550, bd=8, relief='raise')
LeftMayFrame2.pack(side=TOP)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=215, bd=8, relief='raise')
RightMayFrame1.pack(side=TOP)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=415, bd=8, relief='raise')
RightMayFrame2.pack(side=TOP)

#------------------------------------------------------------------------#
cont1 = Canvas(RightMayFrame2, width=350,height=425, bg='black')
cont1.grid(row=0,column=0)
image5 = PhotoImage(file='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON_PL/images/pic1.png')
cont1.create_image(200,200, image= image5)
#------------------------------------------------------------------------#
cont = Canvas(RightMayFrame1, width = 350,height = 215)
cont.grid(row=0,column=0)
image1 = PhotoImage(file='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON_PL/images/pic1.png')
#image = cont.create_image(200,200, image = image1)

def pic1():
    image = cont.create_image(200,200, image = image1)

image2 = PhotoImage(file='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON_PL/images/pic1.png')

def pic2():
    image = cont.create_image(200,200, image = image2)

image3 = PhotoImage(file='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON_PL/images/pic1.png')

def pic3():
    image = cont.create_image(200,200, image = image3)

image4 = PhotoImage(file='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON_PL/images/pic1.png')

def pic4():
    image = cont.create_image(200,200, image = image4)



#----------------------------------Var--------------------------------------#
DateofOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()

def fill():
    if (value0.get() == 'Present'):
        value1.set("Present")
        value2.set("Present")
        value3.set("Present")
        value4.set("Present")
        value5.set("Present")
        value6.set("Present")
        value7.set("Present")
        value8.set("Present")
        value9.set("Present")
        value10.set("Present")
        value11.set("Present")
        value12.set("Present")

    elif (value0.get() == 'Sick'):
        value1.set("Sick")
        value2.set("Sick")
        value3.set("Sick")
        value4.set("Sick")
        value5.set("Sick")
        value6.set("Sick")
        value7.set("Sick")
        value8.set("Sick")
        value9.set("Sick")
        value10.set("Sick")
        value11.set("Sick")
        value12.set("Sick")

    elif (value0.get() == 'Late'):
        value1.set("Late")
        value2.set("Late")
        value3.set("Late")
        value4.set("Late")
        value5.set("Late")
        value6.set("Late")
        value7.set("Late")
        value8.set("Late")
        value9.set("Late")
        value10.set("Late")
        value11.set("Late")
        value12.set("Late")

    elif (value0.get() == 'Absent'):
        value1.set("Absent")
        value2.set("Absent")
        value3.set("Absent")
        value4.set("Absent")
        value5.set("Absent")
        value6.set("Absent")
        value7.set("Absent")
        value8.set("Absent")
        value9.set("Absent")
        value10.set("Absent")
        value11.set("Absent")
        value12.set("Absent")

    elif (value0.get() == ' '):
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        value10.set(" ")
        value11.set(" ")
        value12.set(" ")
    return
        

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")

def qExit():
    qExit = messagebox.askyesno('Exit System', 'Do you want to quit')
    if qExit > 0:
        root.destroy()
        return

#----------------------------------Components--------------------------------------#
DateofOrder.set(time.strftime('%d/%m/%Y'))
#----------------------------------LeftMayFrame1--------------------------------------#

lblNo = Label(LeftMayFrame1,font=('arial',10,'bold'), text='No.', bd=16) 
lblNo.grid(row=0, column=0, sticky=W)
lblStudentNo = Label(LeftMayFrame1,font=('arial',10,'bold'), text='Student No.',bd=16)
lblStudentNo.grid(row=0,column=1,sticky=W)
lblStudentName = Label(LeftMayFrame1,font=('arial',10,'bold'), text='Student Name', bd=16)
lblStudentName.grid(row=0, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame1,font=('arial',10,'bold'), text='Course Code', bd=16)
lblCourseCode.grid(row=0, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame1, textvariable=value0, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=0,column=4)

btnFill = Button(LeftMayFrame1, text='Fill', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1,command=fill).grid(row=0,column=5)

btnReset = Button(LeftMayFrame1, text='Reset', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1,command=Reset).grid(row=0,column=6)

btnExit = Button(LeftMayFrame1, text='Exit', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1,command=qExit).grid(row=0,column=7)

lblDateofOrder= Label(LeftMayFrame1,font=('arial',10,'bold'),textvariable=DateofOrder,padx=2,
                      pady=2,bd=2, fg='black', bg='white', relief='sunken')
lblDateofOrder.grid(row=0,column=8,sticky=W)
#----------------------------------LeftMayFrame2 row1--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1', bd=16) 
lblNo.grid(row=0, column=0, sticky=W)
lblstudentNo_1 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1223',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_1.grid(row=0,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Sam Kinteh', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=0, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0001', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=0, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=0,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=0,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=0,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=0,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=0,column=8)


#----------------------------------LeftMayFrame2 row2--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='2', bd=16) 
lblNo.grid(row=1, column=0, sticky=W)
lblstudentNo_2 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1224',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_2.grid(row=1,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Ara Kinteh', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=1, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0001', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=1, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=1,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=1,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=1,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=1,column=8)


#----------------------------------LeftMayFrame2 row3--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='3', bd=16) 
lblNo.grid(row=2, column=0, sticky=W)
lblstudentNo_3 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1225',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_3.grid(row=2,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Ara junior Kinteh', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=2, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0001', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=2, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value3, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=2,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=2,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=2,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=2,column=8)


#----------------------------------LeftMayFrame2 row4--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='4', bd=16) 
lblNo.grid(row=3, column=0, sticky=W)
lblstudentNo_4 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1226',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_4.grid(row=3,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Sam junior Kinteh', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=3, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0001', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=3, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value4, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=3,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=3,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=3,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=3,column=8)


#----------------------------------LeftMayFrame2 row5--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='5', bd=16) 
lblNo.grid(row=4, column=0, sticky=W)
lblstudentNo_5 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1228',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_5.grid(row=4,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Desire Ezeh', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=4, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0002', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=4, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value5, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=4,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=4,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=4,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=4,column=8)


#----------------------------------LeftMayFrame2 row6--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='6', bd=16) 
lblNo.grid(row=5, column=0, sticky=W)
lblstudentNo_6 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1229',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_6.grid(row=5,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Pa seedy Trawally', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=5, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0002', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=5, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value6, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=5,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=5,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=5,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=5,column=8)


#----------------------------------LeftMayFrame2 row7--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='7', bd=16) 
lblNo.grid(row=6, column=0, sticky=W)
lblstudentNo_7 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1230',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_7.grid(row=6,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Habib Choi', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=6, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0002', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=6, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value7, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=6,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=6,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=6,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=6,column=8)

#----------------------------------LeftMayFrame2 row8--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='8', bd=16) 
lblNo.grid(row=7, column=0, sticky=W)
lblstudentNo_8 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1231',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_8.grid(row=7,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Joakim Mendy', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=7, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0003', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=7, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value8, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=7,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=7,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=7,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=7,column=8)

#----------------------------------LeftMayFrame2 row9--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='3', bd=16) 
lblNo.grid(row=8, column=0, sticky=W)
lblstudentNo_9 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1232',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_9.grid(row=8,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Bakary Faux', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=8, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0003', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=8, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value9, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=8,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=8,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=8,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=8,column=8)

#----------------------------------LeftMayFrame2 row10--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='10', bd=16) 
lblNo.grid(row=9, column=0, sticky=W)
lblstudentNo_10 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1233',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_10.grid(row=9,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Joseph Jabang', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=9, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0003', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=9, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value10, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=9,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=9,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=9,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=9,column=8)

#----------------------------------LeftMayFrame2 row11--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='11', bd=16) 
lblNo.grid(row=10, column=0, sticky=W)
lblstudentNo_11 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1234',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_11.grid(row=10,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Tida Bah', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=10, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0004', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=10, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value11, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=10,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=10,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=10,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=10,column=8)

#----------------------------------LeftMayFrame2 row12--------------------------------------#
lblNo = Label(LeftMayFrame2,font=('arial',10,'bold'), text='12', bd=16) 
lblNo.grid(row=11, column=0, sticky=W)
lblstudentNo_12 = Label(LeftMayFrame2,font=('arial',10,'bold'), text='1235',bd=2,padx=2,pady=2,fg='black',width=18)
lblstudentNo_12.grid(row=11,column=1,sticky=W)
lblstudentName = Label(LeftMayFrame2,font=('arial',10,'bold'), text='Ali Sarr', bd=2,padx=2,pady=2,fg='black',width=12)
lblstudentName.grid(row=11, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame2,font=('arial',10,'bold'), text='0006', bd=2,padx=2,pady=2,fg='black',width=12)
lblCourseCode.grid(row=11, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value12, state='readonly')
box['values'] = ('','Present','Late','Absent','Sick')
box.current(0)
box.grid(row=11,column=4)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=5)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=11,column=6)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=11,column=7)

btnspace = Button(LeftMayFrame2, text='', padx=2,pady=2,bd=2,fg='black',
                  font=('arial',10,'bold'),width=11,height=1).grid(row=11,column=8)
#---------------------------------- --------------------------------------#







root.mainloop()
