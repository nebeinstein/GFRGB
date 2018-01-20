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

xEntry = ttk.Entry(maineframe, textvariable=xVar).grid(column=1, row=1)
yEntry = ttk.Entry(maineframe, textvariable=yVar).grid(column=1, row=2)
radiusEntry = ttk.Entry(maineframe, textvariable=radiusVar).grid(column=3, row=1)
arcLengthEntry = ttk.Entry(maineframe, textvariable=arcLenVar).grid(column=3, row=2)
arcPhaseEntry = ttk.Entry(maineframe, textvariable=arcPhaseVar).grid(column=5, row=2)
nextButt = ttk.Button(maineframe, text='Next').grid(column=7, row=2)
imageLabel = ttk.Label(maineframe, image=screamjov).grid(row=0, column=0, columnspan=8)

ttk.Label(maineframe, text='X:').grid(column=0, row=1)
ttk.Label(maineframe, text='Y:').grid(column=0, row=2)
ttk.Label(maineframe, text='Radius:').grid(column=2, row=1)
ttk.Label(maineframe, text='Arc Length:').grid(column=2, row=2)
ttk.Label(maineframe, text='Arc Phase:').grid(column=4, row=2)

for child in maineframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)

root.mainloop()