
from tkinter import * 
from tkinter import messagebox
import webbrowser
import os 
import sys

# control with geomatric program
window = Tk()
window.geometry('800x450+250+50')
window.title("SUBERMARKET")
window.resizable(False,False)
window.iconbitmap('supermarket_png (1).ico')

# Add linkes
url_1= 'https://www.facebook.com/mostafa.salm.9659'
url_2 = "https://t.me/+201096853195"
url_3 ="www.youtube.com/@mostafasalim-vn1np"
class social_media():
    def __init__(self, url1, url2, url3) -> None:
        self.url1 = url1
        self.url2 = url2
        self.url3 = url3
        # self.user = user, user, password
        # self.password = password
    def open1 (self):
        webbrowser.open(f"{self.url1}")
    def open2 (self):
        webbrowser.open(f"{self.url2}")
    def open3 (self):
        webbrowser.open(f"{self.url3}")
    def about1(self):
        messagebox.showinfo("Develober"," Mustafa Salem")
    def about2(self):
        messagebox.showinfo('About Program','Suber Market System')
    def entry1(self):
        user = ent1.get()
        password = ent2.get
        if user == "mustafa" and password == '12345':
            messagebox.showinfo('Hello ', "Right Informtion")
        else:
            messagebox.showinfo('Hello ', "Invalid Informtion")
social_media_sets = social_media(url_1 ,url_2 ,url_3 )



# title from program interface
title = Label(window, text="Suber Maket System", fg="gold", bg="black", font=('tajawal', 16, 'bold'))
title.pack(fill=X)

# frame One From Right Interface Program 
f1 = Frame(window , bg="#14073b", width=230, height=420)
f1.place(x=570, y=30)
title1 = Label(f1, text="مشروع سوبر ماركت ", bg="#14073b" , fg='white', font=('tajawal', 16, 'bold'))
title1.place(x=40 , y= 10)
title1 = Label(f1, text="*****************", bg="#14073b", fg='white',font=('tajawal', 16, 'bold'))
title1.place(x=45 , y= 45)
title1 = Label(f1, text="  وسائل الاتصال بنا ", bg="#14073b" , fg='white', font=('tajawal', 16, 'bold'))
title1.place(x=45 , y= 80)
# button on linkes social media
button1 = Button(f1, text="حسابنا علي فيسبوك " ,width=15 , activeforeground="white" ,  bg="#300000" , activebackground="blue" , fg='white', font=('tajawal', 16, 'bold'), command=social_media_sets.open1) 
button1.place(x=15, y=120)
button2 = Button(f1, text="حسابنا علي تليجرام " ,width=15 , activeforeground="white" ,  bg="#4d0303", activebackground="blue"  , fg='white', font=('tajawal', 16, 'bold'), command=social_media_sets.open2) 
button2.place(x=15, y=170)
button3 = Button(f1, text="حسابنا علي يوتيوب " ,width=15 , activeforeground="white" ,  bg="#660707", activebackground="blue" , fg='white', font=('tajawal', 16, 'bold'),  command=social_media_sets.open3) 
button3.place(x=15, y=220)
button4 = Button(f1, text="لمحه عن المطور" ,width=15 , activeforeground="white" ,  bg="#851010", activebackground="blue"  , fg='white', font=('tajawal', 16, 'bold'),  command=social_media_sets.about1) 
button4.place(x=15, y=270)
button5 = Button(f1, text=" لمحه عن المشروع" ,width=15 , activeforeground="white" ,  bg="#a61c1c", activebackground="blue"  , fg='white', font=('tajawal', 16, 'bold'),  command=social_media_sets.about2) 
button5.place(x=15, y=320)
button5 = Button(f1, text=" اغلاق البرنامج" ,width=15, activeforeground="white" ,bg="#c22d2d", activebackground="black"  , fg='white', font=('tajawal', 16, 'bold'), command=quit) 
button5.place(x=15, y=370)

# Image For Interface Program
photo = PhotoImage(file="supermarket232.png")
image_interface = Label(window, image=photo,width=520, height=295,bg="white")
image_interface.place(x=30, y=30)

# Frame Two 
f2 = Frame(window , bg="#14073b", width=570, height=120)
f2.place(x=0, y=330)
photo2 = PhotoImage(file="supermarket_png (1).png")
images_iconFram = Label(f2, image=photo2)
images_iconFram.place(x=450, y=0, width=120 ,height=120)
lab1 = Label(f2, text="اسم المستخدم" ,font=('tajawal', 16, 'bold'), bg="#14073b", fg="yellow")
lab1.place(x=330, y=25)
lab2 = Label(f2, text="كلمة المرور " ,font=('tajawal', 16, 'bold'), fg="yellow", bg="#14073b")
lab2.place(x=330, y=70)
ent1 = Entry(f2, font=('tajawal', 12), justify='center')
ent1.place(x=130, y=27)
ent2 = Entry(f2, font=('tajawal', 12), justify='center')
ent2.place(x=130, y=72)
butt = Button(f2, text="تسجيل الدخول ", font=('tajawal',12), activebackground="blue" , width=12 , height=4, bg="yellow", command=social_media_sets.entry1)
butt.place(x = 10, y=20)




window.mainloop()
