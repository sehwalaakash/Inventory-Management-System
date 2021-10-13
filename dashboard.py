from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass  
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #=====Title=====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Times New Roman",40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====Button_Logout====
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("Times New Roman",15,"bold"),cursor="hand2",bg="yellow").place(x=1150,y=10,height=50,width=150)

        #====Clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",font=("Times New Roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=25)

        #====LeftMenu====
        self.MenuLogo=Image.open("E:\Project\Inventory Management System\images\menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X) #X is used to resize the image according to the width of the frame

        self.icon_side=PhotoImage(file="images/side.png")
        #====Menu Label====
        lbl_menu=Label(LeftMenu,text="Menu",font=("Times New Roman",20),bg="#009688",fg="white").pack(side=TOP,fill=X)

        #====Employee Button====
        btn_employee=Button(LeftMenu,text="Employee",image=self.icon_side,command=self.employee,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#33bbf9",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Supplier Button====
        btn_supplier=Button(LeftMenu,text="Supplier",image=self.icon_side,command=self.supplier,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#ff5722",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Category Button====
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,command=self.category,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#009688",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Products Button====
        btn_products=Button(LeftMenu,text="Products",image=self.icon_side,command=self.product,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#607d8b",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Sales Button====
        btn_employee=Button(LeftMenu,text="Sales",image=self.icon_side,command=self.sales,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#ffc107",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Exit Button====
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="#524559",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #=============================Content=============================

        #---Employee Label---
        self.lbl_employee=Label(self.root,text="Total Employee \n [ 0 ]",bd=5,relief=RIDGE, bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        #---Supplier Label---
        self.lbl_supplier=Label(self.root,text="Total Supplier \n [ 0 ]",bd=5,relief=RIDGE, bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        #---Category Label---
        self.lbl_category=Label(self.root,text="Total Category \n [ 0 ]",bd=5,relief=RIDGE, bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        #---Product Label---
        self.lbl_product=Label(self.root,text="Total Products \n [ 0 ]",bd=5,relief=RIDGE, bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        #---Sales Label---
        self.lbl_sales=Label(self.root,text="Total Sales \n [ 0 ]",bd=5,relief=RIDGE, bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        #====Footer====
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by Aakash Sharma \n For any Technical Issue, Contact: 9468497114",font=("Times New Roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()

#========================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)


    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Products \n [ {str(len(product))} ]")
        
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers \n [ {str(len(supplier))} ]")

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category \n [ {str(len(category))} ]")
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee \n [ {str(len(employee))} ]")

            bill=os.listdir('bill')
            self.lbl_sales.config(text=f'Total Sales \n [{str(len(bill))}]')  

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date: {str(date_)} \t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)


        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()


