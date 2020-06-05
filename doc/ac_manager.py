from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

window = Tk()
window.title("Sumit")
window.geometry('1350x700')

web=StringVar()
usr=StringVar()
pas=StringVar()
new_usr=StringVar()
new_pas=StringVar()

bg_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\black.png")
logout_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\logout.png")
add_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\add.png")
search_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\search.png")
update_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\update.png")
delete_ico=PhotoImage(file=r"C:\Users\sumit\Desktop\projects\delete.png")


bg_lbl=Label(window,image=bg_ico).pack()
title=Label(window,text='Password Management System',font=("Times New Roman",40,"bold"),bg='light blue',fg='white',bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)
   
frame=Frame(window,bg='white',bd=10,relief=GROOVE)  
frame.place(x=300,y=150)
lbl_1=Label(frame,text="Welcome To Account Management System",font=("Times New Roman",15,"bold"),bg='white').grid(row=0,columnspan=1)
lbl_2=Label(frame,text="Select what you want to do",font=("Times New Roman",15,"bold"),bg='white').grid(row=1,columnspan=1)

def db_add():  
    if usr.get()=="" and web.get()=="" and pas.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
    else :
        cur.execute("INSERT INTO manager VALUES(?,?,?)",(web.get(),usr.get(),pas.get(),))
        conn.commit()
        messagebox.showinfo("Add","Data Added")
        web.set("")
        usr.set("")
        pas.set("")

def db_search():
    tree = ttk.Treeview(frame2)
    tree["columns"] = ("0", "1", "2")
    tree.heading("0", text="Website")
    tree.heading("1", text="Username")
    tree.heading("2", text="Password")
                
    tree.column("#0",minwidth=0,width=0)
    tree.column("0",minwidth=0,width=200)
    tree.column("1",minwidth=0,width=250)
    tree.column("2",minwidth=0,width=248)


    tree.place(x=-2,y=200)
    cursor = cur.execute("SELECT * FROM manager WHERE website=?",(web.get(),))
    i=0
    if cursor==None :
        messagebox.showerror("Error","No Records Found")
    for row in cursor:
        tree.insert('',i,values=row)
        i=i+1    

def db_update_usr():
    if usr.get()=="" and web.get()=="" and new_usr.get()=="":
        messagebox.showerror("Error","All Fields Are Requigrey80")
    else :
        ad=cur.execute('''UPDATE manager SET user=? WHERE website=? AND user=?''',(new_usr.get(),web.get(),usr.get(),))
        conn.commit()
        print(ad)
        messagebox.showinfo("Update","Username Updated Succesfully")
        web.set("")
        usr.set("")
        new_usr.set("")

def db_update_pas():
    if new_pas.get()=="" and pas.get()=="" and usr.get()=="" :
        messagebox.showerror("Error","All Fields Are Required")
    else :
        cur.execute('''UPDATE manager SET password=? WHERE user=? AND password=?''',(new_pas.get(),usr.get(),pas.get(),))
        conn.commit()
        messagebox.showinfo("Update","Password Updated Succesfully")
        pas.set("")
        usr.set("")
        new_pas.set("")
     


            


