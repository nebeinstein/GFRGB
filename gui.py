from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import preproc as pp
import loader as ldr
import sys
class GFRGBGUI:
    def __init__(self, root):
        """ Create the window and define the grid weights.
            Populate the window.
        """
        
        self.root = root
        
        self.root.title("Radio-Memology App")
        
        self.root.option_add('*tearOff', False)
        
        self.maineframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.maineframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.maineframe.columnconfigure(0, weight=1)
        self.maineframe.columnconfigure(1, weight=1)
        self.maineframe.columnconfigure(2, weight=1)
        self.maineframe.columnconfigure(3, weight=1)
        self.maineframe.columnconfigure(4, weight=1)
        self.maineframe.columnconfigure(5, weight=1)
        self.maineframe.columnconfigure(6, weight=4)
        self.maineframe.columnconfigure(7, weight=1)
        self.maineframe.rowconfigure(0, weight=1)
        self.maineframe.rowconfigure(1, weight=1)
        self.maineframe.rowconfigure(2, weight=1)
        
        #self.win = Toplevel(self.root)
        
        ttk.Label(self.maineframe, text='X:').grid(column=1, row=1)
        ttk.Label(self.maineframe, text='Y:').grid(column=1, row=2)
        ttk.Label(self.maineframe, text='Radius:').grid(column=3, row=1)
        ttk.Label(self.maineframe, text='Arc Length:').grid(column=3, row=2)
        ttk.Label(self.maineframe, text='Arc Phase:').grid(column=5, row=2)
        
        self.populateWidgets()
        self.makeReticle()
        self.setCallbacks()
        
        for child in self.maineframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
    def makeReticle(self):
        """ toss the reticle onto the image right there in the middle"""
        self.horzLine = self.imageCanvas.create_line(340,350,360,350, fill='red')
        self.vertLine = self.imageCanvas.create_line(350,360,350,340, fill='red')
        self.reticleArc = self.imageCanvas.create_arc(330,330, 370,370, outline='red', style='arc')
        
    def populateWidgets(self):
        """ Create and add the widgets to the window. """
        self.scream = Image.open('.\\ordo hereticus seal.jpg')
        self.screamjov = ImageTk.PhotoImage(self.scream)
        
        self.xVar = IntVar()
        self.yVar = IntVar()
        self.radiusVar = IntVar()
        self.arcLenVar = IntVar()
        self.arcPhaseVar = IntVar()
        
        self.xEntry = ttk.Entry(self.maineframe, textvariable=self.xVar)
        self.yEntry = ttk.Entry(self.maineframe, textvariable=self.yVar)
        self.radiusEntry = ttk.Entry(self.maineframe, textvariable=self.radiusVar)
        self.arcLengthEntry = ttk.Entry(self.maineframe, textvariable=self.arcLenVar)
        self.arcPhaseEntry = ttk.Entry(self.maineframe, textvariable=self.arcPhaseVar)
        self.nextButt = ttk.Button(self.maineframe, text='Next')
        self.imageCanvas = Canvas(self.maineframe, width=700, height=700)
        self.image = self.imageCanvas.create_image((350,350), image=self.screamjov)   
        self.fileListBox = Listbox(self.maineframe)  
        self.menuBar = Menu(self.root) 
        self.fileMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(menu=self.fileMenu, label='File')
        
        self.xEntry.grid(column=2, row=1)
        self.yEntry.grid(column=2, row=2)
        self.radiusEntry.grid(column=4, row=1)
        self.arcLengthEntry.grid(column=4, row=2)
        self.arcPhaseEntry.grid(column=6, row=2)
        self.nextButt.grid(column=8, row=2)
        self.imageCanvas.grid(column=1, row=0, columnspan=8) 
        self.fileListBox.grid(column=0, row=0, rowspan=3, sticky=(N, W, S, E))
        self.fileMenu.add_command(label='Open', command=self.menu_item_open)
        self.fileMenu.add_command(label='Save')
        self.fileMenu.add_command(label='Quit')
        
        self.root.config(menu=self.menuBar)
        
    def updateFileList(self, newList):
        """ Replace the current list of files with a new list. """
        self.fileListBox.delete(0, END)
        for item in newList:
            self.fileListBox.insert(END, item)
    
    def updateOnClick(self, a):
        """ Update the position of the reticle on a click on the image. """
        r = int(self.radiusEntry.get())
        theta = int(self.arcLengthEntry.get())
        psi = int(self.arcPhaseEntry.get())
        self.imageCanvas.coords(self.horzLine, a.x-10, a.y, a.x+10, a.y)
        self.imageCanvas.coords(self.vertLine, a.x, a.y-10, a.x, a.y+10)
        self.imageCanvas.coords(self.reticleArc, a.x-r, a.y-r, a.x+r, a.y+r)
        self.imageCanvas.itemconfigure(self.reticleArc, start=psi, extent=theta)
        self.xEntry.delete(0, END)
        self.yEntry.delete(0, END)
        self.xEntry.insert(0, str(a.x - (700 - self.scream.width)/2))
        self.yEntry.insert(0, str(-1*(a.y - (700 - self.scream.height/2))))
            
    def updateOnReturn(self, a):
        """ update the reticle's location when you hit return on the coordinate inputs """
        x = float(self.xEntry.get())
        y = -1*float(self.yEntry.get())
        x = x + (700 - self.scream.width)/2
        y = y + (700 + self.scream.height)/2
        self.imageCanvas.coords(self.horzLine, x-10, y, x+10, y)
        self.imageCanvas.coords(self.vertLine, x, y+10, x, y-10)
        pass
    
    def run(self):
        """ make it go"""
        self.root.mainloop()

    def menu_item_open(self):
        """Loads in all the files in the given directory."""
        filepath = filedialog.askdirectory()
        if(filepath==''):
            return
        the_list_of_files = ldr.get_files_in(filepath)
        self.updateFileList(the_list_of_files)

    def menu_item_exit(self):
        """Exits the program"""
        sys.exit(0)

    def setCallbacks(self):
        """ Set callbacks in the object. """
        self.imageCanvas.bind('<Button-1>', lambda x: self.updateOnClick(x))
        self.xEntry.bind('<Return>', lambda x: self.updateOnReturn(x))
        self.yEntry.bind('<Return>', lambda x: self.updateOnReturn(x))
        self.radiusEntry.bind('<Return>', lambda x: self.updateOnClick(x))


        
if __name__ == "__main__":
    
    gui = GFRGBGUI(Tk())
    gui.run()