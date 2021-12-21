from Mapping_for_Tkinter import Mapping_for_Tkinter
from Ball import Ball
from Racket import Racket
from tkinter import *
import math
import time
import random

#imported all the files and functions needed

def main():

        ###### create a mapping
        swidth=input("Enter window size in pixels (press Enter for default 600): ")
        if swidth=="":
            width=600   #default value
        else:
            width=int(swidth)

        Lx=width/10   #sets variable Lx equal to variable width/10
        Ly=width/60   #sets variable Ly equal to variable width/60
        R=width/120   #sets variable R equal to variable width/120

        
        mapping=Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)   #creates mapping
        rectangle1=mapping.get_ymin()   #sets rectangle1 to ymin

        ##### User Input 
        data=input("Enter velocity and theta (press Enter for default: 200 pixel/s and 53 degree):")
        if data=="":
            velocity=200   #default value of velocity
            angle=53*math.pi/180   #default angle
        else:
            velocity,angle=data.split()   #splits the input into two variables 
            velocity=float(velocity)  #turns input into float
            angle=float(angle)   #turns input into float 
            angle=angle*(math.pi/180)   #degrees to radians 

            
        ##### create a window, canvas, and racket
        window = Tk() 
        canvas = Canvas(window,width=mapping.get_width(),height=mapping.get_height(),bg="white") # create a canvas width*height
        canvas.pack()

        myracket=Racket(mapping,canvas,Lx,Ly,rectangle1)   #creates racket 
        
        y_initial=mapping.get_ymin()+Ly+R   #sets y value of ball
        ball1=Ball(mapping,canvas,0,y_initial,velocity,angle)   #creates ball

        ####### bind mouse click with action
        
        canvas.bind("<Button-1>",lambda e:myracket.shift_left())  #binds keys to shifting left
        canvas.bind("<Button-2>",lambda e:myracket.shift_right())   #binds keys to shifting right 
    
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time 
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t,myracket.Ly)# Update ball position and return collision event
            window.update()
            if side!=0:
                t=0
            if side==4:   #bottom of canvas
                if ball1.x<=myracket.x+(myracket.Lx/2) and ball1.x>=myracket.x-(myracket.Lx/2):  #if it is range of the racket 
                    continue
                else:
                    print("Game over. Total time",t_total)   #if not in range breaks and returns time played 
                    break
            elif side==3:   #top of canvas 
                ball1.velocity=ball1.velocity*1.25   #increases velocity 
                ball1.angle=random.uniform(-170,-10)   #gives a random angle 
            time.sleep(0.01)
        window.mainloop() # wait until the window is closed

if __name__=="__main__":
    main()



