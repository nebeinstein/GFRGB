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
        
        self.root.title("Gluten Free (tm) Radioactive Green Beans - Radio-Memology App")
        
        self.root.option_add('*tearOff', False)
        
        self.maine_frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.maine_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.maine_frame.columnconfigure(0, weight=1, minsize=120)
        self.maine_frame.columnconfigure(1, weight=1, minsize=30)
        self.maine_frame.columnconfigure(2, weight=1, minsize=120)
        self.maine_frame.columnconfigure(3, weight=1, minsize=30)
        self.maine_frame.columnconfigure(4, weight=1, minsize=120)
        self.maine_frame.columnconfigure(5, weight=1, minsize=30)
        self.maine_frame.columnconfigure(6, weight=1, minsize=120)
        self.maine_frame.columnconfigure(7, weight=1, minsize=180)
        self.maine_frame.columnconfigure(8, weight=1, minsize=120)
        self.maine_frame.rowconfigure(0, weight=1)
        self.maine_frame.rowconfigure(1, weight=1)
        self.maine_frame.rowconfigure(2, weight=1)
        
        #self.win = Toplevel(self.root)
        
        ttk.Label(self.maine_frame, text='X:').grid(column=1, row=1)
        ttk.Label(self.maine_frame, text='Y:').grid(column=1, row=2)
        ttk.Label(self.maine_frame, text='Radius:').grid(column=3, row=1)
        ttk.Label(self.maine_frame, text='Arc Length:').grid(column=3, row=2)
        ttk.Label(self.maine_frame, text='Arc Phase:').grid(column=5, row=2)
        
        self.populate_widgets()
        self.make_reticle()
        self.set_callbacks()
        
        for child in self.maine_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
        
    def make_reticle(self):
        """ toss the reticle onto the image right there in the middle"""
        self.horz_line = self.image_canvas.create_line(340,350,360,350, fill='red')
        self.vert_line = self.image_canvas.create_line(350,360,350,340, fill='red')
        self.reticle_arc = self.image_canvas.create_arc(330,330, 370,370, outline='red', style='arc')
        
    def populate_widgets(self):
        """ Create and add the widgets to the window. """
        self.scream = Image.open('.\\ordo hereticus seal.jpg')
        self.scream_tkver = ImageTk.PhotoImage(self.scream)
        
        self.x_var = IntVar()
        self.y_var = IntVar()
        self.radius_var = IntVar()
        self.arc_length_var = IntVar()
        self.arc_phase_var = IntVar()
        
        self.radius_var.set(20)
        self.arc_length_var.set(90)
        
        self.x_entry = ttk.Entry(self.maine_frame, textvariable=self.x_var)
        self.y_entry = ttk.Entry(self.maine_frame, textvariable=self.y_var)
        self.radius_entry = ttk.Entry(self.maine_frame, textvariable=self.radius_var)
        self.arc_length_entry = ttk.Entry(self.maine_frame, textvariable=self.arc_length_var)
        self.arc_phase_entry = ttk.Entry(self.maine_frame, textvariable=self.arc_phase_var)
        self.next_butt = ttk.Button(self.maine_frame, text='Next')
        self.image_canvas = Canvas(self.maine_frame, width=700, height=700)
        self.image = self.image_canvas.create_image((350,350), image=self.scream_tkver)   
        self.file_list_box = Listbox(self.maine_frame)  
        self.menu_bar = Menu(self.root) 
        self.file_menu = Menu(self.menu_bar)
        
        self.x_entry.grid(column=2, row=1)
        self.y_entry.grid(column=2, row=2)
        self.radius_entry.grid(column=4, row=1)
        self.arc_length_entry.grid(column=4, row=2)
        self.arc_phase_entry.grid(column=6, row=2)
        self.next_butt.grid(column=8, row=2)
        self.image_canvas.grid(column=1, row=0, columnspan=8) 
        self.file_list_box.grid(column=0, row=0, rowspan=3, sticky=(N, W, S, E))
        self.file_menu.add_command(label='Open', command=self.menu_item_open)
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Quit')
        self.menu_bar.add_cascade(menu=self.file_menu, label='File')
        
        self.root.config(menu=self.menu_bar)
        
    def update_file_list(self, newList):
        """ Replace the current list of files with a new list. """
        self.file_list_box.delete(0, END)
        for item in newList:
            self.file_list_box.insert(END, item)
            
    def update_file_select(self, a):
        print(self.file_list_box.get(self.file_list_box.curselection()))
        box_idx = self.file_list_box.curselection()[0]
        self.scream = Image.open(self.filepath + '/' + self.file_list_box.get(box_idx))
        self.scream_tkver = ImageTk.PhotoImage(self.scream)
    
    def update_on_click(self, a):
        """ Update the position of the reticle on a click on the image. """
        r = int(self.radius_entry.get())
        theta = int(self.arc_length_entry.get())
        psi = int(self.arc_phase_entry.get())
        self.image_canvas.coords(self.horz_line, a.x-10, a.y, a.x+10, a.y)
        self.image_canvas.coords(self.vert_line, a.x, a.y-10, a.x, a.y+10)
        self.image_canvas.coords(self.reticle_arc, a.x-r, a.y-r, a.x+r, a.y+r)
        self.image_canvas.itemconfigure(self.reticle_arc, start=psi, extent=theta)
        self.x_entry.delete(0, END)
        self.y_entry.delete(0, END)
        self.x_entry.insert(0, str(a.x - (700 - self.scream.width)/2))
        self.y_entry.insert(0, str(-1*(a.y - (700 - self.scream.height/2))))
            
    def update_on_return(self, a):
        """ update the reticle's location when you hit return on the coordinate inputs """
        self.update_file_list(['a', 'b', 'Lorem ipsum dolor sit amet'])
        x = float(self.x_entry.get())
        y = -1*float(self.y_entry.get())
        x = x + (700 - self.scream.width)/2
        y = y + (700 + self.scream.height)/2
        self.image_canvas.coords(self.horz_line, x-10, y, x+10, y)
        self.image_canvas.coords(self.vert_line, x, y+10, x, y-10)
        pass
    
    def run(self):
        """ make it go"""
        self.root.mainloop()

    def menu_item_open(self):
        """Loads in all the files in the given directory."""
        self.filepath = filedialog.askdirectory()
        if(self.filepath==''):
            return
        the_list_of_files = ldr.get_files_in(self.filepath)
        self.update_file_list(the_list_of_files)

    def menu_item_exit(self):
        """Exits the program"""
        sys.exit(0)

    def set_callbacks(self):
        """Set callbacks in the object."""
        self.image_canvas.bind('<Button-1>', lambda x: self.update_on_click(x))
        self.x_entry.bind('<Return>', lambda x: self.update_on_return(x))
        self.y_entry.bind('<Return>', lambda x: self.update_on_return(x))
        self.radius_entry.bind('<Return>', lambda x: self.update_on_click(x))
        self.file_list_box.bind('<<ListboxSelect>>', lambda x: self.update_file_select(x))


        
if __name__ == "__main__":
    
    gui = GFRGBGUI(Tk())
    gui.run()