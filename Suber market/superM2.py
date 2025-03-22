
from tkinter import *
from tkinter import messagebox
import math , random , os

class super:
    def __init__(self, window) -> None:
        self.window = window
        self.window.geometry('1300x735+30+10')
        self.window.title("Super Market")
        self.window.resizable(False,False)
        self.window.iconbitmap("supermarket_icons.ico")
        title = Label(window, text="Hellow In Super Market System!", fg="white", bg="#0B2F3A", font=('tajawal', 15))
        title.pack(fill=X)
        #=========ALL VARIABLES ============
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        self.q11 = IntVar()
        self.q12 = IntVar()
        self.q13 = IntVar()
        self.q14 = IntVar()
        self.q15 = IntVar()
        self.q16 = IntVar()
        #==============----==============
        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
        self.qq8 = IntVar()
        self.qq9 = IntVar()
        self.qq10 = IntVar()
        self.qq11 = IntVar()
        self.qq12 = IntVar()
        self.qq13 = IntVar()
        self.qq14 = IntVar()
        self.qq15 = IntVar()
        self.qq16 = IntVar()
        #==============-------=============
        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        self.qqq8 = IntVar()
        self.qqq9 = IntVar()
        self.qqq10 = IntVar()
        self.qqq11 = IntVar()
        self.qqq12 = IntVar()
        self.qqq13 = IntVar()
        #_______متغيرات حساب المشتري _______
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        x = random.randint(1000,9999)
        self.fatora.set(str(x))




        #_______متغيرات الحساب الكلي _______
        self.bacoliat= StringVar()
        self.adoat= StringVar()
        self.kahraba = StringVar()




        # Customer DATA

        f1 = Frame(window, bd=2, width=378 , height=190, bg="#0B4C5F")
        f1.place(x=920, y= 30)
        tit = Label(f1, text=": بيانات المشتري ", font=('tajawal',16, 'bold'), bg='#0B4C5F' , fg='tomato')
        tit.place(x= 245, y=0)
        has_name = Label(f1, text=": اسم المشتري", font=('tajawal', 13), bg='#0B4C5F', fg='white')
        has_name.place(x=277, y=40)
        has_name = Label(f1, text=": رقم المشتري", font=('tajawal', 13), bg='#0B4C5F', fg='white')
        has_name.place(x=279, y=80)
        has_name = Label(f1, text=": رقم الفاتوره", font=('tajawal', 13), bg='#0B4C5F', fg='white')
        has_name.place(x=285, y=120)
        entry1 = Entry(f1,font=('tajawal', 12), textvariable= self.namo, justify='center')
        entry1.place(x=95, y=43)
        entry2 = Entry(f1,font=('tajawal', 12), textvariable= self.phono, justify='center')
        entry2.place(x=95, y=83)
        entry3 = Entry(f1,font=('tajawal', 12), textvariable= self.fatora, justify='center')
        entry3.place(x=95, y=123)
        button_research =Button(f1, text='بحث' , height=6 ,width=11)
        button_research.place(x= 2 , y= 44)
        titedd = Label(f1 , text='[الفواتير]', font=('tajawal', 15 , 'bold'), bg='#0B4C5F', fg='gold')
        titedd.place(x= 175 , y=159)
        # Two Frame From Apperance Bill
        f3 = Frame(window , width=378, height=400, bg='white')
        f3.place(x=920 , y=222)
        # Make Scroll
        scrol_y = Scrollbar(f3, orient=VERTICAL)
        self.textarea = Text(f3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side= LEFT, fill= Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        #Frame From Brice
        # Button
        f4 = Frame(window, bd=2, width=684 ,height=119, bg='#0B4C5F')
        f4.place(x=613 ,y=615)
        hesab = Button(f4, text='الحساب', font=('tajawal',16,'bold'), bg='gold', width=8 , command=self.total )
        hesab.place(x=535 , y=5 )
        fatora = Button(f4, text='تصدير الفاتوره', font=('tajawal',16,'bold'), bg='gold', width=8,command= self.billiding )
        fatora.place(x=535 , y=60 )
        clear = Button(f4, text='افراغ الحقول ', font=('tajawal',16,'bold'), bg='gold', width=8, command=self.clear )
        clear.place(x=415 , y=5 )
        exit = Button(f4, text='اغلاق البرنامج ', font=('tajawal',16,'bold'), bg='gold', width=8, command=self.close )
        exit.place(x=415 , y=60 )
        # lable
        labo1 = Label(f4, text='حساب الكلي للبقوليات', font=('tajawal',12,'bold') , bg='#0B4C5F', fg='gold')
        labo1.place(x=200, y=7 )
        labo2 = Label(f4, text='حساب اللوازم المنزليه', font=('tajawal',12,'bold') , bg='#0B4C5F', fg='gold')
        labo2.place(x=200, y=44 )
        labo3 = Label(f4, text='حساب الادوات الكهربيه ', font=('tajawal',12,'bold') , bg='#0B4C5F', fg='gold')
        labo3.place(x=200, y=80 )
        #ُ Entry 
        ento1 = Entry(f4, textvariable= self.bacoliat ,justify='center')
        ento1.place(x=30, y=7)
        ento2 = Entry(f4, textvariable= self.adoat, justify='center')
        ento2.place(x=30,y=44)
        ento3 = Entry(f4,textvariable= self.kahraba , justify='center')
        ento3.place(x=30, y=80 )

        #  =========ITEMS==========
        ff1 = Frame(window, bd= 2 , width= 305, height=704, bg='#0B4C5F')
        ff1.place(x=1 , y=30)
        bq0 = Label (ff1 , text="البقوليات", font=('tajawal', 16, 'bold'), fg="gold", bg="#0B4C5F")
        bq0.place(x=110 , y=1)
        bq1 = Label(ff1, text="الارز", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq1.place(x=220 , y=50)
        bq2 = Label(ff1, text="العدس", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq2.place(x=220 , y=90)
        bq3 = Label(ff1, text="الفصوليا", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq3.place(x=220 , y=130)
        bq4 = Label(ff1, text="اللوبيا", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq4.place(x=220 , y=170)
        bq5 = Label(ff1, text="المعكرونه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq5.place(x=220 , y=210)
        bq6 = Label(ff1, text="البيض", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq6.place(x=220 , y=250)
        bq7 = Label(ff1, text="اللحم", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq7.place(x=220 , y=290)
        bq8 = Label(ff1, text="الفراخ", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq8.place(x=220 , y=330)
        bq9 = Label(ff1, text="الملح", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq9.place(x=220 , y=370)
        bq10 = Label(ff1, text="البرغل", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq10.place(x=220 , y=410)
        bq11 = Label(ff1, text="الفاكهه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq11.place(x=220 , y=450)
        bq12 = Label(ff1, text="الزنجبيل", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq12.place(x=220 , y=490)
        bq13 = Label(ff1, text="البهارات", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq13.place(x=220 , y=530)
        bq14 = Label(ff1, text="البسكويت", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq14.place(x=220 , y=570)
        bq15= Label(ff1, text="الشبسي", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq15.place(x=220 , y=610)
        bq16 = Label(ff1, text="الكنزات", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq16.place(x=220 , y=650)
        # ============ALL ENTRY==============
        
        bq1 = Entry(ff1,textvariable=self.q1 , justify='left' )
        bq1.place(x=30 , y=53)
        bq2 = Entry(ff1,textvariable=self.q2 , justify='left' )
        bq2.place(x=30 , y=93)
        bq3 = Entry(ff1,textvariable=self.q3 , justify='left' )
        bq3.place(x=30 , y=133)
        bq4 = Entry(ff1,textvariable=self.q4 , justify='left' )
        bq4.place(x=30 , y=173)
        bq5 = Entry(ff1,textvariable=self.q5, justify='left' )
        bq5.place(x=30 , y=213)
        bq6 = Entry(ff1,textvariable=self.q6 , justify='left' )
        bq6.place(x=30 , y=253)
        bq7 = Entry(ff1,textvariable=self.q7 , justify='left' )
        bq7.place(x=30 , y=293)
        bq8 = Entry(ff1,textvariable=self.q8 , justify='left' )
        bq8.place(x=30 , y=333)
        bq9 = Entry(ff1,textvariable=self.q9 , justify='left' )
        bq9.place(x=30 , y=373)
        bq20 = Entry(ff1,textvariable=self.q10 , justify='left' )
        bq20.place(x=30 , y=413)
        bq21 = Entry(ff1,textvariable=self.q11 , justify='left' )
        bq21.place(x=30 , y=453)
        bq22 = Entry(ff1,textvariable=self.q12 , justify='left' )
        bq22.place(x=30 , y=493)
        bq23 = Entry(ff1,textvariable=self.q13 , justify='left' )
        bq23.place(x=30 , y=533)
        bq24 = Entry(ff1,textvariable=self.q14 , justify='left' )
        bq24.place(x=30 , y=573)
        bq25= Entry(ff1,textvariable=self.q15 , justify='left' )
        bq25.place(x=30 , y=613)
        bq26 = Entry(ff1 ,textvariable=self.q16 , justify='left')
        bq26.place(x=20 , y=653)
        # Frame From two
        ff2 = Frame(window, bd= 2 , width= 305, height=704, bg='#0B4C5F')
        ff2.place(x=307 , y=30)


        bq0 = Label (ff2 , text="اللوازم المنزليه ", font=('tajawal', 16, 'bold'), fg="gold", bg="#0B4C5F")
        bq0.place(x=110 , y=1)
        bq10 = Label(ff2, text="غساله", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq10.place(x=220 , y=50)
        bq20 = Label(ff2, text="بوتجاز", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq20.place(x=220 , y=90)
        bq30 = Label(ff2, text="خلاط", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq30.place(x=220 , y=130)
        bq40 = Label(ff2, text="ثلاجه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq40.place(x=220 , y=170)
        bq50 = Label(ff2, text="شاشه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq50.place(x=220 , y=210)
        bq60 = Label(ff2, text="لابتوب", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq60.place(x=220 , y=250)
        bq70 = Label(ff2, text="اطباق", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq70.place(x=220 , y=290)
        bq80 = Label(ff2, text="تكييف", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq80.place(x=220 , y=330)
        bq90 = Label(ff2, text="مكوه ", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq90.place(x=220 , y=370)
        bq20 = Label(ff2, text="فرن", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq20.place(x=220 , y=410)
        bq21 = Label(ff2, text="غلايه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq21.place(x=220 , y=450)
        bq22 = Label(ff2, text="فريزر", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq22.place(x=220 , y=490)
        bq23 = Label(ff2, text="شوكه  ", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq23.place(x=220 , y=530)
        bq24 = Label(ff2, text="مطبخ", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq24.place(x=220 , y=570)
        bq25= Label(ff2, text="ملعقه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq25.place(x=220 , y=610)
        bq26 = Label(ff2, text="سكينه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        bq26.place(x=220 , y=650)
        # ============ALL ENTRY==============
        
        bq10 = Entry(ff2,textvariable=self.qq1 , justify='left' )
        bq10.place(x=30 , y=53)
        bq20 = Entry(ff2,textvariable=self.qq2 , justify='left' )
        bq20.place(x=30 , y=93)
        bq30 = Entry(ff2,textvariable=self.qq3 , justify='left' )
        bq30.place(x=30 , y=133)
        bq40 = Entry(ff2,textvariable=self.qq4 , justify='left' )
        bq40.place(x=30 , y=173)
        bq50 = Entry(ff2,textvariable=self.qq5 , justify='left' )
        bq50.place(x=30 , y=213)
        bq60 = Entry(ff2,textvariable=self.qq6 , justify='left' )
        bq60.place(x=30 , y=253)
        bq70 = Entry(ff2,textvariable=self.qq7 , justify='left' )
        bq70.place(x=30 , y=293)
        bq80 = Entry(ff2,textvariable=self.qq8 , justify='left' )
        bq80.place(x=30 , y=333)
        bq90 = Entry(ff2,textvariable=self.qq9 , justify='left' )
        bq90.place(x=30 , y=373)
        bq20 = Entry(ff2,textvariable=self.qq10 , justify='left' )
        bq20.place(x=30 , y=413)
        bq21 = Entry(ff2,textvariable=self.qq11 , justify='left' )
        bq21.place(x=30 , y=453)
        bq22 = Entry(ff2,textvariable=self.qq12 , justify='left' )
        bq22.place(x=30 , y=493)
        bq23 = Entry(ff2,textvariable=self.qq13 , justify='left' )
        bq23.place(x=30 , y=533)
        bq24 = Entry(ff2,textvariable=self.qq14 , justify='left' )
        bq24.place(x=30 , y=573)
        bq25= Entry(ff2,textvariable=self.qq15 , justify='left' )
        bq25.place(x=30 , y=613)
        bq27 = Entry(ff2,textvariable=self.qq16 , justify='left')
        bq27.place(x=30 , y=653)

        # Frame Frame Three
        ff5 = Frame(window, bd= 2 , width= 304 , height=583, bg="#0B4C5F")
        ff5.place(x=614 , y=30)

        dq0 = Label (ff5 , text="الادوات الكهربيه", font=('tajawal', 16, 'bold'), fg="gold", bg="#0B4C5F")
        dq0.place(x=110 , y=1)
        dq1 = Label(ff5, text="الارز", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq1.place(x=220 , y=50)
        dq2 = Label(ff5, text="العدس", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq2.place(x=220 , y=90)
        dq3 = Label(ff5, text="الفصوليا", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq3.place(x=220 , y=130)
        dq4 = Label(ff5, text="اللوبيا", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq4.place(x=220 , y=170)
        dq5 = Label(ff5, text="المعكرونه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq5.place(x=220 , y=210)
        dq6 = Label(ff5, text="البيض", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq6.place(x=220 , y=250)
        dq7 = Label(ff5, text="اللحم", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq7.place(x=220 , y=290)
        dq8 = Label(ff5, text="الفراخ", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq8.place(x=220 , y=330)
        dq9 = Label(ff5, text="الملح", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq9.place(x=220 , y=370)
        dq10 = Label(ff5, text="البرغل", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq10.place(x=220 , y=410)
        dq11 = Label(ff5, text="الفاكهه", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq11.place(x=220 , y=450)
        dq12 = Label(ff5, text="الزنجبيل", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq12.place(x=220 , y=490)
        dq13 = Label(ff5, text="البهارات", font=('tajawal', 13), fg="gold", bg="#0B4C5F")
        dq13.place(x=220 , y=530)

        # ENTRY FROM FRAM THREE
        dq10 = Entry(ff5,textvariable=self.qqq1 , justify='left' )
        dq10.place(x=30 , y=53)
        dq20 = Entry(ff5,textvariable=self.qqq2 , justify='left' )
        dq20.place(x=30 , y=93)
        dq30 = Entry(ff5,textvariable=self.qqq3 , justify='left' )
        dq30.place(x=30 , y=133)
        dq40 = Entry(ff5,textvariable=self.qqq4 , justify='left' )
        dq40.place(x=30 , y=173)
        dq50 = Entry(ff5,textvariable=self.qqq5 , justify='left' )
        dq50.place(x=30 , y=213)
        dq60 = Entry(ff5,textvariable=self.qqq6 , justify='left' )
        dq60.place(x=30 , y=253)
        dq70 = Entry(ff5,textvariable=self.qqq7 , justify='left' )
        dq70.place(x=30 , y=293)
        dq80 = Entry(ff5,textvariable=self.qqq8 , justify='left' )
        dq80.place(x=30 , y=333)
        dq90 = Entry(ff5,textvariable=self.qqq9 , justify='left' )
        dq90.place(x=30 , y=373)
        dq20 = Entry(ff5,textvariable=self.qqq10 , justify='left' )
        dq20.place(x=30 , y=413)
        dq21 = Entry(ff5,textvariable=self.qqq11 , justify='left' )
        dq21.place(x=30 , y=453)
        dq22 = Entry(ff5,textvariable=self.qqq12 , justify='left' )
        dq22.place(x=30 , y=493)
        dq23 = Entry(ff5,textvariable=self.qqq13 , justify='left' )
        dq23.place(x=30 , y=533)
        # =========START RUNNING FUNICTION WELLCOME ==================
        self.welcome()

    # =============== MAKE FUNCTION TO COLLECT TOTAL PRICE ================
    def total(self):

        # ===============COLLEECT BACOLIAT PRICE =====================
        self.rez = self.q1.get() *1.5
        self.progal = self.q2.get() *1.5
        self.tomato = self.q3.get() *1.5
        self.meet = self.q4.get() *1.5
        self.tee = self.q5.get() *1.5
        self.paharat = self.q6.get() *1.5
        self.quzpara = self.q7.get() *1.5
        self.pental = self.q8.get() *1.5
        self.meat = self.q9.get() *1.5
        self.milk = self.q10.get() *1.5
        self.salt = self.q11.get() *1.5
        self.vegtabols = self.q12.get() *1.5
        self.pasta = self.q13.get() *1.5
        self.lgenat = self.q14.get() *1.5
        self.helal = self.q15.get() *1.5
        self.suger = self.q16.get() *1.5
        self.bacoliats = float(
            self.rez+
            self.progal+
            self.tomato+
            self.meet +
            self.tee+
            self.paharat+
            self.quzpara+
            self.pental+
            self.meat+
            self.milk+
            self.salt +
            self.vegtabols+
            self.pasta+
            self.lgenat+
            self.helal+
            self.suger
        )
        self.bacoliat.set(str(self.bacoliats)+' $ ')


        # ===============COLLEECT ADWAT  PRICE =====================

        self.rez = self.qq1.get() *2
        self.progal = self.qq2.get() *2
        self.tomato = self.qq3.get() *2
        self.meet = self.qq4.get() *2
        self.tee = self.qq5.get() *2
        self.paharat = self.qq6.get() *2
        self.quzpara = self.qq7.get() *2
        self.pental = self.qq8.get() *2
        self.meat = self.qq9.get() *2
        self.milk = self.qq10.get() *2
        self.salt = self.qq11.get() *2
        self.vegtabols = self.qq12.get() *2
        self.pasta = self.qq13.get() *2
        self.lgenat = self.qq14.get() *12
        self.helal = self.qq15.get() *12
        self.suger = self.qq16.get() *12
        self.kahrabo = float(
            self.rez+
            self.progal+
            self.tomato+
            self.meet +
            self.tee+
            self.paharat+
            self.quzpara+
            self.pental+
            self.meat+
            self.milk+
            self.salt +
            self.vegtabols+
            self.pasta+
            self.lgenat+
            self.helal+
            self.suger
        )
        self.kahraba.set(str(self.kahrabo)+' $ ')



        # ===============COLLEECT KAHRAPA PRICE =====================

        self.rez = self.qqq1.get() *22
        self.progal = self.qqq2.get() *22
        self.tomato = self.qqq3.get() *25
        self.meet = self.qqq4.get() *27
        self.tee = self.qqq5.get() *29
        self.paharat = self.qqq6.get() *23
        self.quzpara = self.qqq7.get() *23
        self.pental = self.qqq8.get() *29
        self.meat = self.qqq9.get() *29
        self.milk = self.qqq10.get() *24
        self.salt = self.qqq11.get() *23
        self.vegtabols = self.qqq12.get() *22
        self.pasta = self.qqq13.get() *21
        self.adoato = float(
            self.rez+
            self.progal+
            self.tomato+
            self.meet +
            self.tee+
            self.paharat+
            self.quzpara+
            self.pental+
            self.meat+
            self.milk+
            self.salt +
            self.vegtabols+
            self.pasta+
            self.lgenat
        )
        self.adoat.set(str(self.adoato)+' $ ')
        self.all= float(
            self.bacoliats+
            self.kahrabo+
            self.adoato
            )
        # ================ MAKE FUNNICTION WELCOME TO WRIGHT FATORA ==================
    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END ,'\t سوبر ماركت ابو سالم يرحب بكم ')
        self.textarea.insert(END , '\n ==================================')
        self.textarea.insert(END , f'\n\t B.NUM  : {self.fatora.get()}')
        self.textarea.insert(END , f'\n\t NAME  : {self.namo.get()}')
        self.textarea.insert(END , f'\n\t PHONE  : {self.phono.get()}')
        self.textarea.insert(END , f'\n السعر\t     العدد\t      المشتريات\t ')
        self.textarea.insert(END , '\n===================================')
    # ===============MAKE FUNCTION CLEAR TO CLEAR ALL DATA  =====================
    
    def clear(self):
        pass
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)

        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0) 
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)

        self.bacoliat.set(0)
        self.kahraba.set(0)
        self.adoat.set(0)

        self.namo.set(' ')
        self.fatora.set(' ')
        self.phono.set(' ')
        # ================ MAKE FUNCTION CLOSR TO CLOSE PROGRAM ============        
    def close(self):
        self.window.destroy()

    def savee(self):
        op = messagebox.askyesno('save', 'Are You Sure Save Fatora!?')
        if op > 0 :
            self.bb == self.textarea.get('1.0', END)
            f1 = open('bue'+str(self.fatora.get())+'.txt', 'w', encoding="utf-8")
            f1.write(self.bb)
            f1.close()
        else:
            return 
        
    def billiding(self):
        self.textarea.insert(END , f'\n\t B.NUM  : {self.fatora.get()}')

        if self.namo.get() == '' or self.phono.get()== '':
            messagebox.showerror('Errors', "Don't Enable The Field Name And Number Is Empty")
        elif self.bacoliat.get()=='0.0 $' and self.adoat.get() == '0.0 $' and self.kahraba.get() == '0.0 $':
            messagebox.showerror("Invallid","Don't Enable All fildes Empty")
        else:
            self.welcome()
            if self.q1.get() !=0:
                self.textarea.insert(END,f"\n {self.rez}\t\t{self.q1.get()}\t\tالرز")
            if self.q2.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q2.get()}\t\tالعدس")
            if self.q3.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q3.get()}\t\tالفصوليا")
            if self.q4.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q4.get()}\t\tاللوبيا")
            if self.q5.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q5.get()}\t\tالمعكرونه")
            if self.q6.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q6.get()}\t\tالبيض")
            if self.q7.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q7.get()}\t\tاللحم")
            if self.q8.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q8.get()}\t\tالفراخ")
            if self.q9.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q9.get()}\t\tالملح")
            if self.q10.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q10.get()}\t\tالبرغل")
            if self.q11.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q11.get()}\t\tالفاكهه")
            if self.q12.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q12.get()}\t\tالزنجبيل")
            if self.q13.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q13.get()}\t\tالبهارات")
            if self.q14.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q14.get()}\t\tالبسكويت")
            if self.q15.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q15.get()}\t\tالشبسي")
            if self.q16.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.q16.get()}\t\tالكنزات")
            #============================================================================
            if self.qq1.get() !=0:
                self.textarea.insert(END,f"\n {self.rez}\t\t{self.qq1.get()}\t\tغساله")
            if self.qq2.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq2.get()}\t\tبوتجاز")
            if self.qq3.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq3.get()}\t\tخلاط")
            if self.qq4.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq4.get()}\t\tثلاجه")
            if self.qq5.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq5.get()}\t\tشاشه")
            if self.qq6.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq6.get()}\t\tلابتوب")
            if self.qq7.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq7.get()}\t\tاطباق")
            if self.qq8.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq8.get()}\t\tتكييف")
            if self.qq9.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq9.get()}\t\tفرن")
            if self.qq10.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq10.get()}\t\tغلايه")
            if self.qq11.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq11.get()}\t\tفريزر")
            if self.qq12.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq12.get()}\t\tشوكه")
            if self.qq13.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq13.get()}\t\tمطبخ")
            if self.qq14.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq14.get()}\t\tملعقه")
            if self.qq15.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq15.get()}\t\tمكوه")
            if self.qq16.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qq16.get()}\t\tسكينه")
            #=============================================================================   
            if self.qqq1.get() !=0:
                self.textarea.insert(END,f"\n {self.rez}\t\t{self.qqq1.get()}\t\tغساله")
            if self.qqq2.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq2.get()}\t\tبوتجاز")
            if self.qqq3.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq3.get()}\t\tخلاط")
            if self.qqq4.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq4.get()}\t\tثلاجه")
            if self.qqq5.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq5.get()}\t\tشاشه")
            if self.qqq6.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq6.get()}\t\tلابتوب")
            if self.qqq7.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq7.get()}\t\tاطباق")
            if self.qqq8.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq8.get()}\t\tتكييف")
            if self.qqq9.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq9.get()}\t\tفرن")
            if self.qqq10.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq10.get()}\t\tغلايه")
            if self.qqq11.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq11.get()}\t\tفريزر")
            if self.qqq12.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq12.get()}\t\tشوكه")
            if self.qqq13.get() !=0:
                self.textarea.insert(END,f"\n {self.progal}\t\t{self.qqq13.get()}\t\tمطبخ")

            self.textarea.insert(END,'\n......................................')
            self.textarea.insert(END,f'\n\t{self.all} $\t   المجموع الكلي ')
            self.textarea.insert(END,'\n......................................')
            self.savee()
            




window = Tk()
ob = super(window)
window.mainloop()




