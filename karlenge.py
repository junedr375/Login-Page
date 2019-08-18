from tkinter import*
import os
def deslogin():
    q.destroy()
def delete0():
    
    v.destroy()


def delete1():
    r.destroy()

def login_succes():
    def fun1():
        print("juned")


    def resize():
        print("juned")
        p.geometry("200x300")
          

    def default():
        print("juned")
        p.geometry("400x500")

   

        pathlabel.config(text=filename)
    global v
    v=Toplevel(q)
    
    v.geometry("200x300")

    menu= Menu(v)


    v.config(menu=menu)

    subMenu1=Menu(menu)
    subMenu2=Menu(menu)
    menu3=Menu(menu)


    menu.add_cascade(label="My Account",menu=subMenu1,font=40)
    menu.add_cascade(label="Profile",menu=subMenu2,font=40)
    subMenu1.add_command(label="Address",command=fun1,font=30)
    subMenu1.add_command(label="My Rewards",command=fun1,font=30)
    subMenu1.add_command(label="DY Cash",command=fun1,font=30)
    subMenu1.add_command(label="Logout",command=delete0,font=30)
    subMenu1.add_separator()
    subMenu1.add_command(label="EXIT",command=delete0)

    subMenu2.add_command(label="Edit",command=fun1)
    subMenu2.add_command(label="Help",command=fun1)
    subMenu1.add_cascade(label="Adress",subMenu1=menu3,font=40)
    menu3.add_command(label="View",command=fun1)
    menu3.add_command(label="Edit",command=fun1)

    pathlabel=Label(v).pack()


def delete3():
    t.destroy()

def delete4():
    u.destroy()
    

def ps_nf():
    global t
    t=Toplevel(p)
    t.title("Success")
    t.geometry("150x100")
    l8=Label(t,text="Password Error").pack()
    b6=Button(t,text="OK",command=delete3).pack() 



def un_nf():
    global u
    u=Toplevel(p)
    u.title("Success")
    u.geometry("150x100")
    l8=Label(u,text="User not Found").pack()
    b7=Button(u,text="OK",command=delete4).pack() 


def sign1():
    nm=name.get()
    ps=password.get()
    em=email.get()
    ph=phone.get()
    print(nm)
    print(ps)

    b=open(nm,'w')
    b.write(nm+ "\n")
    b.write(ps+ "\n")
    b.write(em+ "\n")
    b.write(ph)
    b.close

    Label(r,text="Succesfully Signed Up",font=30,fg="green").pack()

def login():
    global q
    q = Toplevel(p)
    q.title("LOGIN")
    q.geometry("300x200")


    global un
    global ps
    global e1
    global e2

    un=StringVar()
    ps=StringVar()
    
    
    l3=Label(q,text='Username',font=30,fg='black',bg='orange').pack()
    e1=Entry(q,textvariable = un,font=30)
    e1.pack()

    l5=Label(p,text='                             ').pack()
    
    l4=Label(q,text='Password',font=30,fg='black',bg='orange').pack()
    e2=Entry(q,textvariable = ps,font=30)
    e2.pack()
    l5=Label(p,text='                             ').pack()
    
    c1=Checkbutton(q,text='Stay Logged In',fg='black',bg='orange').pack()
    
    b3=Button(q,text='LOGIN',command=login1,fg='black',bg='orange',width="50",height="2").pack()
    b4=Button(q,text='Back',command=deslogin,fg='black',bg='orange',width="25",height="1").pack()

    
    q.mainloop()

def login1():
    un_info = un.get()
    ps_info = ps.get()
    
    e1.delete(0,END)
    e2.delete(0,END)

    list_of_files = os.listdir()
    if un_info in list_of_files:
        file1=open(un_info,"r")
        verify=file1.read().splitlines()
        if ps_info in verify:
            print("login Succesful")
            login_succes()
            Label(q,text="login Succesful",font=30,fg="green").pack()
        else:
            print("Password is wrong")
            ps_nf()
            Label(q,text="Password is Wrong",font=30,fg="green").pack()
    else:
        print("User not found:")
        un_nf()
        Label(q,text="User not found",font=30,fg="green").pack()



def sign():
    global r
    r=Toplevel(p)
    
    r.geometry("200x300")

    global name
    global password
    global email
    global phone
    global e3
    global e4
    global e5
    global e6

    
    name=StringVar()
    password=StringVar()
    email=StringVar()
    phone=StringVar()
    


    l3=Label(r,text='Username',font=30,fg='black',bg='orange').pack()
    e3=Entry(r,textvariable=name).pack()
    l5=Label(p,text='                             ').pack()
    
    l4=Label(r,text='Password',font=30,fg='black',bg='orange').pack()
    e4=Entry(r,textvariable=password).pack()
    l5=Label(p,text='                             ').pack()
    
    l6=Label(r,text='Email Id',font=30,fg='black',bg='orange').pack()
    e5=Entry(r,textvariable=email).pack()
    l5=Label(p,text='                             ').pack()
    
    l7=Label(r,text='Phone Number',font=30,fg='black',bg='orange').pack()
    e6=Entry(r,textvariable=phone).pack()
    l5=Label(p,text='                             ').pack()
    
    c1=Checkbutton(r,text='I Agree with term and Condition',fg="green").pack()
    b3=Button(r,text='Submit',command=sign1,fg='blue',width="30",height="1").pack()
    b4=Button(r,text='EXIT',fg="red",command=delete1,width="50",height="1").pack()

    r.mainloop()
    

p=Tk()
p.title("Welcome")
p.geometry("400x400")


l1=Label(p,text="Welcome",fg="grey",bg='brown',font=('Bold',25)).pack()
l5=Label(p,text='                             ').pack()
l5=Label(p,text='                             ').pack()
l5=Label(p,text='                             ').pack()



b1=Button(p,text="LOGIN" ,command=login,width="50",height="1",fg="black",bg="orange",font=('bold',20)).pack()
l5=Label(p,text='                             ').pack()

b2=Button(p,text="SIGN UP" ,command=sign,width="50",height="1",fg="black",bg="orange",font=('bold',20)).pack()
l5=Label(p,text='                             ').pack()

b8=Button(p,text='EXIT',fg="black",bg="orange",width="50",height="1",command=quit).pack(fill=X)

p.mainloop()
