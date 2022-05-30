from tkinter import*
from tkinter import font
root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)
def Reset():
    entry_dosa.delete(0,END)
    entry_Idly.delete(0,END)
    entry_Parota.delete(0,END)
    entry_Juice.delete(0,END)
    entry_water.delete(0,END)
    entry_Poori.delete(0,END)
def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(Idly.get())
    except:a2=0

    try:a3=int(Parota.get())
    except:a3=0
    
    try:a4=int(Juice.get())
    except:a4=0

    try:a5=int(water.get())
    except:a5=0

    try:a6=int(Poori.get())
    except:a6=0

#cost
    c1=35*a1
    c2=8*a2
    c3=10*a3
    c4=30*a4
    c5=15*a5
    c6=35*a6
    
    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="pink")
    entry_total.place(x=20,y=100)

    Bill1=Label(f2,text="THANK YOU!!!",font=("calibri",20,"bold"),bg="lightyellow")
    Bill1.place(x=70,y=180)
    Bill2=Label(f2,text="COME AGAIN!!!",font=("calibri",20,"bold"),bg="lightyellow")
    Bill2.place(x=70,y=230)
    Bill2=Label(f2,text="HAVE A NICE DAY!!!",font=("calibri",20,"bold"),bg="lightyellow")
    Bill2.place(x=70,y=280)

    totalcost=c1+c2+c3+c4+c5+c6
    string_bill=("Rs.",totalcost,".00","/---")
    Total_bill.set(string_bill)


    
#title  
Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2" ).pack()
Label(text="By Vigneswaraa MS",bg="yellow",fg="black",font=("calibri",20),width="15",height="1" ).place(x=750,y=75)

#menu frame
f=Frame(root,bg="orange",highlightbackground="black",highlightthickness=5,width=300,height=370)
f.place(x=10,y=118)

#menu card
Label(f,text="MENU",font=("Gabriola",40,"bold"),fg="black",bg="orange").place(x=80,y=0)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa=Rs.35",fg="black",bg="orange").place(x=10,y=80)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Idly=Rs.8",fg="black",bg="orange").place(x=10,y=110)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Parota=Rs.10",fg="black",bg="orange").place(x=10,y=140)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Poori=Rs.35",fg="black",bg="orange").place(x=10,y=170)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Juice=Rs.30",fg="black",bg="orange").place(x=10,y=200)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Water=Rs.15",fg="black",bg="orange").place(x=10,y=230)

#bill board
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20,"bold"),bg="lightyellow")
Bill.place(x=120,y=10)

#enter work
f1=Frame(root,bd=5,height=370,width=250,relief=RAISED)
f1.pack()

dosa=StringVar()
Idly=StringVar()
Parota=StringVar()
Poori=StringVar()
Juice=StringVar()
water=StringVar()
Total_bill=StringVar()

#label text

lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=10,fg="blue4")
lbl_Idly=Label(f1,font=("aria",20,'bold'),text="Idly",width=10,fg="blue4")
lbl_Parota=Label(f1,font=("aria",20,'bold'),text="Parota",width=10,fg="blue4")
lbl_poori=Label(f1,font=("aria",20,'bold'),text="Poori",width=10,fg="blue4")
lbl_Juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=10,fg="blue4")
lbl_water=Label(f1,font=("aria",20,'bold'),text="Water",width=10,fg="blue4")
lbl_dosa.grid(row=1,column=0)
lbl_Idly.grid(row=2,column=0)
lbl_Parota.grid(row=3,column=0)
lbl_poori.grid(row=4,column=0)
lbl_Juice.grid(row=5,column=0)
lbl_water.grid(row=6,column=0)

#entry
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=6,bg="pink")
entry_Idly=Entry(f1,font=("aria",20,"bold"),textvariable=Idly,bd=6,width=6,bg="pink")
entry_Parota=Entry(f1,font=("aria",20,"bold"),textvariable=Parota,bd=6,width=6,bg="pink")
entry_Poori=Entry(f1,font=("aria",20,"bold"),textvariable=Poori,bd=6,width=6,bg="pink")
entry_Juice=Entry(f1,font=("aria",20,"bold"),textvariable=Juice,bd=6,width=6,bg="pink")
entry_water=Entry(f1,font=("aria",20,"bold"),textvariable=water,bd=6,width=6,bg="pink")
entry_dosa.grid(row=1,column=1)
entry_Idly.grid(row=2,column=1)
entry_Parota.grid(row=3,column=1)
entry_Poori.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_water.grid(row=6,column=1)

#button
btn_reset=Button(f1,bd=5,bg="lightblue",fg="black",font=("ariel",20,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,bg="lightblue",fg="black",font=("ariel",20,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)



root.mainloop()
