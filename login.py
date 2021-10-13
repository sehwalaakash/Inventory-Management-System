from tkinter import *
from PIL import ImageTk # pip install pillow
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed by Aakash Sharma")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.otp=''

        #=================================Images=================================
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #===============All Variables==================
        self.employee_id=StringVar()
        self.password=StringVar()

#============================================================================================================================================================================================================================
        #======================================================FrontEnd Development======================================================
        
        #=================================Login System Frame=================================
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)


        #==========Title==========
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        #=============================================================================================================

        #============================================Text and Labels============================================

        
        #==========User Name Label==========
        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)


        #==========User Name Text==========
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        #==========Password Label==========
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)

        #==========Password Text==========
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        #=============================================================================================================

        #============================================Buttons============================================

        #==========Login Button==========
        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="violet",fg="white",activeforeground="black",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        #=============================================================================================================

        #========== Horizontal Line ==========
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        
        #========== OR Label ==========
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        #=============================================================================================================

        #============================================Buttons============================================

        #==========Forget Password Button==========
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E",cursor="hand2",bd=0).place(x=100,y=390)
        
        #=============================================================================================================

        #============================================================================================================================================================================================================================

        #===================================================Frame2===================================================
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        #=============================================================================================================

        #==========================================Labels==========================================

        #============Register Label============
        lbl_reg=Label(register_frame,text="SUBSCRIBE | LIKE | SHARE ",font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)
        
        #=============================================================================================================

        #============================================Buttons============================================

        #==========Signup Button==========
        # btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E",cursor="hand2",bd=0).place(x=200,y=17)
        
        #=============================================================================================================

        #============================================Animation Images============================================
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        
        
        self.animate()

        
#============================================================================================================================================================================================================================
        
        #======================================================BackEnd Development======================================================

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
    
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All Fields are required.",parent=self.root)

            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()

                if user==None:
                    messagebox.showerror("Error","Invalid Username/Password!!!",parent=self.root)
                
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")

                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required.",parent=self.root)

            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()

                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID \n Try Different.",parent=self.root)
                
                else:
    #====================================================================================================================
    #==============================================FORGET WINDOW==============================================                    
                    
                    #======All Variables======
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    # call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error \n Try Again!!!!",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="RESET PASSWORD",font=('goudy old style',15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)

                        lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)

                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='lightyellow').place(x=20,y=100,width=250,height=30)

                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("times new roman",15),bg='lightblue')
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)

                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)

                        lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)

                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forget_win,text="UPDATE",state=DISABLED,command=self.update_password,font=("times new roman",15),bg='lightblue')
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
       
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required.",parent=self.forget_win)

        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","Password mismatched.\n Try Again!!",parent=self.forget_win)

        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee set pass=? where eid=? ", (self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully.",parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
       

    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)

        else:
            messagebox.showerror("Error","Invalid OTP \n Try Again!!!!",parent=self.forget_win)


    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)              

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))

        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam \n\n Your OTP for Reset Password is {str(self.otp)}. \n\n With Regards, \n IMS Team.'
        msg="Subject:{}\n\n{}".format(subj,msg)

        s.sendmail(email_,to_,msg)
        chk=s.ehlo()

        if chk[0]==250:
            return 's'
        else:
            return 'f'

root=Tk()
obj=Login_System(root)
root.mainloop()