import os
import pygame
from tkinter import *  
from tkinter.filedialog import askdirectory
pygame.mixer.init()

root=Tk()
root.title('Music Player')
root.minsize(350,300)


listbox = Listbox(root)
listbox.pack(fill = BOTH)

list_songs= []
def choose_directory():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            list_songs.append(files)
choose_directory()


for items in list_songs:
    listbox.insert(0,items)

def play():
    global list_songs
    pygame.mixer.music.load(list_songs[0])
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

index = 0
def nextsong():
    global index
    index+=1
    pygame.mixer.music.load(list_songs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(list_songs[index])
    pygame.mixer.music.play()

def exitbutton():
    pygame.mixer.music.stop()
    root.destroy()



def volume(val):
    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)


playbutton= Button(root,text = 'Play',height = 2, width = 6, command = play)
playbutton.pack(side=LEFT)

pausebutton = Button(root,text = 'Pause',height = 2, width = 6,command = pause)
pausebutton.pack(side=LEFT)

unpausebutton = Button(root,text = 'Unpause',height = 2, width = 6,command = unpause)
unpausebutton.pack(side=LEFT)

prevbutton = Button(root,text = 'Previous',height = 2,  width = 6,command = prevsong)
prevbutton.pack(side = LEFT)

nextbutton = Button(root,text = 'Next',height = 2, width = 6,command = nextsong)
nextbutton.pack(side= LEFT)

exitbutton = Button(root,text = 'Exit',height = 2, width = 6,command = exitbutton)
exitbutton.pack(anchor = 'e',side = BOTTOM )


scale =  Scale(root,from_ = 0, to = 100, orient = HORIZONTAL, command= volume)
scale.set(27)
scale.pack()


root.mainloop()





























