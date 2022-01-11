# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 07:09:37 2021

@author: surya
"""

import numpy as np
from tkinter import *
import random
import math


canva = Tk()
canva.wm_title('Simulation')
canvas = Canvas(canva, width=700, height=500, bg='black')
canvas.grid(row=0, column=0)

G = 10**(-1)

objects = []

class Object:
    def __init__(self, m, x, y, V):
        self.mass = m                           #Mass
        self.R = (3*m/(4*math.pi))**(1/3)            #Radius
        self.P = np.array([x, y], dtype=float)  #Array of positions
        self.V = np.array(V, dtype=float)       #Array of velocities 
        
    def gravity(self, other, dt):
        
        r_vec = []
        if self == other:
            self.dV = np.array([0,0], dtype=float)
        else:
            dist = math.sqrt((self.P[0]-other.P[0])**2 + (self.P[1]-other.P[1])**2)
            r_vec = np.array([(other.P[0]-self.P[0]), (other.P[1]-self.P[1])])
            if dist == 0:
                self.dV = 0
            else:    
                F = (G*self.mass*other.mass/dist**2)*r_vec
                self.dV = dt*(F/self.mass)
                if dist < (self.R + other.R):    
                    self.dV = 2*(other.mass/self.mass)*other.V/10  # Collision change in velocity
                    other.V *= -1
                    #self.dV *= -0.5
            
            self.V += self.dV
            
            if self.P[0] <= self.R:
                self.V[0] *= -1
                self.P[0] += 1
            if self.P[0] >= (700 - self.R):
                self.V[0] *= -1
                self.P[0] -= 1
            if self.P[1] <= self.R:
                self.V[1] *= -1
                self.P[1] += 1
            if self.P[1] >= (500 - self.R):
                self.V[1] *= -1
                self.P[1] -= 1
                
if __name__ == "__main__":
    OBJECTS = 75
    
    for i in range(OBJECTS):
        objects.append(Object(random.randrange(10,500), random.randrange(50, 650), random.randrange(50, 450), [0, 0]))
        print(objects[i].mass)

    T = 0
    flag = True
    dt = 0.1
    
    while flag:
        canvas.delete('all')  
        
        for obj in objects:
            for others in objects:
                obj.gravity(others, dt)
            obj.P += obj.V*dt
            
            canvas.create_oval(obj.P[0]-obj.R, obj.P[1]-obj.R, obj.P[0]+obj.R, obj.P[1]+obj.R, fill='orange')
            
        canvas.update()
        
        T += dt
        if T > 100000:
            flag = False
       
    canva.destroy()     
    
                                                                                                        
    
