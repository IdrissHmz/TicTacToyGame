from tkinter import Tk, Menu, filedialog, messagebox, LabelFrame, RIDGE, \
Frame, Entry, W, END, Button, E, Label, Listbox, Scrollbar, \
RIGHT, Y, X, BOTTOM, LEFT,IntVar
from tkinter import ttk
from tkinter import messagebox
from random import randint

player = 1
p1=[]
p2=[]

root0= Tk()
root0.title("Tic Tac Toy :Player 1")
style=ttk.Style()
style.theme_use('classic')
root=ttk.Frame(root0)
root.config(height=310,width=310)
root.grid(row="0")

def ButtonClicked(id):
    global player
    global computer
    print(computer.get())
    if(player==1):
        p1.append(id)
        SetSymbole(id,'X')
        Judge(p1) 
        player=2
        if(computer.get()==1):
            automatic()
        
    else:
        p2.append(id)
        SetSymbole(id,'O')
        Judge(p2)  
        player=1    
      
    root0.title("Tic Tac Toy :Player {}".format(player))
    

def Judge(p):
    win=False
    if((1 in p)and(2 in p) and(3 in p)): 
        win=True 
    if((1 in p)and(4 in p) and(7 in p)): 
        win=True 
    if((3 in p)and(6 in p) and(9 in p)): 
        win=True 
    if((7 in p)and(8 in p) and(9 in p)): 
        win=True 
    if((1 in p)and(5 in p) and(9 in p)): 
        win=True 
    if((3 in p)and(5 in p) and(7 in p)):  
        win=True        
    if((4 in p)and(5 in p) and(6 in p)): 
        win=True  
    if((2 in p)and(5 in p) and(8 in p)): 
        win=True
    if(win==True):
         messagebox.showinfo(title="CONGRATULATION",message="player {} wins".format(player))
         bu1.state(['disabled'])
         bu2.state(['disabled'])
         bu3.state(['disabled'])
         bu4.state(['disabled'])
         bu5.state(['disabled'])
         bu6.state(['disabled'])
         bu7.state(['disabled'])
         bu8.state(['disabled'])
         bu9.state(['disabled'])
         

def automatic():
    global p1
    global p2
    global player
    emptycells=[]
    for i in range(9):
        if (((i+1 not in p1)and(i+1 not in p2))):
            emptycells.append(i+1)   
    random=randint(0,len(emptycells)-1)
    ButtonClicked(emptycells[random])


       


def SetSymbole(id,symbole):
    if(id==1):
        bu1.config(text='{}'.format(symbole))
        bu1.state(['disabled'])
    elif(id==2):
        bu2.config(text='{}'.format(symbole))
        bu2.state(['disabled'])    
    elif(id==3):
        bu3.config(text='{}'.format(symbole))
        bu3.state(['disabled'])    
    elif(id==4):
        bu4.config(text='{}'.format(symbole))
        bu4.state(['disabled'])
    elif(id==5):
        bu5.config(text='{}'.format(symbole))
        bu5.state(['disabled'])
    elif(id==6):
        bu6.config(text='{}'.format(symbole))
        bu6.state(['disabled'])
    elif(id==7):
        bu7.config(text='{}'.format(symbole))
        bu7.state(['disabled'])
    elif(id==8):
        bu8.config(text='{}'.format(symbole))
        bu8.state(['disabled'])
    else:
        bu9.config(text='{}'.format(symbole))
        bu9.state(['disabled'])







#Adding buttons
bu1=ttk.Button(root,text='')
bu1.config(command=lambda: ButtonClicked(1))
bu1.grid(row="0",column="0",sticky='snew',ipadx=30,ipady=30)

bu2=ttk.Button(root,text='')
bu2.config(command=lambda: ButtonClicked(2))
bu2.grid(row="0",column="1",sticky='snew',ipadx=30,ipady=30)


bu3=ttk.Button(root,text='')
bu3.config(command=lambda: ButtonClicked(3))
bu3.grid(row="0",column="2",sticky='snew',ipadx=30,ipady=30)

bu4=ttk.Button(root,text='')
bu4.config(command=lambda: ButtonClicked(4))
bu4.grid(row="1",column="0",sticky='snew',ipadx=30,ipady=30)

bu5=ttk.Button(root,text='')
bu5.config(command=lambda: ButtonClicked(5))
bu5.grid(row="1",column="1",sticky='snew',ipadx=30,ipady=30)

bu6=ttk.Button(root,text='')
bu6.config(command=lambda: ButtonClicked(6))
bu6.grid(row="1",column="2",sticky='snew',ipadx=30,ipady=30)

bu7=ttk.Button(root,text='')
bu7.config(command=lambda: ButtonClicked(7))
bu7.grid(row="2",column="0",sticky='snew',ipadx=30,ipady=30)

bu8=ttk.Button(root,text='')
bu8.config(command=lambda: ButtonClicked(8))
bu8.grid(row="2",column="1",sticky='snew',ipadx=30,ipady=30)

bu9=ttk.Button(root,text='')
bu9.config(command=lambda: ButtonClicked(9))
bu9.grid(row="2",column="2",sticky='snew',ipadx=30,ipady=30)

computer = IntVar()
computer.set(0)

cp=ttk.Checkbutton(root0,text="Do you want to play against the computer ?")
cp.config(variable=computer)
cp.grid(row="1")




root0.mainloop()