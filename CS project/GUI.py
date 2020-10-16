from tkinter import *
from Diffraction_Guru import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
  
def pl():
    fig = Figure(figsize=(4, 4), dpi=100)
    #fig, ax = plt.subplots(1,1)
    #ax.contourf(pattern(sxsize.get()*10**-6, sysize.get()*10**-6, sz.get(), sl.get()*10**-6))
    fig.add_subplot(111).contourf(pattern(sxsize.get()*10**-6, sysize.get()*10**-6, sz.get(), sl.get()*10**-6))
    canvas = FigureCanvasTkAgg(fig, master = master)   
    canvas.draw() 
    canvas.get_tk_widget().grid(row=500, column=10)
  
    
master = Tk()
master.title('Diffraction Guru')
sxsize = Scale(master, from_=0, to=3000, orient='horizontal', length = 500)
sxsize.set(3)
sxsize.grid(row = 0, column = 10)
sysize = Scale(master, from_=0, to=3000, orient='horizontal', length = 500)
sysize.set(3000)
sysize.grid(row = 100, column = 10)
sz = Scale(master, from_=0, to=10, orient='horizontal', length = 500)
sz.set(1)
sz.grid(row = 200, column = 10)
sl = Scale(master, from_=0, to=3000, orient='horizontal', length = 500)
sl.set(6)
sl.grid(row = 300, column = 10)
b = Button(master, text = "PLOT", command=pl)
b.grid(row = 400, column = 10)
master.mainloop()
