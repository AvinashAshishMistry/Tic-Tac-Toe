from tkinter import*
import tkinter as tk
import random

row_clounm = [[0,0,0],[0,0,0],[0,0,0]]
starting_player = random.choice(['X','O'])
click_remains = 9;


def start_game():
     global starting_player,row_clounm,click_remains,buttons
     starting_player = random.choice(['X','O'])
     row_clounm = [[0,0,0],[0,0,0],[0,0,0]]
     click_remains = 9;
     l1.config(text="Tic Tak Toe Game # Python",fg="white",bg="black")
     l.config(text="Player "+ starting_player + "'s turn")
     start.config(state= "disabled")
     for wiget in buttons:
         for buttonss in wiget:
             buttonss.config(text="  ",state= "active",bg="white")
 

def check_result(row,coloum,button_n):
     global buttons
     left_col = coloum - 1;
     right_col = coloum + 1;
     up_row = row - 1;
     down_row = row + 1;
     answer = False;

     if(left_col < 0 ):left_col = 2;
     if(right_col > 2 ):right_col = 0;
     if(up_row < 0 ):up_row = 2;
     if(down_row > 2 ):down_row = 0;

     if(row_clounm[row][coloum] == row_clounm[row][left_col] == row_clounm[row][right_col]):
         answer = "row"
     elif (row_clounm[row][coloum] == row_clounm[up_row][coloum] == row_clounm[down_row][coloum]):
         answer = "colounm"
     elif (button_n == c or button_n == g):
         if(row_clounm[row][coloum] == row_clounm[down_row][left_col] == row_clounm[up_row][right_col]):
             answer = "r_dia"
     elif (button_n == a or button_n == e or button_n == i):
         if(row_clounm[row][coloum] == row_clounm[left_col][up_row] == row_clounm[right_col][down_row]):
             answer = "l_dia"
     
     if(answer != False):
         buttons[row][coloum].config(bg="red")
         if(answer == "row"):
             buttons[row][left_col].config(bg="red")
             buttons[row][right_col].config(bg="red")             
         elif(answer == "colounm"):
             buttons[up_row][coloum].config(bg="red")
             buttons[down_row][coloum].config(bg="red")
         elif(answer == "r_dia"):
             buttons[down_row][left_col].config(bg="red")
             buttons[up_row][right_col].config(bg="red")
         elif(answer == "l_dia"):
             buttons[left_col][up_row].config(bg="red")
             buttons[right_col][down_row].config(bg="red")
             
     return answer      

def click(row,colounm,button_n):
     global starting_player,row_clounm,click_remains,buttons

     if(starting_player == "X"):
         row_clounm[row][colounm] = -1;
     elif(starting_player == "O"):
         row_clounm[row][colounm] = 1;

     button_n.config(text = starting_player,fg = "black",state= "disabled")
     answer = check_result(row,colounm,button_n)

     if(answer != False):
         l1.config(text="!!! GAME OVER !!!",bg="red")
         l.config(text="player \"" + starting_player + "\" wins")

         for widget in buttons:
             for buttonss in widget:
                 buttonss.config(state= "disabled")

         start.config(text="RESTART",state="active")
         return
     
     if(starting_player == "X"):starting_player = "O";
     else:starting_player = "X"

     l.config(text="Player "+ starting_player + "'s turn")
    
     click_remains = click_remains - 1;
     if(click_remains == 0):
         l1.config(text="!!! MATCH DRAW !!!",bg="red")
         l.config(text="match tie between player \"X\" and \"O\"")
         start.config(text="RESTART",state="active")

root=Tk()

root.minsize(500,500)
root.geometry("500x500")
root.title("Tic Tak Toe game")
root.config(bg="black")

l1=Label (root,text="Tik Tak Game # Python",fg="white",bg="black",font=("Georgia ",16,"bold"))
l1.pack(padx=5,pady=5,side=TOP)
l=Label(root,text="",fg="white",bg="black",font=("Georgia ",16,"bold"))
l.pack(fill=X,padx=5,pady=5,side=TOP)
f1=Frame(root,bg="black")
a=tk.Button(f1,padx=25,pady=25,text="  ",bg="white",fg="white",state= "disabled",font=("Georgia ",15,"bold"),command=lambda :click(0,0,a))
a.pack(side=LEFT,padx=8)
b=tk.Button(f1,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(0,1,b))
b.pack(side=LEFT,padx=8)
c=tk.Button(f1,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(0,2,c))
c.pack(side=LEFT,padx=8)
f1.pack(padx=5,pady=8)

f2=Frame(root,bg="black")
d=tk.Button(f2,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(1,0,d))
d.pack(side=LEFT,padx=8)
e=tk.Button(f2,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(1,1,e))
e.pack(side=LEFT,padx=8)
f=tk.Button(f2,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(1,2,f))
f.pack(side=LEFT,padx=8)
f2.pack(padx=5,pady=8)

f3=Frame(root,bg="black")
g=tk.Button(f3,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(2,0,g))
g.pack(side=LEFT,padx=8)
h=tk.Button(f3,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(2,1,h))
h.pack(side=LEFT,padx=8)
i=tk.Button(f3,padx=25,pady=25,text="  ",state= "disabled",bg="white",fg="white",font=("Georgia ",15,"bold"),command=lambda:click(2,2,i))
i.pack(side=LEFT,padx=8)
f3.pack(padx=5,pady=8)

f4=Frame(root,bg="black")
start=Button(f4,text="START",padx=10,pady=5,bg="white",fg="black",font=("Georgia ",15,"bold"),command=lambda:start_game())
start.pack(side=TOP,pady=25)
f4.pack()

buttons = [[a,b,c],[d,e,f],[g,h,i]]
root.mainloop()