def add():
    bg_lbl=Label(window,image=bg_ico).pack()
    frame1=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame1.place(x=300,y=150,relheight=0.5)
    lbl=Label(frame1,text="     Add Data",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    lbl_web=Label(frame1,text="Enter Website",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    txtweb=Entry(frame1,textvariable=web,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
    lbl_usr=Label(frame1,text="Enter Username",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
    txtusr=Entry(frame1,textvariable=usr,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
    lbl_pas=Label(frame1,text="Enter Password",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=4,column=0,padx=20,pady=10)
    txtpass=Entry(frame1,textvariable=pas,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
    log_btn=Button(frame1,text='Add',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=db_add).grid(row=5,column=1)
    log_btn=Button(frame1,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=frame1.destroy).grid(row=6,column=1)




def search():
        
    bg_lbl=Label(window,image=bg_ico).pack()
    frame2=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame2.place(x=200,y=150,relheight=0.7,relwidth=0.7)
    lbl=Label(frame2,text="     Search Data",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    lbl_web=Label(frame2,text="Enter Website",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    txtweb=Entry(frame2,textvariable=web,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)       
    def db_search():
        tree = ttk.Treeview(frame2)
        tree["columns"] = ("0", "1", "2")
        tree.heading("0", text="Website")
        tree.heading("1", text="Username")
        tree.heading("2", text="Password")
                    
        tree.column("#0",minwidth=0,width=0)
        tree.column("0",minwidth=0,width=200)
        tree.column("1",minwidth=0,width=250)
        tree.column("2",minwidth=0,width=248)


        tree.place(x=-2,y=200)
        cursor = cur.execute("SELECT * FROM manager WHERE website=?",(web.get(),))
        i=0
        if cursor==None :
            messagebox.showerror("Error","No Records Found")
        for row in cursor:
            tree.insert('',i,values=row)
            i=i+1   
    def back():
        web.set("")
        frame2.destroy()
    sch_btn=Button(frame2,text='Search',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=db_search).grid(row=3,column=1)
    back_btn=Button(frame2,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=back).grid(row=4,column=1)



        

def up_usr():
    frame3=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame3.place(x=200,y=150,relheight=0.5,relwidth=0.6)
    lbl_1=Label(frame3,text="  To Update Username",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    lbl_web=Label(frame3,text="Enter Website",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    txtweb=Entry(frame3,textvariable=web,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
    lbl_usr=Label(frame3,text="Enter Username",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
    txtusr=Entry(frame3,textvariable=usr,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
    lbl_new_usr=Label(frame3,text="Enter New Username",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=4,column=0,padx=20,pady=10)
    txt_new_usr=Entry(frame3,textvariable=new_usr,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
    upd_btn=Button(frame3,text='Update',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=db_update_usr).grid(row=5,column=1)
    back_btn=Button(frame3,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=frame3.destroy).grid(row=6,column=1)
            

def up_pas():
    frame3=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame3.place(x=200,y=150,relheight=0.5,relwidth=0.6)
    lbl_1=Label(frame3,text="  To Password",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    lbl_web=Label(frame3,text="Enter Username",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    txtweb=Entry(frame3,textvariable=usr,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
    lbl_usr=Label(frame3,text="Enter Password",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
    txtusr=Entry(frame3,textvariable=pas,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
    lbl_new_usr=Label(frame3,text="Enter New Password",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=4,column=0,padx=20,pady=10)
    txt_new_usr=Entry(frame3,textvariable=new_pas,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
    upd_btn=Button(frame3,text='Update',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=db_update_pas).grid(row=5,column=1)
    back_btn=Button(frame3,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=frame3.destroy).grid(row=6,column=1)
            
def update():
    bg_lbl=Label(window,image=bg_ico).pack()
    frame3=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame3.place(x=300,y=150,relheight=0.5,relwidth=0.4)
    lbl_1=Label(frame3,text="     Update Data",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    lbl_2=Label(frame3,text=" Select What you want to do ",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    usr_btn=Button(frame3,text='Update Username',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=up_usr).grid(row=3,column=0)
    pas_btn=Button(frame3,text='Update Password',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=up_pas).grid(row=4,column=0)
    back_btn=Button(frame3,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=frame3.destroy).grid(row=5,column=0)
        
        

def delete() :
    bg_lbl=Label(window,image=bg_ico).pack()
    frame4=Frame(window,bg='white',bd=10,relief=GROOVE)  
    frame4.place(x=200,y=150,relheight=0.7,relwidth=0.7)
    def dis_all() :   
        tree = ttk.Treeview(frame4)
        verscrlbar = ttk.Scrollbar(frame4, orient ="vertical", command = tree.yview).place(x=632,y=300,relheight=0.35) 
        tree["columns"] = ("0", "1", "2")
        tree.heading("0", text="Website")
        tree.heading("1", text="Username")
        tree.heading("2", text="Password")               
        tree.column("#0",minwidth=0,width=0)
        tree.column("0",minwidth=0,width=180)
        tree.column("1",minwidth=0,width=250)
        tree.column("2",minwidth=0,width=180)
        tree.place(x=30,y=300,relheight=0.35)
        cursor = cur.execute("SELECT * FROM manager ")
        i=0
        if cursor==None :
            messagebox.showerror("Error","No Records Found")
        for row in cursor:
            tree.insert('',i,values=row)
            i=i+1
    def db_delete():
        if  usr.get()=="" and  pas.get()==""  :
            messagebox.showerror("Error","All Fields Are Required")
        else :
            cur.execute('''DELETE FROM manager WHERE user=? AND password=?''',(usr.get(),pas.get()))
            conn.commit()
            messagebox.showinfo("Delete","Password Deleted Succesfully")
            pas.set("")
            usr.set("")
            dis_all()
            
    lbl_1=Label(frame4,text="Delete Data",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=1,columnspan=2,padx=20,pady=5)
    lbl_2=Label(frame4,text="  Enter Following Details",compound=CENTER,font=("Times New Roman",20,"bold")).grid(row=2,columnspan=2,padx=20,pady=5)
    lbl_web=Label(frame4,text="Username",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
    txtweb=Entry(frame4,textvariable=usr,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
    lbl_usr=Label(frame4,text="Password",compound=LEFT,font=("Times New Roman",20,"bold")).grid(row=4,column=0,padx=20,pady=10)
    txtusr=Entry(frame4,textvariable=pas,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
    del_btn=Button(frame4,text='Delete',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=db_delete).grid(row=5,column=1)
    back_btn=Button(frame4,text='Back',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='red',command=frame4.destroy).grid(row=6,column=1)
    dis_all()         

       
                
def iExit():
    iExit=messagebox.askyesno("Password Management","Confirm if you want to exit")
    if iExit > 0 :
        window.destroy()
    
            
            
    #add_btn=Button(frame,text='Add Data ',width=15,font=("Times New Roman",14,"bold"),bg='royalblue',fg='grey80',command=add).grid(row=2)

add_btn=Button(frame,image=add_ico,command=add).grid(row=2)
search_btn=Button(frame,image=search_ico,command=search).grid(row=3)
update_btn=Button(frame,image=update_ico,command=update).grid(row=4)
delete_btn=Button(frame,image=delete_ico,command=delete).grid(row=5)
logout_btn=Button(frame,image=logout_ico,command=iExit).grid(row=6)

window.mainloop()
    
