from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time

class Ball:
    def __init__(self,mapping=None,canvas=None,x0=None,y0=None,velocity=None,angle=None):   #attributes for class ball
        self.mapping=mapping   #setting all self.variables to varible name
        self.canvas=canvas
        self.x0=x0
        self.y0=y0
        self.velocity=velocity
        self.angle=angle
        self.x=self.x0
        self.y=self.y0
        self.R=mapping.get_width()/120   #radius equal to variable width/120
        self.oval=self.canvas.create_oval(self.mapping.get_i(self.x-self.R),self.mapping.get_j(self.y+self.R),self.mapping.get_i(self.x+self.R),self.mapping.get_j(self.y-self.R),fill="blue")   #create ball coordinates

    def update_xy(self,t,rectangle=0):   #update the xy coordinates
        side=0   #initialize side
        self.x=self.x0+self.velocity*math.cos(self.angle)*t   #x coordinate of ball
        self.y=self.y0+(self.velocity*math.sin(self.angle))*t   #y coordinate of ball

        if self.y+self.R+rectangle>=self.mapping.get_ymax():   #top of canvas
            self.angle=-self.angle
            self.x0=self.x
            self.y0=self.mapping.get_ymax()-self.R-rectangle
            side=3
            
        elif self.y-self.R-rectangle<=self.mapping.get_ymin():   #bottom of canvas
            self.angle=-self.angle
            self.x0=self.x
            self.y0=self.mapping.get_ymin()+self.R+rectangle
            side=4
            
        elif self.x-self.R<=self.mapping.get_xmin():   #side of canvas
            self.angle=math.pi-self.angle
            self.x0=self.mapping.get_xmin()+self.R
            self.y0=self.y
            side=1
            
        elif self.x+self.R>=self.mapping.get_xmax():   #side of canvas
            self.angle=math.pi-self.angle
            self.x0=self.mapping.get_xmax()-self.R
            self.y0=self.y
            side=2
            
        self.canvas.coords(self.oval,self.mapping.get_i(self.x-self.R),self.mapping.get_j(self.y-self.R),self.mapping.get_i(self.x+self.R),self.mapping.get_j(self.y+self.R))   #moves the ball on the canvas

        return side   #returns int value of side 
        

def main(): 
        ##### create a mapping
        swidth=input("Enter window size in pixels (press Enter for default 600): ")
        if swidth=="":
            width=600   #default value
        else:
            width=int(swidth)

        mapping=Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)   #create mapping
        R=width/120   #radius is equal to variable width/120
        
        ##### User Input 
        data=input("Enter velocity and theta (press Enter for default: 500 pixel/s and 30 degree):")
        if not data:  #if enter is entered
            data= "500 30"
        
        velocity,angle=data.split()   #splits input into two variables
        velocity=float(velocity)   #turns into float
        angle=float(angle)   #turns into float 
        angle=angle*(math.pi/180)  #changes from degrees to radians 

        
        ##### create a window, canvas and ball object
        root = Tk() 
        canvas = Canvas(root,width=mapping.get_width(),height=mapping.get_height(),bg="white") # create a canvas width*height
        canvas.pack()

        ball1=Ball(mapping,canvas,0,0,velocity,angle)   #creates the ball
           
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t)# Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count==10: break # stop the simulation
            
        print("Game over! Total time: %ss"%t_total)
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

