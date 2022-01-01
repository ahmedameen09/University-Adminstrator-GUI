from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk , Image
from main import *

flag = 0

# Functions

def login():
    global email , password , top , flag
    email = box1.get()
    password = box2.get()
    if len(email) > 0 and len(password) > 5:
        var = checklogin2(email,password)
        if var == 1 :
            loginW.destroy()
            flag = 1
        else :
            messagebox.showinfo("Invalid Login", "Email or Password are not correct!")
            flag = 0
    else :
        messagebox.showinfo("Invalid Input", "Email or Password are Empty or not completely filled")
        flag = 0

#___________________________________________________________________________________________________

def click0():
    top1 = Toplevel()
    top1.title("Students Accounts DB")
    top1.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    top1.option_add("*tearOff", False)  # for remove dashed line from ui\ux
    top1.geometry("1100x550")
    top1.resizable(False, FALSE)

    def add_saccount():
        global btnt1, btnt2, btnt3
        top1.title("Add Account")
        lblt1 = ttk.Label(top1, text="Email", font=("arial", 11, "bold"), foreground="white")
        lblt2 = ttk.Label(top1, text="Password", font=("arial", 11, "bold"), foreground="white")
        lblt3 = ttk.Label(top1, text="ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1,width=25)
        boxt2 = ttk.Entry(top1,width=25)
        boxt3 = ttk.Entry(top1,width=25)
        btn_save = ttk.Button(top1, text="Save",command=lambda:add_saccount_db(email= boxt1.get(),password= boxt2.get(),id= boxt3.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0,column=1,padx=(180,20),pady=(30,30))
        lblt2.grid(row=0,column=3, padx=(20, 0), pady=(0, 0))
        lblt3.grid(row=1,column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0,column=2,padx=(20,20),pady=(30,30))
        boxt2.grid(row=0,column=4, padx=(0, 20), pady=(0, 0))
        boxt3.grid(row=1,column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    def r_saccount():
        top1.title("Remove Account")
        lblt1 = ttk.Label(top1, text="Email", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Remove",command=lambda:r_saccount_db(email=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    def Re_saccount():
        top1.title("Recover Account")
        lblt1 = ttk.Label(top1, text="Email", font=("arial", 11, "bold"), foreground="white")
        lblt2 = ttk.Label(top1, text="New Password", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        boxt2 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Update",command=lambda:Re_saccount_db(email=boxt1.get(),password=boxt2.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(160, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        lblt2.grid(row=0, column=3, padx=(20, 0), pady=(0, 0))
        boxt2.grid(row=0, column=4, padx=(0, 20), pady=(0, 0))
        btn_save.grid(row=2,column=3, padx=(130, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    # Setting Widgets

    btnt1 = ttk.Button(top1, text="Add Account",command=add_saccount,width=15)
    btnt2 = ttk.Button(top1, text="Remove Account",command=r_saccount,width=15)
    btnt3 = ttk.Button(top1, text="Recover Account",command=Re_saccount,width=15)
    btnt1.grid(row=0,column=0,padx=(20,20),pady=(100,100))
    btnt2.grid(row=1,column=0,padx=(20,20),pady=(0,0))
    btnt3.grid(row=2,column=0,padx=(20,20),pady=(100,100))


def click1():
    top1 = Toplevel()
    top1.title("Students Accounts DB")
    top1.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    top1.option_add("*tearOff", False)  # for remove dashed line from ui\ux
    top1.geometry("1100x550")
    top1.resizable(False, FALSE)

    def add_adm():
        top1.title("Add Administrator")
        lblt1 = ttk.Label(top1, text="AID", font=("arial", 11, "bold"), foreground="white")
        lblt2 = ttk.Label(top1, text="SSN", font=("arial", 11, "bold"), foreground="white")
        lblt3 = ttk.Label(top1, text="Name", font=("arial", 11, "bold"), foreground="white")
        lblt4 = ttk.Label(top1, text="Address", font=("arial", 11, "bold"), foreground="white")
        lblt5 = ttk.Label(top1, text="Gender", font=("arial", 11, "bold"), foreground="white")
        lblt6 = ttk.Label(top1, text="Salary", font=("arial", 11, "bold"), foreground="white")
        lblt7 = ttk.Label(top1, text="Grad", font=("arial", 11, "bold"), foreground="white")
        lblt8 = ttk.Label(top1, text="Specialist", font=("arial", 11, "bold"), foreground="white")
        lblt9 = ttk.Label(top1, text="Phone", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1,width=25)
        boxt2 = ttk.Entry(top1,width=25)
        boxt3 = ttk.Entry(top1,width=25)
        boxt4 = ttk.Entry(top1, width=25)
        boxt5 = ttk.Entry(top1, width=25)
        boxt6 = ttk.Entry(top1, width=25)
        boxt7 = ttk.Entry(top1, width=25)
        boxt8 = ttk.Entry(top1, width=25)
        boxt9 = ttk.Entry(top1, width=25)

        btn_save = ttk.Button(top1, text="Save",style="Accent.TButton",command=lambda:add_adm_db( id = boxt1.get(),ssn = boxt2.get(),name = boxt3.get(),address = boxt4.get()
        ,gender = boxt5.get()
        ,salary = boxt6.get()
        ,grad = boxt7.get()
        ,job = boxt8.get()
        ,phone = boxt9.get()),width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0,column=1,padx=10,pady=20)
        lblt2.grid(row=0,column=3,padx=10,pady=20)
        lblt3.grid(row=1,column=1,padx=10,pady=20)
        lblt4.grid(row=1, column=3,padx=10,pady=20)
        lblt5.grid(row=2, column=1,padx=10,pady=20)
        lblt6.grid(row=2, column=3,padx=10,pady=20)
        lblt7.grid(row=3, column=1,padx=10,pady=20)
        lblt8.grid(row=3, column=3,padx=10,pady=20)
        lblt9.grid(row=4, column=1, padx=10, pady=20)
        boxt1.grid(row=0,column=2,padx=10,pady=20)
        boxt2.grid(row=0,column=4,padx=10,pady=20)
        boxt3.grid(row=1,column=2,padx=10,pady=20)
        boxt4.grid(row=1, column=4,padx=10,pady=20)
        boxt5.grid(row=2, column=2,padx=10,pady=20)
        boxt6.grid(row=2, column=4,padx=10,pady=20)
        boxt7.grid(row=3, column=2,padx=10,pady=20)
        boxt8.grid(row=3, column=4,padx=10,pady=20)
        boxt9.grid(row=4, column=2, padx=10, pady=20)
        btn_save.grid(row=4,column=4,padx=(50,0),pady=(40,10))
        btn_cancel.grid(row=4, column=5,padx=(10,0),pady=(40,10))

    def search_adm():
        top1.title("Search Administrator")
        lblt1 = ttk.Label(top1, text="Administrator ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Search",command=lambda:search_adm_db(id=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    btnt1 = ttk.Button(top1, text="Add Administrator",command=add_adm,width=18)
    btnt2 = ttk.Button(top1, text="Search Administrator",command=search_adm,width=18)
    btnt1.grid(row=0,column=0,padx=(20,20),pady=(100,100))
    btnt2.grid(row=1,column=0,padx=(20,20),pady=(0,0))



def click2():
    top1 = Toplevel()
    top1.title("Students Accounts DB")
    top1.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    top1.option_add("*tearOff", False)  # for remove dashed line from ui\ux
    top1.geometry("1100x550")
    top1.resizable(False, FALSE)

    def search_prof():
        top1.title("Search Professor")
        lblt1 = ttk.Label(top1, text="Professor ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Search",command=lambda:search_prof_db(id=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    def search_dem():
        top1.title("Search Demonstrators")
        lblt1 = ttk.Label(top1, text="Demonstrators ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Search",command=lambda:search_dem_db(id=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))

    btnt2 = ttk.Button(top1, text="Search Professors",command=search_prof,width=19)
    btnt3 = ttk.Button(top1, text="Search Demonstrators",command=search_dem,width=19)
    btnt2.grid(row=0,column=0,padx=(20,20),pady=(100,0))
    btnt3.grid(row=1, column=0, padx=(20, 20), pady=(100, 100))

def click4():
    top1 = Toplevel()
    top1.title("Students Accounts DB")
    top1.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    top1.option_add("*tearOff", False)  # for remove dashed line from ui\ux
    top1.geometry("1100x550")
    top1.resizable(False, FALSE)

    def add_student():
        top1.title("Add Student")
        lblt1 = ttk.Label(top1, text="SID", font=("arial", 11, "bold"), foreground="white")
        lblt2 = ttk.Label(top1, text="SSN", font=("arial", 11, "bold"), foreground="white")
        lblt3 = ttk.Label(top1, text="Name", font=("arial", 11, "bold"), foreground="white")
        lblt4 = ttk.Label(top1, text="Address", font=("arial", 11, "bold"), foreground="white")
        lblt5 = ttk.Label(top1, text="Gender", font=("arial", 11, "bold"), foreground="white")
        lblt6 = ttk.Label(top1, text="GPA", font=("arial", 11, "bold"), foreground="white")
        lblt7 = ttk.Label(top1, text="class", font=("arial", 11, "bold"), foreground="white")
        lblt8 = ttk.Label(top1, text="units", font=("arial", 11, "bold"), foreground="white")
        lblt9 = ttk.Label(top1, text="Phone", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1,width=25)
        boxt2 = ttk.Entry(top1,width=25)
        boxt3 = ttk.Entry(top1,width=25)
        boxt4 = ttk.Entry(top1, width=25)
        boxt5 = ttk.Entry(top1, width=25)
        boxt6 = ttk.Entry(top1, width=25)
        boxt7 = ttk.Entry(top1, width=25)
        boxt8 = ttk.Entry(top1, width=25)
        boxt9 = ttk.Entry(top1, width=25)

        btn_save = ttk.Button(top1, text="Save",style="Accent.TButton",command=lambda:add_student_db( id = boxt1.get(),ssn = boxt2.get(),name = boxt3.get(),address = boxt4.get()
        ,gender = boxt5.get()
        ,GPA = boxt6.get()
        ,classy = boxt7.get()
        ,units = boxt8.get()
        ,phone = boxt9.get()),width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0,column=1,padx=10,pady=20)
        lblt2.grid(row=0,column=3,padx=10,pady=20)
        lblt3.grid(row=1,column=1,padx=10,pady=20)
        lblt4.grid(row=1, column=3,padx=10,pady=20)
        lblt5.grid(row=2, column=1,padx=10,pady=20)
        lblt6.grid(row=2, column=3,padx=10,pady=20)
        lblt7.grid(row=3, column=1,padx=10,pady=20)
        lblt8.grid(row=3, column=3,padx=10,pady=20)
        lblt9.grid(row=4, column=1, padx=10, pady=20)
        boxt1.grid(row=0,column=2,padx=10,pady=20)
        boxt2.grid(row=0,column=4,padx=10,pady=20)
        boxt3.grid(row=1,column=2,padx=10,pady=20)
        boxt4.grid(row=1, column=4,padx=10,pady=20)
        boxt5.grid(row=2, column=2,padx=10,pady=20)
        boxt6.grid(row=2, column=4,padx=10,pady=20)
        boxt7.grid(row=3, column=2,padx=10,pady=20)
        boxt8.grid(row=3, column=4,padx=10,pady=20)
        boxt9.grid(row=4, column=2, padx=10, pady=20)
        btn_save.grid(row=4,column=4,padx=(50,0),pady=(40,10))
        btn_cancel.grid(row=4, column=5,padx=(10,0),pady=(40,10))


    def search_student():
        top1.title("Search Student")
        lblt1 = ttk.Label(top1, text="Student ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Search",command=lambda:search_student_db(id=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))


    def search_s_result():
        top1.title("Search Student Result")
        lblt1 = ttk.Label(top1, text="Student ID", font=("arial", 11, "bold"), foreground="white")
        boxt1 = ttk.Entry(top1, width=25)
        btn_save = ttk.Button(top1, text="Search",command=lambda:search_s_result_db(id=boxt1.get()),style="Accent.TButton",width=12)
        btn_cancel = ttk.Button(top1, text="Cancel",command=top1.quit,width=12)
        lblt1.grid(row=0, column=1, padx=(180, 20), pady=(30, 30))
        boxt1.grid(row=0, column=2, padx=(20, 20), pady=(30, 30))
        btn_save.grid(row=2,column=3, padx=(100, 10), pady=(30, 30))
        btn_cancel.grid(row=2, column=4, padx=(5, 20), pady=(30, 30))

    btnt1 = ttk.Button(top1, text="Add Students",width=20,command=add_student)
    btnt2 = ttk.Button(top1, text="Search Students",command=search_student,width=20)
    btnt3 = ttk.Button(top1, text="Search Student's Result",command=search_s_result,width=20)
    btnt1.grid(row=0, column=0, padx=(20, 20), pady=(50, 50))
    btnt2.grid(row=1,column=0,padx=(20,20),pady=(0,0))
    btnt3.grid(row=2, column=0, padx=(20, 20), pady=(50, 50))



# General login Configuration

loginW = Tk()
loginW.title("MRU Administrator System")
loginW.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
loginW.option_add("*tearOff", False)                            # for remove dashed line from ui\ux
loginW.geometry("1000x650")                                     # for default size of window
loginW.resizable(False, FALSE)                                  # for resizing of window
loginW.columnconfigure(index=0 , weight=1)
loginW.columnconfigure(index=1 , weight=2)
loginW.columnconfigure(index=2 , weight=1)
loginW.rowconfigure(index=0 , weight=1)
loginW.rowconfigure(index=1 , weight=1)
loginW.rowconfigure(index=2 , weight=1)
style = ttk.Style(loginW)

# Setting Login Frame
loginframe = ttk.Frame(loginW,padding=(20,0, 0, 10))
loginframe.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
loginframe.columnconfigure(index=0, weight=1)

# setting the theme
loginW.call("source", r"C:\Users\14b007\Desktop\MRU Database Project\Azure-ttk-theme-main\azure.tcl")
loginW.call("set_theme", "dark")

# setting Logo
logo = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Logo Design\Removal-547.png")  # open image
r_logo = logo.resize((150,139), Image.ANTIALIAS)               # resizing image
F_logo = ImageTk.PhotoImage(r_logo)                            # make image photo
logolbl = Label(image=F_logo)                                  # make image as label

# setting login button
loginbtn = ttk.Button(loginframe,text = "Login",style="Accent.TButton" , width=15 , command=login ) # ttk is module from class for themed widgets

# setting Boxes Entry & Labels
box1 = ttk.Entry(loginframe)
box2 = ttk.Entry(loginframe , show="x")
lbl1 = ttk.Label(loginframe,text="Admin mail",font=("arial" , 11 , "bold"),foreground="white")
lbl2 = ttk.Label(loginframe,text="Password",font=("arial" , 11 , "bold"),foreground="white")
lbl3 = ttk.Label(loginframe,text="Forgotten password?",font=("arial" , 10),foreground="grey")

# Setting widgets on the screen
logolbl.grid(row=0, column=1 , pady=(10,30) ,sticky=EW)
lbl1.grid(row=1 , column=0 , columnspan=1 , pady=(185,10) , padx=(190,200) , sticky=W)
box1.grid(row=2 ,column=0 , columnspan=1 , pady=(0,10) , padx=(190,200) , sticky=EW)
lbl2.grid(row=3 , column=0 , columnspan=1 , pady=(10,10) , padx=(190,200) , sticky=W)
box2.grid(row=4 , column=0 , columnspan=1 , pady=(0,20) , padx=(190,200) , sticky=EW)
lbl3.grid(row=5 , column=0 , columnspan=1 , pady=(20,10) , padx=(190,200))
loginbtn.grid(row=6 ,column=0 , columnspan=1 , pady=20 , padx=(190,200))

# Loops Running
loginW.mainloop()

#___________________________________________________________________________________________________

# Window Configuration
if flag == 1 :
    mainW = Tk()
    mainW.title("MISR University Adminstrator System")
    mainW.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    mainW.option_add("*tearOff", False)
    mainW.geometry("1200x650")
    mainW.resizable(True, True)
    mainW.columnconfigure(index=0 , weight=1)
    mainW.columnconfigure(index=1 , weight=1)
    mainW.columnconfigure(index=2 , weight=1)
    mainW.columnconfigure(index=3 , weight=1)
    mainW.rowconfigure(index=0 , weight=1)
    mainW.rowconfigure(index=1 , weight=1)
    mainW.rowconfigure(index=2 , weight=1)
    mainW.rowconfigure(index=3 , weight=1)
    sizegrip = ttk.Sizegrip(mainW)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
    style = ttk.Style(mainW)

    # setting the theme
    mainW.call("source", r"C:\Users\14b007\Desktop\MRU Database Project\Azure-ttk-theme-main\azure.tcl")
    mainW.call("set_theme", "dark")

    # Frames
    # frame['padding'] = (left, top, right, bottom)
    # frame['padding'] allows you to add extra space around the inside of the frame.

    frame_0 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_1 = ttk.Frame(mainW, height=200, width=200, borderwidth=5)
    frame_2 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_3 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_4 = ttk.Frame(mainW, height=200, width=200, borderwidth=5)
    frame_5 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_6 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_7 = ttk.Frame(mainW,height=200 ,width=200,borderwidth=5)

    # Griding on Screen
    # padx and pady allows you to add extra space around the outside of the frame

    frame_0.grid(row=1,column=0,sticky="WS",padx=(110,0))
    frame_1.grid(row=1,column=1,sticky="WS")
    frame_2.grid(row=1,column=2,sticky="WS")
    frame_3.grid(row=1,column=3,sticky="WS")
    frame_4.grid(row=2,column=0,sticky="WS",padx=(110,0))
    frame_5.grid(row=2,column=1,sticky="WS")
    frame_6.grid(row=2,column=2,sticky="WS")
    frame_7.grid(row=2,column=3,sticky="WS")

    lbl = ttk.Label(mainW,text="Administrator Main Menu",font = "arial 13")
    lbl.grid(row=0,column=1,columnspan=2)

    # Frame_0 Widgets setting

    img0 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\7303401-removebg-preview.png")
    r_img0 = img0.resize((160,160), Image.ANTIALIAS)
    F_img0 = ImageTk.PhotoImage(r_img0)
    img0_lbl = Label(frame_0,image=F_img0)
    btn0 = ttk.Button(frame_0,text = "Accounts DB",command=click0)
    img0_lbl.grid(pady=(0,10),padx=10)
    btn0.grid()

    # Frame_1 Widgets setting

    img1 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\pngfind.com-admin-icon-png-5286002.png")
    r_img1 = img1.resize((160,160), Image.ANTIALIAS)
    F_img1 = ImageTk.PhotoImage(r_img1)
    img1_lbl = Label(frame_1,image=F_img1)
    btn1 = ttk.Button(frame_1,text = "Administrators DB",command=click1)
    img1_lbl.grid(pady=(0,10),padx=10)
    btn1.grid()

    # Frame_2 Widgets setting

    img2 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\professor.png")
    r_img2 = img2.resize((160,160), Image.ANTIALIAS)
    F_img2 = ImageTk.PhotoImage(r_img2)
    img2_lbl = Label(frame_2,image=F_img2)
    btn2 = ttk.Button(frame_2,text = "Educational Staff",command=click2)
    img2_lbl.grid(pady=(0,10),padx=10)
    btn2.grid()

    # Frame_3 Widgets setting

    img3 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\Student-Dtabase.png")
    r_img3 = img3.resize((160,160), Image.ANTIALIAS)
    F_img3 = ImageTk.PhotoImage(r_img3)
    img3_lbl = Label(frame_3,image=F_img3)
    btn3 = ttk.Button(frame_3,text = "Students DB",width=12,command=click4)
    img3_lbl.grid(pady=(0,10),padx=10)
    btn3.grid()

    # Frame_4 Widgets setting

    img4 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\Announcment.png")
    r_img4 = img4.resize((160,160), Image.ANTIALIAS)
    F_img4 = ImageTk.PhotoImage(r_img4)
    img4_lbl = Label(frame_4,image=F_img4)
    btn4 = ttk.Button(frame_4,text = "Announcements")
    img4_lbl.grid(pady=(0,10),padx=10)
    btn4.grid()

    # Frame_5 Widgets setting

    img5 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\Registration.png")
    r_img5 = img5.resize((160,160), Image.ANTIALIAS)
    F_img5 = ImageTk.PhotoImage(r_img5)
    img5_lbl = Label(frame_5,image=F_img5)
    btn5 = ttk.Button(frame_5,text = "Registration")
    img5_lbl.grid(pady=(0,10),padx=10)
    btn5.grid()

    # Frame_6 Widgets setting

    img6 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\others-icon-20.jpg")
    r_img6 = img6.resize((160,160), Image.ANTIALIAS)
    F_img6 = ImageTk.PhotoImage(r_img6)
    img6_lbl = Label(frame_6,image=F_img6)
    btn6 = ttk.Button(frame_6,text = "Documentations & Social")
    img6_lbl.grid(pady=(0,10),padx=10)
    btn6.grid()

    # Frame_7 Widgets setting

    img7 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\kindpng_211349.png")
    r_img7 = img7.resize((160,160), Image.ANTIALIAS)
    F_img7 = ImageTk.PhotoImage(r_img7)
    img7_lbl = Label(frame_7,image=F_img7)
    btn7 = ttk.Button(frame_7,text = "Results",width=12)
    img7_lbl.grid(pady=(0,10),padx=10)
    btn7.grid()
    mainloop()
