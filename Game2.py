from Mapping_for_Tkinter import Mapping_for_Tkinter
from Ball import Ball
from Racket import Racket
from tkinter import *
import math
import time
import random

#imports all files and functions needed

def main():

        ###### create a mapping
        swidth=input("Enter window size in pixels (press Enter for default 600): ")
        if swidth=="":
            width=600   #default value 
        else:
            width=int(swidth)

        Lx=width/10   #variable Lx is equal to variable width/10
        Ly=width/60   #variable Ly is equal to variable width/60
        R=width/120   #variable Radius is equal to variable width/120
        
        mapping=Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)   #create mapping
        rectangle1=mapping.get_ymin()   #assigns rectangle 1 to ymin
        rectangle2=mapping.get_ymax()-Ly   #assigns rectangle 2 to ymax-Ly

        ##### User Input 
        data=input("Enter velocity and theta (press Enter for default: 200 pixel/s and 53 degree):")
        if data=="":
            velocity=300   #default value
            angle=45*math.pi/180   #default value
        else:
            velocity,angle=data.split()   #splits input into two variables
            velocity=float(velocity)   #turns into float 
            angle=float(angle)   #turns into float 
            angle=angle*(math.pi/180)   #turns degrees in to radians 

            
        ##### create a window, canvas, and racket
        window = Tk() 
        canvas = Canvas(window,width=mapping.get_width(),height=mapping.get_height(),bg="white") # create a canvas width*height
        canvas.pack()

        myracket=Racket(mapping,canvas,Lx,Ly,rectangle1)   #creates racket1
        
        myracket2=Racket(mapping,canvas,Lx,Ly,rectangle2)   #creates racket2
        
        y_initial=mapping.get_ymin()+Ly+R   #assings y value to ymin+Ly+radius 
        ball1=Ball(mapping,canvas,0,y_initial,velocity,angle)   #creates ball

        ####### bind mouse click with action
        myracket2.color_red()   #intializes racket two as red 
        canvas.bind("<Button-1>",lambda e:myracket2.shift_left())   #binds keys to racket2
        canvas.bind("<Button-2>",lambda e:myracket2.shift_right())   #binds keys to racket2

        ############################################
        ####### start simulation
        ############################################

        #####im not sure why my while loop isnt working,runs but doesnt abide by the if and elif statements###
        
        t=0               # real time between event
        t_total=0         # real total time 
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t,myracket.Ly)# Update ball position and return collision event
            window.update()
            if side!=0:
                t=0   #reinitialize time
            elif side==4:   #bottom of canvas
                if ball1.x<=myracket.x+(myracket.Lx/2) and ball1.x>=myracket.x-(myracket.Lx/2):   #if ball hits racket one
                    ball1.angle=random.uniform(10,170)   #random angle
                    myracket2.color_red()   #turns racket two to red
                    myracket.color_black()   #turns racket one to black 
                    canvas.bind("<Button-1>",lambda e:myracket2.shift_left())   #binds keys to racket two for shifting left 
                    canvas.bind("<Button-2>",lambda e:myracket2.shift_right())   #binds keys to racket two for shifting right 
                else:
                    print("Game over for racket 1. Total time",t_total)  #if not game breaks 
                    break
            elif side==3:   #top of canvas 
                if ball1.x<=myracket2.x+(myracket.Lx/2) and ball1.x>=myracket2.x-(myracket2.Lx/2):   #if ball hits racket two 
                    ball1.angle=random.uniform(-170,-10)   #gives random angle 
                    myracket.color_red()   #changes racket one to red 
                    myracket2.color_black()   #changes racket two to black 
                    canvas.bind("<Button-1>",lambda e:myracket.shift_left())   #binds keys to racket one to shifting left 
                    canvas.bind("<Button-2>",lambda e:myracket.shift_right())   #binds keys to racket one to shifting right 
                else:
                    print("Game over for racket 2. Total time",t_total)  #if not game breaks 

                
            time.sleep(0.01)
        window.mainloop() # wait until the window is closed

if __name__=="__main__":
    main()

