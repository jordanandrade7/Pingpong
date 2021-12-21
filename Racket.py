from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *

class Racket:
    def __init__(self,mapping=None,canvas=None,Lx=None,Ly=None, rectangle1=None):   #make the attributes of class rectangle
        self.mapping=mapping
        self.canvas=canvas
        self.Lx=Lx
        self.Ly=Ly
        self.x=0
        self.y=float(rectangle1+self.Ly/2)
        self.rect=self.canvas.create_rectangle(self.mapping.get_i(-self.Lx/2),self.mapping.get_j(self.y-self.Ly/2),self.mapping.get_i(self.Lx/2),self.mapping.get_j(self.y+self.Ly/2),fill="black")
        
    def shift_left(self):   #allows the racket ot shift left 
        if self.x-(self.Lx/2)!=self.mapping.get_xmin():   #sets boundary
            self.canvas.move(self.rect,-(self.Lx/2),0)   #moves the racket -Lx/2
            self.x=self.x-self.Lx/2
            
        
    def shift_right(self):   #allows the racket to shift right
        if self.x+self.Lx<=self.mapping.get_xmax():   #sets boundary
            self.canvas.move(self.rect,self.Lx/2,0)   #moves the racket Lx/2
            self.x=self.x+self.Lx/2
            
    def color_black(self):   #changes the color of the racket to black 
        self.canvas.itemconfig(self.rect,fill="black")
    
    def color_red(self):   #changes the color of the racket to red 
        self.canvas.itemconfig(self.rect,fill="red") 

        
def main():

    ###### create a mapping
    swidth=input("Enter window size in pixels (press Enter for default 600): ")
    if swidth=="":   #if enter is entered 
        width=600
    else:
        width=int(swidth)

    Lx=width/10   #takes account of the variable width
    Ly=width/60   #takes account of the variable width
    mapping=Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)  #instantiate mapping
    rectangle1=mapping.get_ymin()  #set variable to ymin
        
    ##### create a window, canvas, and racket
    window = Tk() 
    canvas = Canvas(window,width=mapping.get_width(),height=mapping.get_height(),bg="white") # create a canvas width*height
    canvas.pack()

    myracket=Racket(mapping,canvas,Lx,Ly,rectangle1)   #create racket
    

    ####### bind mouse click with action
    
    canvas.bind("<Button-1>",lambda e:myracket.shift_left())  #binding keys for shift left
    canvas.bind("<Button-2>",lambda e:myracket.shift_right())   #binding keys for shift right 

    window.mainloop()
    
if __name__=="__main__":
    main()

