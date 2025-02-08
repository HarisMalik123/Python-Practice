BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
root=Tk()
root.title("Flash Card Game ")

df=pd.read_csv("word.csv")
data=df.to_dict(orient="records")
current={}

def nextcard():
    global current,fliptimer
    root.after_cancel(fliptimer)
    current=random.choice(data)
    canvas.itemconfig(cardtitle,text="French",fill="black")
    canvas.itemconfig(cardword,text=current["French"],fill="black")
    canvas.itemconfig(cardbg,image=cardimg)
    fliptimer=root.after(3000,func=flipcard)
def flipcard():
    canvas.itemconfig(cardtitle,text="English",fill="white")
    canvas.itemconfig(cardword,text=current["English"],fill="white")
    canvas.itemconfig(cardbg,image=cardback)
def isknown():
    data.remove(current)
    data1=pd.DataFrame(data)
    data1.to_csv("word.csv",index=False)
    nextcard()
    
root.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
fliptimer=root.after(3000,func=flipcard)
canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
cardimg=PhotoImage(file="front.png")
cardback=PhotoImage(file="back.png")
cardbg=canvas.create_image(400,263,image=cardimg)
cardtitle=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
cardword=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
cross=PhotoImage(file="wrong.png")
crossbutton=Button(image=cross,command=nextcard)
crossbutton.grid(row=1,column=0)
ticki=PhotoImage(file="e.png")
tickbutton=Button(image=ticki,command=isknown)
tickbutton.grid(row=1,column=1)
nextcard()
root.mainloop()