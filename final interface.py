from tkinter import *


APP = Tk()
APP.geometry("900x900")


def Welcome_to_GameInt():

    mainF = Frame(APP)
    mainF.place(height=900,width=900)


    Welcome_to_GameInt = Frame(mainF,bg='white')
    Welcome_to_GameInt.place(x=150,y=8,height=790,width=900)

    Label(Welcome_to_GameInt,text="Welcome to GameInt",fg="red",bg="white",font=('Times New Roman',25,'bold','italic')).place(x=200,y=10)
    
    e1=Entry(Welcome_to_GameInt,border=0,bg="#dddddd",fg="#929292")
    e1.place(x=250,y=80,height=35,width=200)
    e1.insert(0,'Your Name')


    Button(Welcome_to_GameInt,text="START",fg="white",bg="green",border=0).place(x=250,y=120,height=35,width=200)
    Label(Welcome_to_GameInt,text="OR",bg='white').place(x=335,y=155)
    Button(Welcome_to_GameInt,text="END",fg="white",bg="green",border=0).place(x=250,y=175,height=35,width=200)

    Label(Welcome_to_GameInt,text="Number to Guess-X X X X",bg='white',font=('Times New Roman',16,)).place(x=40,y=218)
    Label(Welcome_to_GameInt,text="Colour Mapping:",bg='white',font=('Times New Roman',14,)).place(x=550,y=218)
    Label(Welcome_to_GameInt,text="1-White 2-Blue 3-Red",bg='white',font=('Times New Roman',12,)).place(x=550,y=242)      
    Label(Welcome_to_GameInt,text="4-Yellow 5-Green 6-Purple",bg='white',font=('Times New Roman',12,)).place(x=550,y=262)
    Label(Welcome_to_GameInt,text="Attempt No",bg='white',font=('Times New Roman',14,'underline')).place(x=40,y=280)
    Label(Welcome_to_GameInt,text="Guess",bg='white',font=('Times New Roman',14,'underline')).place(x=280,y=280)
    Label(Welcome_to_GameInt,text="Result",bg='white',font=('Times New Roman',14,'underline')).place(x=450,y=280)
    
    Label(Welcome_to_GameInt,text="1",bg='white',font=('Times New Roman',12,)).place(x=40,y=320)
    Label(Welcome_to_GameInt,text="2 4 5 3",bg='white',font=('Times New Roman',12,)).place(x=280,y=320)
    Label(Welcome_to_GameInt,text="1 1",bg='white',font=('Times New Roman',12,)).place(x=450,y=320)
    Label(Welcome_to_GameInt,text=". .",bg='white',font=('Times New Roman',12,)).place(x=450,y=340)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=360,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="2",bg='white',font=('Times New Roman',12,)).place(x=40,y=370)
    Label(Welcome_to_GameInt,text="2 5 6 1",bg='white',font=('Times New Roman',12,)).place(x=280,y=370)
    Label(Welcome_to_GameInt,text="1 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=370)
    Label(Welcome_to_GameInt,text="0 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=390)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=410,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="3",bg='white',font=('Times New Roman',12,)).place(x=40,y=420)
    Label(Welcome_to_GameInt,text="2 6 1 1",bg='white',font=('Times New Roman',12,)).place(x=280,y=420)
    Label(Welcome_to_GameInt,text="1 1",bg='white',font=('Times New Roman',12,)).place(x=450,y=420)
    Label(Welcome_to_GameInt,text="1 1",bg='white',font=('Times New Roman',12,)).place(x=450,y=440)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=465,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="4",bg='white',font=('Times New Roman',12,)).place(x=40,y=470)
    Label(Welcome_to_GameInt,text="2 3 4 1",bg='white',font=('Times New Roman',12,)).place(x=280,y=470)
    Label(Welcome_to_GameInt,text="1 .",bg='white',font=('Times New Roman',12,)).place(x=450,y=470) 
    Label(Welcome_to_GameInt,text=". 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=490)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=510,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="5",bg='white',font=('Times New Roman',12,)).place(x=40,y=520)
    Label(Welcome_to_GameInt,text="1 5 4 1",bg='white',font=('Times New Roman',12,)).place(x=280,y=520)
    Label(Welcome_to_GameInt,text="0 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=520)
    Label(Welcome_to_GameInt,text="1 1",bg='white',font=('Times New Roman',12,)).place(x=450,y=540)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=560,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="6",bg='white',font=('Times New Roman',12,)).place(x=40,y=570)
    Label(Welcome_to_GameInt,text="4 3 3 6",bg='white',font=('Times New Roman',12,)).place(x=280,y=570)
    Label(Welcome_to_GameInt,text="1 .",bg='white',font=('Times New Roman',12,)).place(x=450,y=570)
    Label(Welcome_to_GameInt,text="0 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=590)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=610,height=2,width=470)
    
    Label(Welcome_to_GameInt,text="7",bg='white',font=('Times New Roman',12,)).place(x=40,y=620)
    Label(Welcome_to_GameInt,text="5 1 2 2",bg='white',font=('Times New Roman',12,)).place(x=280,y=620)
    Label(Welcome_to_GameInt,text="0 .",bg='white',font=('Times New Roman',12,)).place(x=450,y=620)
    Label(Welcome_to_GameInt,text="0 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=640)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=40,y=660,height=2,width=470)

    Label(Welcome_to_GameInt,text="8",bg='white',font=('Times New Roman',12,)).place(x=40,y=670)
    Label(Welcome_to_GameInt,text="4 4 5 3",bg='white',font=('Times New Roman',12,)).place(x=280,y=670)
    Label(Welcome_to_GameInt,text="0 1",bg='white',font=('Times New Roman',12,)).place(x=450,y=670)
    Label(Welcome_to_GameInt,text="1 0",bg='white',font=('Times New Roman',12,)).place(x=450,y=690)
    
    
    Label(Welcome_to_GameInt,text="Congratulations!!! You have won the Game",bg='white',font=('Times New Roman',12,)).place(x=40,y=710)
    Label(Welcome_to_GameInt,text="You have scored XXX points",bg='white',font=('Times New Roman',12,)).place(x=40,y=730)
    Label(Welcome_to_GameInt,text="Do you want to play again (Yes/No)",bg='white',font=('Times New Roman',12,)).place(x=40,y=750)

    Label(Welcome_to_GameInt,bg="black",border=0).place(x=10,y=10,height=2,width=730)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=740,y=10,height=770,width=2)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=10,y=10,height=770,width=2)
    Label(Welcome_to_GameInt,bg="black",border=0).place(x=10,y=780,height=2,width=732)
    
    
     
Welcome_to_GameInt()
APP.mainloop()


