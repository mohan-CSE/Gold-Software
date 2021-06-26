from tkinter import *
from tkinter import messagebox,ttk
import glob
import pathlib
import locale
import re
from PyPDF2 import PdfFileWriter, PdfFileReader
import sqlite3, datetime, pandas, time
import xlwt
import xlrd
from xlutils.copy import copy
from PIL import ImageTk
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from num2words import num2words
import os
master_pin = "1vGQVCiFN8YsCqvH"
#---------------------------------------------------------------------------BILL CODE BEGINS---------------------------------------------
def bill(price):
    global price_o
    img = Image.open("0003.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    f = ImageFont.truetype("ARIAL.ttf", 50)
    f1 = ImageFont.truetype("ARIAL.ttf", 33)
    # draw.text((x, y),"Sample Text",(r,g,b))
    address = (cust_address.get('1.0', END)).split("/n")
    locale.setlocale(locale.LC_MONETARY, 'en_IN')
    a = locale.currency(round(price_o), grouping=True)[2:]
    b = locale.currency(round(price), grouping=True)[2:]
    if answer2=="yes":
            invoice = (datee.replace("-","")).replace("-","")+str(timee)
            print(timee)
    else:
            invoice = invoicee
    draw.text((450,865),"VSGS"+invoice,(0,0,0), font = f1)
    draw.text((476,933),datee,(0,0,0), font = f)
    draw.text((1130,933),cashier_namee,(0,0,0), font = f)
    draw.text((1952,855),str(b),(0,0,0), font = f)
    draw.text((1885,933),str(b),(0,0,0), font = f)
    draw.text((221,1071),address[0],(0,0,0), font = f)
    if cust_phone.get() is not None:
        draw.text((221,1300),cust_phone.get(),(0,0,0), font = f)
    if gstin_entry.get() != "":
        draw.text((221,1390),"GSTIN:",(0,0,0), font = f)
        draw.text((400,1390),gstin_entry.get(),(0,0,0), font = f)
        print('m',gstin_entry.get())
    if typee == "24" or typee == "22":
        draw.text((120,1612),"Gold",(0,0,0), font = f)
    else:
        draw.text((120,1612),"Silver",(0,0,0), font = f)
    draw.text((300,1612),"71081200",(0,0,0), font = f)
    draw.text((556,1612),grams_entry.get()+"g",(0,0,0), font = f)
    draw.text((766,1612),typee,(0,0,0), font = f)
    draw.text((950,1612),str(b),(0,0,0), font = f1)
    draw.text((1330,1610),str(a),(0,0,0), font = f1)
    draw.text((1610,1612),cgst+"%",(0,0,0), font = f)
    draw.text((1828,1612),sgst+"%",(0,0,0), font = f)
    draw.text((2025,1612),tcs+"%",(0,0,0), font = f)
    draw.text((2189,1610),str(b),(0,0,0), font = f1)
    draw.text((2178,1756),str(a),(0,0,0), font = f)
    draw.text((2178,1828),str(round(((price_o)*(float(float(sgst)/100))))),(0,0,0), font = f)
    draw.text((2174,1908),str(round(((price_o)*(float(float(cgst)/100))))),(0,0,0), font = f)
    draw.text((2178,1975),str(round(((price_o)*(float(float(tcs)/100))))),(0,0,0), font = f)
    draw.text((2190,2130),str(b),(0,0,0), font = f)
    draw.text((2056,2283),str(b),(0,0,0), font = f)
    draw.text((90,2052),(num2words(str(price), lang = "en_IN")).upper(),(0,0,0), font = f1)
    draw.text((152,2445),datee,(0,0,0), font = f1)
    draw.text((388,2445),payment_combo.get(),(0,0,0), font = f1)
    draw.text((539,2444),"INR "+str(b),(0,0,0), font = f1)
    img.save('sample-out.jpg')
    image1 = Image.open('sample-out.jpg')
    im1 = image1.convert('RGB')
    im1.save("VSGS"+invoice+".pdf")
    if  cust_phone.get()!=None:
        cust_phone.delete(0,'end')
    if customer_name.get!=None:
        customer_name.delete(0,'end')
    if cust_aadhar.get()!=None:
        cust_aadhar.delete(0,'end')
    if cust_address.get('1.0', END)!=None:
        cust_address.delete('1.0',END)
    if grams_entry.get()!=None:
        grams_entry.delete(0,'end')
    if date_entry.get()!=None:
        date_entry.delete(0,'end')
    if gstin_entry.get()!=None:
        gstin_entry.delete(0,'end')
    if invoice_entry.get()!=None:
        invoice_entry.delete(0,'end')
    if payment_combo.get()!=None:
        payment_combo.set('')
    value1 = var1.get()
    value2 = var2.get()
    value3 = var3.get()
    os.remove("sample-out.jpg")
    path = "VSGS"+invoice+".pdf"
    os.system(path)

#---------------------------------------------------------------------------BILL CODE ENDS-----------------------------------------------

#-----------------------------------------------------------------------------SQL CODE BEGINS--------------------------------------------

admin_db = "D:\python\gold_project\mohan.db"
def admin_create_table():
    connection = sqlite3.connect("mohan.db")
    cursorObj = connection.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS admin (username text, password text)")
    connection.commit()
admin_create_table()

def insert_admin_values(username, password):
    connection = sqlite3.connect('mohan.db')
    cursorObj = connection.cursor()
    cursorObj.execute("INSERT INTO  admin VALUES(?,?)", (username, password))
    connection.commit()
#insert_admin_values('rohit', 'rohit')

def update_admin_values(username, password):
    connection = sqlite3.connect('mohan.db')
    cursorObj = connection.cursor()
    cursorObj.execute("UPDATE admin SET password=? WHERE username=?", (password, username))
    connection.commit()


def passwords_lists():
    global res, list1, list2, list_u, list_P
    connection = sqlite3.connect('mohan.db')
    cursorObj = connection.cursor()
    cursorObj.execute('SELECT username FROM admin')
    list1 = cursorObj.fetchall()
    cursorObj.execute('SELECT password FROM admin')
    list2 = cursorObj.fetchall()
    list_u = []
    list_p = []
    for i in list1:
        for j in i:
            list_u.append(j)
    for i in list2:
        for j in i:
            list_p.append(j)
    res = dict()
    for u, p in zip(list1, list2):
        for i, j in zip(u, p):
            res[i] = j
    return res
    connection.close()
passwords_lists()
#================================================================================================================================

def price_details_db():
    connection = sqlite3.connect("price_details.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Row(row TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Colomn(colomn TEXT)")
    connection.commit()
    connection.close()
price_details_db()
def p_details(row):
    connection = sqlite3.connect("price_details.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Row VALUES (?)",(row,))
    connection.commit()
    connection.close()
#p_details("1")

def customer_details_db():
    connection = sqlite3.connect("customer_details.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Row(row TEXT)")
    connection.commit()
    connection.close()
customer_details_db()
def c_details_db(row):
    connection = sqlite3.connect("customer_details.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Row VALUES (?)",(row,))
    connection.commit()
    connection.close()
#c_details_db('1')
#================================================================================================================================
def cashier_create_table():
    connection = sqlite3.connect('new_cashier.db')
    cursorObj = connection.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS cashier (username Text, password Text)")
    connection.commit()
cashier_create_table()

def insert_cashier_values(username, password):
    connection = sqlite3.connect('new_cashier.db')
    cursorObj = connection.cursor()
    cursorObj.execute("INSERT INTO  cashier VALUES(?,?)", (username, password))
    connection.commit()
#insert_cashier_values('mohan', 'rohit')

def c_update_cashier_values(username, password):
    connection = sqlite3.connect('new_cashier.db')
    cursorObj = connection.cursor()
    cursorObj.execute("UPDATE cashier SET password=? WHERE username=?", (password, username))
    connection.commit()


def c_passwords_lists():
    global res2, list1, list2, c_list_u, c_list_P
    connection = sqlite3.connect('new_cashier.db')
    cursorObj = connection.cursor()
    cursorObj.execute('SELECT username FROM cashier')
    list1 = cursorObj.fetchall()
    cursorObj.execute('SELECT password FROM cashier')
    list2 = cursorObj.fetchall()
    c_list_u = []
    c_list_p = []
    for i in list1:
        for j in i:
            c_list_u.append(j)
    for i in list2:
        for j in i:
            c_list_p.append(j)
    res2 = dict()
    for u, p in zip(list1, list2):
        for i, j in zip(u, p):
            res2[i] = j
    return res2
    connection.close()
c_passwords_lists()

#-----------------------------------------------------------------------------SQL CODE ENDS--------------------------------------------
def conformation3():
    print(f_pass_entry.get(),fU_entry.get())
    answer3 = messagebox.askquestion("Please Confirm", "Are you sure?")
    username_list = []
    for key in res:
        username_list.append(key)
    if answer3=="yes":
        if fU_entry.get() in username_list and fM_entry.get() == master_pin:
            update_admin_values(fU_entry.get(), f_pass_entry.get())
            forgot.destroy()

def conformation4():
    answer3 = messagebox.askquestion("Please Confirm", "Are you sure?")
    c_username_list = []
    for key in res2:
        c_username_list.append(key)
    if answer3=="yes":
        if c_fU_entry.get() in c_username_list:
            c_update_cashier_values(c_fU_entry.get(), c_f_pass_entry.get())
            c_forgot.destroy()
def admin_forgot():
    login_admin.destroy()
    global fU_entry,fM_entry,f_pass_entry, forgot
    forgot = Tk()
    f_username = StringVar()
    master_p = StringVar()
    new_pass = StringVar()
    forgot.geometry("512x512")
    forgot.title("Varaha Satya Gold & Silver [ADMIN]")
    forgot.iconbitmap("gold.ico")
    c_bg = PhotoImage(file="coins.png")
    Label(forgot, image=c_bg).place(x=0,y=0)
    fU_label = Label(forgot, text="Enter Current Username", fg="black", font=('Arial 17 bold'), bg="white").pack()
    fU_entry = Entry(forgot, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=f_username, fg="black", show="*")
    fU_entry.pack()
    fM_label = Label(forgot, text="Enter Current Password", fg="black", font=('Arial 17 bold'), bg="white").pack()
    fM_entry = Entry(forgot, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=master_p, fg="black", show="*")
    fM_entry.pack()
    f_pass_label = Label(forgot, text="Enter New Password", fg="black", font=('Arial 17 bold'), bg="white").pack()
    f_pass_entry = Entry(forgot, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=new_pass, fg="black", show="*")
    f_pass_entry.pack()
    f_submit = Button(forgot, text="Submit", font=('Arial 13 bold'),fg="White", bg="Green", command=conformation3).pack()
    forgot.mainloop()
    
def cashier_forgot():
    login_cashier.destroy()
    global c_fU_entry,c_fM_entry,c_f_pass_entry,c_forgot
    c_forgot = Tk()
    c_f_username = StringVar()
    c_master_p = StringVar()
    c_new_pass = StringVar()
    c_forgot.geometry("512x512")
    c_forgot.title("Varaha Satya Gold & Silver [CASHIER]")
    c_forgot.iconbitmap("gold.ico")    
    c_bg = PhotoImage(file="coins.png")
    Label(c_forgot, image=c_bg).place(x=0,y=0)

    c_fU_label = Label(c_forgot, text="Enter Current Username", fg="black", font=('Arial 17 bold'), bg="white").pack()
    c_fU_entry = Entry(c_forgot, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=c_f_username, fg="black", show="*")
    c_fU_entry.pack()
    c_f_pass_label = Label(c_forgot, text="Enter New Password", fg="black", font=('Arial 17 bold'), bg="white").pack()
    c_f_pass_entry = Entry(c_forgot, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=c_new_pass, fg="black", show="*")
    c_f_pass_entry.pack()
    c_f_submit = Button(c_forgot, text="Submit", font=('Arial 13 bold'),fg="White", bg="Green", command=conformation4).pack()
    c_forgot.mainloop()
    
def admin_login():
    choice.destroy()
    global login_admin
    login_admin = Tk()
    login_admin.geometry("512x512")
    login_admin.title("Varaha Satya Gold & Silver [ADMIN]")
    login_admin.iconbitmap("gold.ico")

    bg = PhotoImage(file="coins.png")
    admin_bg = Label(login_admin, image=bg)
    admin_bg.place(x=0,y=0)

    #login_admin.configure(bg="#2A2A29")
    global name_box, password_box
    user_name = StringVar()
    pass_word = StringVar()

    #This code below is for username details and boxes
    username_text = Label(login_admin, text="Enter Username", fg="black", font=('Arial 17 bold'), bg="white").pack()
    name_box = Entry(login_admin, width=21, font=('Arial 17 bold'), borderwidth=5, bg="white", textvariable=user_name, fg="black")
    name_box.pack()

    #This code below is for password details and boxes
    password_text = Label(login_admin, font=('Arial 17 bold'),text="Enter Password", fg="black", bg="white").pack()
    password_box = Entry(login_admin, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=pass_word, fg="black", show="*")
    password_box.pack()

    Label(login_admin, text="\n",bg="white").pack()
    #Login button code chunk is below
    login_button = Button(login_admin, text="Login", font=('Arial 17 bold'),fg="white", bg="green", command=admin_check)
    login_button.pack()
    forgot_label = Button(login_admin, text="Forgot Password!!", font=('Arial 13 bold'),fg="Red", bg="Black", command=admin_forgot)
    forgot_label.pack()
    login_admin.mainloop()



def admin_check():
    if(name_box.get() in list_u and password_box.get() == res[name_box.get()]):
        admin_interface()
    else:
        Label(login_admin, text="Invalid Credentials !!", fg="red", bg="#2A2A29").place(x=191,y=155)

def update_price_admin():
    global p,_24k_g,_22k_g,_999k_g,_995k_g,profit,cgst,tcs,sgst
    Label(app, text="Price has been Updated Successfully", font=('Helvetica 18 bold'), fg="green", bg="white").place(x=790,y=659)

    time = datetime.datetime.now()
    time = time.strftime("%d-%B-%Y")
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    print(row1)
    for i in row1:
        for j in i:
            p = int(j)
            print(p)
    rb = xlrd.open_workbook("xlwt example.xls")
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    w_sheet.write(p,0,time)
    w_sheet.write(p,1,cgst_entry.get())
    w_sheet.write(p,2,sgst_entry.get())
    w_sheet.write(p,3,tcs_entry.get())
    w_sheet.write(p,4,profit_entry.get())
    w_sheet.write(p,5,twenty_two_entry.get())
    w_sheet.write(p,6,twenty_four_entry.get())
    w_sheet.write(p,7,nnf_silver_entry.get())
    w_sheet.write(p,8,nnn_silver_entry.get())
    wb.save("xlwt example.xls")
    row = (int(j)+1)
    connection = sqlite3.connect("price_details.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Row SET row=? ",(row,))
    connection.commit()
    connection.close()
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    list1 = sheet.row_values(p)
    cgst = list1[1]
    sgst = list1[2]
    tcs = list1[3]
    profit = list1[4]
    _22k_g = list1[5]
    _24k_g = list1[6]
    _995k_g = list1[7]
    _999k_g = list1[8]
    print(list1)

def conformation1():
    answer3 = messagebox.askquestion("Please Confirm", "Are you sure?")
    if answer3=="yes":
        update_price_admin()
def conformation2():
    answer4 = messagebox.askquestion("Please Confirm", "Are you sure?")
    if answer4=="yes":
        register_cashier()

def conformation5():
    answer4 = messagebox.askquestion("Please Confirm", "Are you sure?")
    if answer4=="yes":
        register_admin()
        
def pdfs_choose():
    global from_entry, to_entry
    from_d = StringVar()
    to_d = StringVar()
    choose = Tk()
    choose.geometry("1000x512")
    choose.title("Varaha Satya Gold & Silver [ADMIN]")
    choose.configure(bg="orange")
    Label(choose, text='FROM', font=('Helvetica 16 bold underline'), fg="black", bg="gold").pack()
    from_entry = Entry(choose, borderwidth=5, textvariable=from_d, fg="black", bg="grey", width=40, font=('arial',15))
    from_entry.pack()
    Label(choose, text='TO', font=('Helvetica 16 bold underline'), fg="black", bg="gold").pack()
    to_entry = Entry(choose, borderwidth=5, textvariable=to_d, fg="black", bg="grey", width=40, font=('arial',15))
    to_entry.pack()
    instruction_label = Label(choose, text="Only give maximum 2 months dates,(dd-mm-yy)(ex:02-06-21)", font=('Helvetica 16 bold underline'), fg="white", bg="gold").pack()
    submit_report = Button(choose, text="SUBMIT", borderwidth=5, command=conformation6, fg="White", bg="Green", font=('Helvetica 15 bold')).pack()


def conformation6():
    global a,b
    answer4 = messagebox.askquestion("Please Confirm", "Are you sure?")
    if answer4=="yes":
        a = from_entry.get()
        b = to_entry.get()
        merger()
    
def merger():
    global from_entry, to_entry,a,b, path
    from_entry = (a.replace("-","")).replace("-","")
    to_entry = (b.replace("-","")).replace("-","")
    f_day = int(from_entry[0:2])
    f_year = int(from_entry[4:6])
    temp1 = f_day
    t_day = int(to_entry[0:2])
    t = 1
    temp2 = t
    f_m = int(from_entry[2:4])
    t_m = int(to_entry[2:4])
    list1 = []
    pdf_path = pathlib.Path().absolute()
    for file_name in glob.iglob(str(pdf_path)+'\*.pdf', recursive=True):
        pdfs = file_name[::]
        list1.append(pdfs)
    path = []
    for j in list1:
        f_day = 1
        while f_day != 32:
            if f_day<10:
                if "0"+str(f_day)+"0"+str(f_m)+str(f_year) in j:
                    path.append(j)
                f_day+=1
            else:
                if str(f_day)+"0"+str(f_m)+str(f_year) in j:
                    path.append(j)
                f_day+=1
    for j in list1:
        t = 0
        while t != 32:
            if t<10:
                if "0"+str(t)+"0"+str(t_m)+"21" in j:
                    path.append(j)
                t+=1
            else:
                if str(t)+"0"+str(t_m)+"21" in j:
                    path.append(j)
                t+=1


    pdf_writer = PdfFileWriter()
    path = set(path)
    path = path
    print(path)
    for i in path:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(str(pdf_path)+"//Merged (PDF)//"+from_entry+"-"+to_entry+"."+"pdf", 'wb') as fh:
        pdf_writer.write(fh)

def admin_interface():
    login_admin.destroy()
    global app, twenty_four_entry, twenty_two_entry, nnn_silver_entry, nnf_silver_entry, cgst_entry, sgst_entry, tcs_entry, app_entry, profit_entry
    app = Tk()
    app.geometry("1920x1080")
    app.title("Varaha Satya Gold & Silver [ADMIN]")
    app.iconbitmap("gold.ico")
    a_bg = ImageTk.PhotoImage(file="gold_coins_wide.png")
    Label(app, image=a_bg).place(x=0,y=0)

    time = datetime.datetime.now()
    time = time.strftime("%d-%B-%Y")

    twenty_two_k = StringVar()
    twenty_four_k = StringVar()
    nnf_silver = StringVar()
    nnn_silver = StringVar()

    Label(app, text='WELCOME ADMIN !!\nDate: '+time, font=('Helvetica 16 bold underline'), fg="black", bg="white").pack()

    twenty_two_label = Label(app, text="Enter price of 1gm 22K gold", bg="#2A2A29", fg="white", font=('arial',15)).place(x=420, y=123)
    twenty_two_entry = Entry(app, borderwidth=5, textvariable=twenty_two_k, fg="black", bg="gold", width=40, font=('arial',15))
    twenty_two_entry.place(x=700, y=120)

    twenty_four_label = Label(app, text="Enter price of 1gm 24K gold", bg="#2A2A29", fg="white", font=('arial',15)).place(x=420, y=180)
    twenty_four_entry = Entry(app, borderwidth=5, textvariable=twenty_four_k, fg="black", bg="gold", width=40, font=('arial',15))
    twenty_four_entry.place(x=700, y=180)

    nnf_silver_label = Label(app, text="Enter price of 1gm 995 Silver", bg="#2A2A29", fg="white", font=('arial',15)).place(x=412, y=237)
    nnf_silver_entry = Entry(app, borderwidth=5, textvariable=nnf_silver, fg="black", bg="gold", width=40, font=('arial',15))
    nnf_silver_entry.place(x=700, y=237)

    nnn_silver_label = Label(app, text="Enter price of 1gm 999 Silver", bg="#2A2A29", fg="white", font=('arial',15)).place(x=412, y=294)
    nnn_silver_entry = Entry(app, borderwidth=5, textvariable=nnn_silver, fg="black", bg="gold", width=40, font=('arial',15))
    nnn_silver_entry.place(x=700, y=294)


    cgst_text = StringVar()
    sgst_text = StringVar()
    tcs_text = StringVar()
    app_text = StringVar()
    profit_text = StringVar()

    cgst_label = Label(app, text="Enter CGST", bg="#2A2A29", fg="white", font=('arial',15)).place(x=580, y=413)
    sgst_label = Label(app, text="Enter SGST", bg="#2A2A29", fg="white", font=('arial',15)).place(x=580, y=470)
    tcs_label = Label(app, text="Enter TCS", bg="#2A2A29", fg="white", font=('arial',15)).place(x=590, y=527)
    profit_label = Label(app, text="Enter PROFIT/gm", bg="#2A2A29", fg="white", font=('arial',15)).place(x=530, y=575)

    cgst_entry = Entry(app, borderwidth=5, fg="black", bg="gold", textvariable=cgst_text, width=40, font=('arial',15))
    cgst_entry.place(x=700, y=408)
    sgst_entry = Entry(app, borderwidth=5, fg="black", bg="gold", textvariable=sgst_text, width=40, font=('arial',15))
    sgst_entry.place(x=700, y=465)
    tcs_entry = Entry(app, borderwidth=5, fg="black", bg="gold", textvariable=tcs_text, width=40, font=('arial',15))
    tcs_entry.place(x=700, y=522)
    profit_entry = Entry(app, borderwidth=5, fg="black", bg="gold", textvariable=profit_text, width=40, font=('arial',15))
    profit_entry.place(x=700, y=569)

    new_cashier = Button(app, text="REGISTER NEW CASHIER", borderwidth=5, command=conformation2, fg="red", bg="black", font=('Helvetica 15 bold')).place(x=60,y=40)

    update_button = Button(app, text="Update", fg="black", bg="green", width=12,
    borderwidth=5, font=('Helvetica 17 bold'), command=conformation1).place(x=600, y=650)

    new_admin = Button(app, text="REGISTER NEW ADMIN", borderwidth=5, command=conformation5, fg="red", bg="black", font=('Helvetica 15 bold')
                       ).place(x=60,y=100)

    report_button  = Button(app, text="Report", fg="Red", bg="Black", width=12,
    borderwidth=5, font=('Helvetica 17 bold'), command=pdfs_choose).place(x=1300, y=80)
    
    logout_button = Button(app, text="Logout", fg="white", bg="red", font=('Arial 15 underline'), command=user_logout).place(x=1440, y=7)

    
    app.mainloop()
def user_logout():
    app.destroy()
    user_choice()

def update_profit():
    profit.destroy()
    global cgst_input, sgst_input, tcs_input, profit_input
    cgst_input = cgst_entry.get()
    sgst_input = sgst_entry.get()
    tcs_input = tcs_entry.get()
    profit_input = profit_entry.get()


def cashier_login():
    choice.destroy()
    global login_cashier
    global c_name_box, c_password_box
    login_cashier = Tk()
    login_cashier.geometry("512x512")
    login_cashier.title("Varaha Satya Gold & Silver [CASHIER]")
    login_cashier.iconbitmap("gold.ico")
    bg = PhotoImage(file="coins.png")
    cashier_bg = Label(login_cashier, image=bg)
    cashier_bg.place(x=0,y=0)
    #login_cashier.configure(bg="#2A2A29")
    
    user_name = StringVar()
    pass_word = StringVar()

    #This code below is for username details and boxes
    username_text = Label(login_cashier, text="Enter Username", fg="black", font=('Arial 17 bold'), bg="white").pack()
    c_name_box = Entry(login_cashier,  width=21, font=('Arial 17 bold'), borderwidth=5, bg="white", textvariable=user_name, fg="black")
    c_name_box.pack()

    #This code below is for password details and boxes
    password_text = Label(login_cashier, font=('Arial 17 bold'),text="Enter Password", fg="black", bg="white").pack()
    c_password_box = Entry(login_cashier, font=('Arial 17 bold'),width=21, borderwidth=5, bg="white", textvariable=pass_word, fg="black", show="*")
    c_password_box.pack()

    Label(login_cashier, text="\n",bg="white").pack()
    #Login button code chunk is below
    c_login_button = Button(login_cashier, text="Login", font=('Arial 17 bold'),fg="white", bg="green", command=cashier_check)
    c_login_button.pack()
    c_forgot_label = Button(login_cashier, text="Forgot Password!!", font=('Arial 13 bold'),fg="Red", bg="Black", command=cashier_forgot)
    c_forgot_label.pack()
    login_cashier.mainloop()


def update_cashier():
    register.destroy()

def update_admin():
    a_register.destroy()


def new_cashier_check():

    if (cashier_password_entry.get() != cashier_confirm_password_entry.get()):
        Label(register, text="Passwords do not match\nPlease check & type again !!", font=('arial 15 bold'), fg="red", bg="#F0F0F0").place(x=125,y=380)
    else:
        insert_cashier_values(cashier_name_entry.get(),cashier_password_entry.get())
        update_cashier()
def a_new_admin_check():
    if (admin_password_entry.get() != admin_confirm_password_entry.get()):
        Label(a_register, text="Passwords do not match\nPlease check & type again !!", font=('arial 15 bold'), fg="red", bg="#F0F0F0").place(x=125,y=380)
    else:
        insert_admin_values(admin_name_entry.get(),admin_password_entry.get())
        update_admin()

def register_admin():
    global list1,admin_fullname_entry,admin_name_entry, admin_password_entry, admin_confirm_password_entry, admin_phone_entry,a_register
    a_register = Toplevel()
    a_register.geometry("512x512")
    a_register.title("Varaha Satya Gold & Silver [NEW ADMIN]")
    r_bg = PhotoImage(file='coins2.png')
    label = Label(a_register, image=r_bg).place(x=0,y=0)
    a_register.iconbitmap("gold.ico")

    a_new_fullname = StringVar()
    a_new_username = StringVar()
    a_new_password = StringVar()
    a_confirm_password = StringVar()
    a_new_phonenumber = StringVar()

    admin_fullname = Label(a_register, text="Enter Full name of Admin", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    admin_fullname_entry = Entry(a_register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=a_new_fullname, bg="gold", fg="black")
    admin_fullname_entry.pack()

    admin_name = Label(a_register, text="Enter new Username", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    admin_name_entry = Entry(a_register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=a_new_username, bg="gold", fg="black") 
    admin_name_entry.pack()

    admin_password = Label(a_register, text="Enter new Password", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    admin_password_entry = Entry(a_register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=a_new_password, bg="gold", fg="black", show="*")
    admin_password_entry.pack()

    admin_confirm_password = Label(a_register, text="Confirm new Password", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    admin_confirm_password_entry = Entry(a_register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=a_confirm_password, bg="gold", fg="black", show="*")
    admin_confirm_password_entry.pack()

    admin_phone_label = Label(a_register, text="Enter Phone Number", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    admin_phone_entry = Entry(a_register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=a_new_phonenumber, bg="gold", fg="black")
    admin_phone_entry.pack()

    a_white_label = Label(a_register, text=" ", bg="#F0F0F0").pack()
    new_admin_submit = Button(a_register, borderwidth=5, text="SUBMIT", font=('Helvetica',12), fg="black", bg="green", command=a_new_admin_check).pack()

    a_register.mainloop()
        

def register_cashier():
    global cashier_fullname_entry,cashier_name_entry, cashier_password_entry, cashier_confirm_password_entry, cashier_phone_entry, register
    register = Toplevel()
    register.geometry("512x512")
    register.title("Varaha Satya Gold & Silver [NEW CASHIER]")
    r_bg = PhotoImage(file='coins2.png')
    label = Label(register, image=r_bg).place(x=0,y=0)
    register.iconbitmap("gold.ico")

    new_fullname = StringVar()
    new_username = StringVar()
    new_password = StringVar()
    confirm_password = StringVar()
    new_phonenumber = StringVar()

    cashier_fullname = Label(register, text="Enter Full name of Cashier", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    cashier_fullname_entry = Entry(register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=new_fullname, bg="gold", fg="black")
    cashier_fullname_entry.pack()

    cashier_name = Label(register, text="Enter new Username", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    cashier_name_entry = Entry(register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=new_username, bg="gold", fg="black") 
    cashier_name_entry.pack()

    cashier_password = Label(register, text="Enter new Password", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    cashier_password_entry = Entry(register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=new_password, bg="gold", fg="black", show="*")
    cashier_password_entry.pack()

    cashier_confirm_password = Label(register, text="Confirm new Password", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    cashier_confirm_password_entry = Entry(register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=confirm_password, bg="gold", fg="black", show="*")
    cashier_confirm_password_entry.pack()

    cashier_phone_label = Label(register, text="Enter Phone Number", font=('Helvetica',12), fg="black", bg="#F0F0F0").pack()
    cashier_phone_entry = Entry(register, font=('Helvetica',15), width=21, borderwidth=5, textvariable=new_phonenumber, bg="gold", fg="black")
    cashier_phone_entry.pack()

    white_label = Label(register, text=" ", bg="#F0F0F0").pack()
    new_cashier_submit = Button(register, borderwidth=5, text="SUBMIT", font=('Helvetica',12), fg="black", bg="green", command=new_cashier_check).pack()

    register.mainloop()
def cashier_check():
    global cashier_namee
    if(c_name_box.get() in c_list_u) and (c_password_box.get() == res2[c_name_box.get()]):
        cashier_namee = c_name_box.get()
        cashier_interface()
    else:
        Label(login_cashier, text="Invalid Credentials !!", fg="red", bg="#2A2A29").place(x=191,y=155)

def generate_bill():
    global list1,price,price_o,cgst,sgst,tcs
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            r = int(j)
    print(r)
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    #list1 = sheet.row_values(r)
    connection = sqlite3.connect("customer_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    row1 = cursor1.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            m = int(j)
    time = datetime.datetime.now()
    time = time.strftime("%d-%B-%Y")
    rb = xlrd.open_workbook("customer_details.xls")
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    w_sheet.write(m,0,time)
    w_sheet.write(m,1,customer_name.get())
    w_sheet.write(m,2,cust_address.get("1.0", END))
    w_sheet.write(m,3,cust_aadhar.get())
    w_sheet.write(m,4,cust_phone.get())
    print("grams",grams_entry.get())
    w_sheet.write(m,5,grams_entry.get())
    if typee=="22":
        w_sheet.write(m,6,_22k_g)
    elif typee=="24":
        w_sheet.write(m,6,_24k_g)
    elif typee=="995":
        w_sheet.write(m,6,_995k_g)
    elif typee=="999":
        w_sheet.write(m,6,_999k_g)
    w_sheet.write(m,7,payment_combo.get())
    w_sheet.write(m,8,str(price))
    print(grams_entry.get())
    print(profit)
    print(m)
    w_sheet.write(m,9,round(float(grams_entry.get())*float(profit)))
    w_sheet.write(m,10,typee)
    wb.save("customer_details.xls")
    row = (int(m)+1)
    print(row)
    connection = sqlite3.connect("customer_details.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Row SET row=? ",(row,))
    connection.commit()
    connection.close()
    print(bill(price))
def bill2():
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            p = int(j)
    p = p-1
    global typee,list1,price,price_o, _22k_g, _24k_g, _995k_g, _999k_g,profit,cgst,sgst,tcs
    typee = "24"
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    list1 = sheet.row_values(p)
    cgst = list1[1]
    sgst = list1[2]
    tcs = list1[3]
    profit = list1[4]
    _22k_g = list1[5]
    _24k_g = list1[6]
    _995k_g = list1[7]
    _999k_g = list1[8]
    print("You have selected 24k button!!!")
    price_o = round((float(profit)*float(grams_entry.get()))+float(_24k_g)*float(grams_entry.get()))
    price = round((price_o*(float(cgst)/100))+(price_o*(float(sgst)/100))+(price_o*(float(tcs)/100))+price_o)
    Label(app, text="The bill is "+str(price)+"/-" , fg="white", bg="#2A2A29").place(x=300, y=400)
def bill1():
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            p = int(j)
    p = p-1
    global typee,list1,price,price_o, _22k_g, _24k_g, _995k_g, _999k_g,profit,cgst,sgst,tcs
    typee = "22"
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    list1 = sheet.row_values(p)
    cgst = list1[1]
    sgst = list1[2]
    tcs = list1[3]
    profit = list1[4]
    _22k_g = list1[5]
    _24k_g = list1[6]
    _995k_g = list1[7]
    _999k_g = list1[8]
    print("You have selected 22k button!!!!")
    price_o = round((float(profit)*float(grams_entry.get()))+float(_22k_g)*float(grams_entry.get()))
    price = round((price_o*(float(cgst)/100))+(price_o*(float(sgst)/100))+(price_o*(float(tcs)/100))+price_o)
    print(price)
    Label(app, text="The bill is "+str(price)+"/-" , fg="white", bg="#2A2A29").place(x=300, y=400)
def bill3():
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            p = int(j)
    p = p-1
    global typee,list1,price,price_o, _22k_g, _24k_g, _995k_g, _999k_g,profit,cgst,sgst,tcs
    typee = "999"
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    list1 = sheet.row_values(p)
    cgst = list1[1]
    sgst = list1[2]
    tcs = list1[3]
    profit = list1[4]
    _22k_g = list1[5]
    _24k_g = list1[6]
    _995k_g = list1[7]
    _999k_g = list1[8]
    print("You have selected 999 Silver")
    price_o = round((float(profit)*float(grams_entry.get()))+float(_999k_g)*float(grams_entry.get()))
    price = round((price_o*(float(cgst)/100))+(price_o*(float(sgst)/100))+(price_o*(float(tcs)/100))+price_o)
    Label(app, text="The bill is "+str(price)+"/-" , fg="white", bg="#2A2A29").place(x=300, y=400)
def bill4():
    connection = sqlite3.connect("price_details.db")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute("SELECT * FROM Row")
    cursor2.execute("SELECT * FROM Colomn")
    row1 = cursor1.fetchall()
    colomn1 = cursor2.fetchall()
    connection.commit()
    connection.close()
    for i in row1:
        for j in i:
            p = int(j)
    p = p-1
    global typee,list1,price,price_o, _22k_g, _24k_g, _995k_g, _999k_g,profit,cgst,sgst,tcs
    typee = "995"
    loc_file = ("xlwt example.xls")
    wb = xlrd.open_workbook(loc_file) 
    sheet = wb.sheet_by_index(0) 
    list1 = sheet.row_values(p)
    cgst = list1[1]
    sgst = list1[2]
    tcs = list1[3]
    profit = list1[4]
    _22k_g = list1[5]
    _24k_g = list1[6]
    _995k_g = list1[7]
    _999k_g = list1[8]
    price_o = round((float(profit)*float(grams_entry.get()))+float(_995k_g)*float(grams_entry.get()))
    price = round((price_o*(float(cgst)/100))+(price_o*(float(sgst)/100))+(price_o*(float(tcs)/100))+price_o)
    Label(app, text="The bill is "+str(price)+"/-" , fg="white", bg="#2A2A29").place(x=300, y=400)

def invoice_insert_manual():
    global answer2, invoicee
    answer2 = None
    invoicee = invoice_entry.get()
    print(invoicee)
def invoice_insert_auto():
    global timee, answer2
    answer2 = messagebox.askquestion("Please Confirm", "Are you sure?")
    if answer2=="yes":
        with open("invoice_number.txt", 'r+') as file_obj1:
            text = now = file_obj1.read()
            diff = 6-len(str(int(now)))
            if len(str(int(now)))!= len(str(int(now)+1)):
                new = "0"*(diff-1)+str(int(now)+1)
            else:
                new = "0"*(diff)+str(int(now)+1)
            text = re.sub(str(now), new, text)
            file_obj1.seek(0)
            file_obj1.write(text)
            file_obj1.truncate()
    timee = now


def date_insert_manual():
    global datee
    datee = date_entry.get()
    print(datee)

def date_insert_auto():
    global datee
    answer1 = messagebox.askquestion("Please Confirm", "Are you sure?")
    datee = ""
    if answer1=="yes":
        datee = time.strftime("%d-%m-%y")
    print(datee)
def conformation7():
    generate_bill()
def cashier_interface():
    login_cashier.destroy()
    global app, tt_gold,tf_gold,nnn_silver,nnf_silver,data_manual,date_auto,invoice_auto,invoice_manual, var1, var2, var3, var4, gold_grams, grams_entry, nnn_silver,gstin_entry, date_entry,invoice_entry,payment_combo,customer_name,cust_aadhar,cust_address,cust_phone
    app = Tk()
    app.geometry("1920x1080")
    app.title("Varaha Satya Gold & Silver [CASHIER]")
    app.iconbitmap("gold.ico")
    a_bg = PhotoImage(file="gold_coins_wide.png")
    mo = Label(app, image=a_bg)
    mo.place(x=0,y=0)
    app.configure(bg="#607399")
    cust_name = StringVar()
    cust_phone = StringVar()
    date = StringVar()
    cust_aadhar = StringVar()
    gold_grams = IntVar()
    gstin = StringVar()
    tt_gold_price = IntVar()
    invoice = StringVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    n = StringVar()
    time = datetime.datetime.now()
    time = time.strftime("%d-%B-%Y")

    Label(app, text='WELCOME CASHIER !!\nDate: '+time, font=('Helvetica 16 bold underline'), fg="black", bg="white").pack()    
    logout_button = Button(app, text="Logout", fg="white", bg="red", font=('Arial 15 underline'), command=user_logout).place(x=1440, y=7)


    cust_name_label = Label(app, text="Enter Customer's Name", font=('Helvetica',17), fg="white", bg="#607399").place(x=480, y=88)
    customer_name = Entry(app, font=('Helvetica',17), width=30, borderwidth=5, textvariable=cust_name, bg="grey", fg="black")
    customer_name.place(x=400, y=120)

    cust_phone_label = Label(app, text="Enter Customer's Phone number", font=('Helvetica',17), fg="white", bg="#607399").place(x=850,y=88)
    cust_phone = Entry(app, font=('Helvetica',17), width=21, borderwidth=5, textvariable=cust_phone, bg="grey", fg="black")
    cust_phone.place(x=880, y=120)

    cust_aadhar_label = Label(app, text="Enter Customer's Aadhar Number", font=('Helvetica',15), fg="white", bg="#607399").place(x=450,y=180)
    cust_aadhar = Entry(app, font=('Helvetica',15), width=21, borderwidth=5, textvariable=cust_aadhar, bg="grey", fg="black")
    cust_aadhar.place(x=470,y=210)

    cust_address_label = Label(app, text="Enter Customer's address", font=('Helvetica',15), fg="white", bg="#607399").place(x=900,y=180)
    #cust_address = Entry(app, font=('Helvetica',15), borderwidth=5, textvariable=cust_address, bg="grey", fg="black")
    cust_address = Text(app,height = 6, width = 25, bg = "grey", fg = "black", font = ('Helvetica',13))
    cust_address.place(x=900, y=210 )
    grams_label = Label(app, text="Enter weight of metal\n(grams)", font=('Helvetica',15), fg="white", bg="#607399").place(x=450,y=323)
    #grams_entry = Entry(app, font=('Helvetica',18), width=21, borderwidth=9, textvariable=gold_grams, bg="light green", fg="black")
    grams_entry = Entry(app, font=('Helvetica',18), width=21, borderwidth=9, textvariable=gold_grams, bg="light green", fg="black")
    grams_entry.place(x=690, y=325)

    
    tt_gold = Radiobutton(app, text="22 Carat Gold", font=('Helvetica',15), activeforeground="white", fg="black",  bg="orange", 
    command=bill1, activebackground="#607399", variable=var1, value = 1).place(x=480,y=450) #onvalue=1, offvalue=0

    tf_gold = Radiobutton(app, text="24 Carat Gold", font=('Helvetica',15), activeforeground="white", fg="black",  bg="gold", 
    command=bill2, borderwidth=5, activebackground="#607399", variable=var1,value = 2).place(x=920,y=450)

    nnn_silver = Radiobutton(app, text="999 Silver", font=('Helvetica',15), activeforeground="white", fg="black",  bg="white", 
    command=bill3, borderwidth=5, activebackground="#607399", variable=var1, value = 3).place(x=480,y=500)

    nnf_silver = Radiobutton(app, text="995 Silver", font=('Helvetica',15), activeforeground="white", fg="black",  bg="silver", 
    command=bill4, borderwidth=5, activebackground="#607399", variable=var1, value = 4).place(x=920,y=500)

    date_label = Label(app, text = "Date:", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=150)
    date_entry = Entry(app, font=('Helvetica',15), borderwidth=5, textvariable=date, bg="grey", fg="black")
    date_entry.place(x=100,y=150)
    
    date_confrim = Label(app, text = "Date:", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=80)
    date_manual = Radiobutton(app, text="Manual", font=('Helvetica',15), activeforeground="gold", fg="black",  bg="gold", 
    command=date_insert_manual, borderwidth=5, activebackground="#607399", variable=var2, value = 5).place(x=100,y=80)
    date_auto = Radiobutton(app, text="Automatic", font=('Helvetica',15), activeforeground="gold", fg="black",  bg="gold", 
    command=date_insert_auto, borderwidth=5, activebackground="#607399", variable=var2, value = 6).place(x=250,y=80)

    invoice_label = Label(app, text = "Invoice:", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=250)
    invoice_entry = Entry(app, font=('Helvetica',15), borderwidth=5, textvariable=invoice, bg="grey", fg="black")
    invoice_entry.place(x=100,y=250)
    
    invoice_confrim = Label(app, text = "Invoice", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=200)
    invoice_manual = Radiobutton(app, text="Manual", font=('Helvetica',15), activeforeground="gold", fg="black",  bg="gold", 
    command=invoice_insert_manual, borderwidth=5, activebackground="#607399", variable=var3, value = 7).place(x=100,y=200)
    invoice_auto = Radiobutton(app, text="Automatic", font=('Helvetica',15), activeforeground="gold", fg="black",  bg="gold", 
    command=invoice_insert_auto, borderwidth=5, activebackground="#607399", variable=var3, value = 8).place(x=250,y=200)

    payment_type = Label(app, text = "Payment Type", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=400)
    payment_combo = ttk.Combobox(app, width = "20", height = "30", font=('Helvetica',15), textvariable = n)
    payment_combo['values'] = ('CASH','UPI','CARD','CHEQUE')
    payment_combo.place(x=20,y=430)
    gstin_label = Label(app, text = "GSTIN:", font = ('Helvetica',15), fg="white", bg="#607399").place(x=10,y=500)
    gstin_entry = Entry(app, font=('Helvetica',15), borderwidth=5, textvariable=gstin, bg="grey", fg="black")
    gstin_entry.place(x=100,y=500)
    generate_bill_button = Button(app, borderwidth=5, text="GENERATE BILL", font=('Helvetica',20), fg="black", bg="green", command=conformation7).place(x=660, y=600)
    #new_payment_botton = Button(app, borderwidth=5, text="New Payment", font=('Helvetica',20), fg="black", bg="red", command=conformation7).place(x=950, y=600) 
    app.mainloop()

def user_choice():
    global choice
    choice = Tk()
    choice.geometry("512x512")
    choice.configure(bg = "#DE911F")
    choice.title("Varaha Satya Gold & Silver")
    choice.iconbitmap("gold.ico")
    c_bg = PhotoImage(file="coins.png")
    Label(choice, image=c_bg).place(x=0,y=0)
    admin_button = Button(choice, text="ADMIN", borderwidth=5, fg="red", bg="white", font=('Helvetica 15 bold'), width=25, height=2, command=admin_login).place(x=100, y=80)
    cashier_button = Button(choice, text="CASHIER", borderwidth=5, fg="green", bg="white", font=('Helvetica 15 bold'), width=25, height=2, command=cashier_login).place(x=100, y=200)
    choice.mainloop()

user_choice()

