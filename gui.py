from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
    
root = Tk()
root.title("Radio-Memology App")

maineframe = ttk.Frame(root, padding="3 3 12 12")
maineframe.grid(column=0, row=0, sticky=(N, W, E, S))
maineframe.columnconfigure(0, weight=1)
maineframe.columnconfigure(1, weight=1)
maineframe.columnconfigure(2, weight=1)
maineframe.columnconfigure(3, weight=1)
maineframe.columnconfigure(4, weight=1)
maineframe.columnconfigure(5, weight=1)
maineframe.columnconfigure(6, weight=4)
maineframe.columnconfigure(7, weight=1)
maineframe.rowconfigure(0, weight=1)
maineframe.rowconfigure(1, weight=1)
maineframe.rowconfigure(2, weight=1)

scream = Image.open('.\\ordo hereticus seal.jpg')
screamjov = ImageTk.PhotoImage(scream)

xVar = IntVar()
yVar = IntVar()
radiusVar = IntVar()
arcLenVar = IntVar()
arcPhaseVar = IntVar()

def updateCenter():
    pass

xEntry = ttk.Entry(maineframe, textvariable=xVar)
yEntry = ttk.Entry(maineframe, textvariable=yVar)
radiusEntry = ttk.Entry(maineframe, textvariable=radiusVar)
arcLengthEntry = ttk.Entry(maineframe, textvariable=arcLenVar)
arcPhaseEntry = ttk.Entry(maineframe, textvariable=arcPhaseVar)
nextButt = ttk.Button(maineframe, text='Next')
imageCanvas = Canvas(maineframe, width=700, height=700)
image = imageCanvas.create_image((350,350), image=screamjov)
horzLine = imageCanvas.create_line(340,350,360,350, fill='red')
vertLine = imageCanvas.create_line(350,360,350,340, fill='red')
reticleArc = imageCanvas.create_arc(330,330, 370,370, outline='red', style='arc')

xEntry.grid(column=1, row=1)
yEntry.grid(column=1, row=2)
radiusEntry.grid(column=3, row=1)
arcLengthEntry.grid(column=3, row=2)
arcPhaseEntry.grid(column=5, row=2)
nextButt.grid(column=7, row=2)
imageCanvas.grid(row=0, column=0, columnspan=8)

ttk.Label(maineframe, text='X:').grid(column=0, row=1)
ttk.Label(maineframe, text='Y:').grid(column=0, row=2)
ttk.Label(maineframe, text='Radius:').grid(column=2, row=1)
ttk.Label(maineframe, text='Arc Length:').grid(column=2, row=2)
ttk.Label(maineframe, text='Arc Phase:').grid(column=4, row=2)

for child in maineframe.winfo_children(): child.grid_configure(padx=5, pady=5)
print('xy', imageCanvas.winfo_width(), imageCanvas.winfo_height())
def updateOnClick(a):
    r = int(radiusEntry.get())
    theta = int(arcLengthEntry.get())
    psi = int(arcPhaseEntry.get())
    imageCanvas.coords(horzLine, a.x-10, a.y, a.x+10, a.y)
    imageCanvas.coords(vertLine, a.x, a.y-10, a.x, a.y+10)
    imageCanvas.coords(reticleArc, a.x-r, a.y-r, a.x+r, a.y+r)
    imageCanvas.itemconfigure(reticleArc, start=psi, extent=theta)
    xEntry.delete(0, END)
    yEntry.delete(0, END)
    xEntry.insert(0, str(a.x - (700 - scream.width)/2))
    yEntry.insert(0, str(-1*(a.y - (700 - scream.height/2))))
    
def updateOnReturn(a):
    x = int(xEntry.get())
    y = -1*int(yEntry.get())
    x = x + (700 - scream.width)/2
    y = y + (700 + scream.height)/2
    imageCanvas.coords(horzLine, x-10, y, x+10, y)
    imageCanvas.coords(vertLine, x, y+10, x, y-10)
    pass

imageCanvas.bind('<Button-1>', lambda x: updateOnClick(x))
xEntry.bind('<Return>', lambda x: updateOnReturn(x))
yEntry.bind('<Return>', lambda x: updateOnReturn(x))
radiusEntry.bind('<Return>', lambda x: updateOnClick(x))

root.mainloop()

pass