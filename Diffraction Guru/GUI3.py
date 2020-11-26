from tkinter import *
from Monte_Carlo_Fresnel import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

pat = []

def pl():
    fig = Figure(figsize=(5, 5), dpi=100)
    #fig, ax = plt.subplots(1,1)
    #ax.contourf(pattern(sxsize.get()*10**-6, sysize.get()*10**-6, sz.get(), sl.get()*10**-6))
    global pat
    pat = pattern(sxsize.get()*10**-6, sysize.get()*10**-6, sz.get(), sl.get()*10**-6)
    kstep = (sxsize.get()*10**-6 + sysize.get()*10**-6)/2
    k = 35 #Same k as used in random sampling part of Monte_Carlo_Frensel.pattern()
    fig.add_subplot(111).contourf(np.linspace(-k*0.5*kstep, k*0.5*kstep, k), np.linspace(-k*0.5*kstep, k*0.5*kstep, k), pat, cmap = cm.plasma)
    canvas = FigureCanvasTkAgg(fig, master = master)   
    canvas.draw() 
    canvas.get_tk_widget().place(x=800, y=100)

def open():
    top=Tk()
    top.title("About the app")
    label=Label(top, text="Hello and welcome to diffraction guru!!\n\n\nThis app helps one understand the concept of diffraction through a real time graph \nwhich plots the pattern of diffraction depending upon the values that the user enters.\n\n\nWe will take various inputs from the user such as the wavelength and the slit distance and suchand then plot the diffraction pattern that would have been obtained on the screen\n\nWe hope this app is found to be helpful to students in understanding diffraction better.\n\n\n\n\n\n\nEnjoy using it!!", font=('arial', 10, 'italic'))
    label.grid(row=0, column=0)

def open2():
    top = Tk()
    top.geometry("900x500")
    top.title("Intensity on the Axes")
    fig2 = Figure(figsize = (3,3), dpi=100)
    fig3 = Figure(figsize = (3,3), dpi=100)
    xint = pat[18][0:len(pat[18])]
    yint = []
    k = 35
    kstep = (sxsize.get()*10**-6 + sysize.get()*10**-6)/2
    for i in range(k):
        yint += [pat[i][18]]
    maxy = 0
    for j in yint:
        if j > maxy:
            maxy = j
    fig2.add_subplot(111).plot(np.linspace(-k*0.5*kstep, k*0.5*kstep, k), yint)
    fig3.add_subplot(111).plot(np.linspace(-k*0.5*kstep, k*0.5*kstep, k), xint)
    canvas2 = FigureCanvasTkAgg(fig2, master = top)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=100, y=100)
    canvas3 = FigureCanvasTkAgg(fig3, master = top)
    canvas3.draw()
    canvas3.get_tk_widget().place(x=500, y=100)
    
    
  
    
master = Tk()
master.title('Diffraction Guru')
master.geometry("2000x2000")

frame=LabelFrame(master, text="For Diffraction Pattern\nClick here", padx=10, pady=10)
frame.place(x=60, y=400)

label1=Label(master, text="Diffraction Guru", font=('arial',30,'bold','italic'))
label1.place(x=500, y=0)

sxsize = Scale(master, label="x length(micro m)", from_=0, to=3000, orient='horizontal', length = 600)
sxsize.set(3)
sxsize.place(x = 10, y = 100)

sysize = Scale(master, label="y length(micro m)", from_=0, to=3000, orient='horizontal', length = 600)
sysize.set(3000)
sysize.place(x = 10, y = 160)

sz = Scale(master, label="Screen distance(m)", from_=0, to=10, orient='horizontal', length = 600)
sz.set(1)
sz.place(x = 10, y = 220)

sl = Scale(master, label="Wavelength", from_=0, to=3000, orient='horizontal', length = 600)
sl.set(6)
sl.place(x = 10, y = 280)

b = Button(frame, text = "PLOT", command=pl, fg="red", bg="yellow")
b.grid(row=300, column = 100)

btn = Button(master, text = "To know more about this app\nClick here", bg="lightblue",command=open)
btn.place(x=30, y=600)

inteframe = LabelFrame(master, text = "For Intensity Graphs along axes\nClick here", padx=10, pady=10)
inteframe.place(x = 200, y= 400)

intebtn = Button(inteframe, text = "PLOTS", command = open2 , fg = "red", bg = "yellow")
intebtn.grid(row = 300, column = 100)

master.mainloop()
