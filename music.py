from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
import os
from tkinter import *
root= Tk()

root.minsize(350,350)
root.configure(bg='black')
root.resizable(width=False,height=False)
listofsongs=[]
v = StringVar()
songlabel = Label(root,textvariable=v,width=50,bg='crimson',fg='white',font=('times new roman',10,'bold'))
index=0
def directorychooser():
    directory= 'C:\music'
    os.chdir("C:\music")
    for  files in os.listdir("C:\music"):
        if files.endswith(".mp3"):
            realdir= os.path.realpath(files)
            audio= ID3(realdir)
            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


directorychooser()


def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])



def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def inc(self):

    pygame.mixer.music.set_volume(value=1)


def dec(self):


    pygame.mixer.music.set_volume(value=1)

TopFrame= Frame(root, width=350, height=7,bd=1, relief="raise")
TopFrame.pack(side=TOP)

label= Label(TopFrame, text='Music Player',bg='black',fg='red',font=('times new roman',18,'bold'))
label.pack()

listbox=Listbox(root,relief=FLAT,bg="pink",font=('times new roman',12,'italic'))
listbox.pack(side="top", anchor="center")
listofsongs.reverse()
#realnames.reverse()
for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()
#realnames.reverse()

Nextbutton=Button(root,text='Next Song',width=4,bg='slateblue4',fg='white',relief=GROOVE,font=('times new roman',9,'bold'),padx=25)
Nextbutton.pack()
Nextbutton.place(x=80,y=263)

Previousbutton=Button(root,text='Previous Song',width=8,bg='slateblue4',fg='white',relief=GROOVE,font=('times new roman',9,'bold'),padx=15)
Previousbutton.pack()
Previousbutton.place(x=185,y=263)

Stopbutton=Button(root,text='Stop Song',width=4,bg='red3',fg='white',relief=GROOVE,font=('times new roman',9,'bold'),padx=25)
Stopbutton.pack()
Stopbutton.place(x=130,y=294)
volumeincbutton=Button(root,text='+',bg='steelblue4',fg='white',relief=GROOVE,font=(10))
volumeincbutton.pack()
volumeincbutton.place(x=270,y=50)
volumedecbutton=Button(root,text='-',bg='steelblue4',fg='white',relief=GROOVE,font=(10),padx=4)
volumedecbutton.pack()
volumedecbutton.place(x=270,y=100)

Nextbutton.bind("<Button-1>", nextsong)
Previousbutton.bind("<Button-1>", prevsong)
Stopbutton.bind("<Button-1>", stopsong)
volumeincbutton.bind("<Button-1>", inc)
volumedecbutton.bind("<Button-1>", dec)

songlabel.pack()

root.mainloop()


