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
def printData(a, b):
    print(horzLine)
    print(vertLine)
    x = int(xEntry.get())
    y = int(yEntry.get())
    imageCanvas.coords(horzLine, a.x-10, a.y, a.x+10, a.y)
    imageCanvas.coords(vertLine, a.x, a.y-10, a.x, a.y+10)
    print(b.winfo_width(), b.winfo_height())
    print(a.x)
    
def updateLocation(xEntry, yEntry):
    pass

imageCanvas.bind('<Button-1>', lambda x: printData(x, imageCanvas))
xEntry.bind('<Return>', lambda x: printData(x, xEntry))
yEntry.bind('<Return>', lambda x: printData(x, yEntry))
radiusEntry.bind('<Return>', lambda x: printData(x, radiusEntry))

root.mainloop()

pass