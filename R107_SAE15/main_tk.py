from PIL import ImageGrab

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("file path here")


from tkinter import *
window=Tk()
# add widgets here

window.geometry("1000x500")
window.savefig("hi.png")*

