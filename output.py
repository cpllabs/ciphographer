import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import output_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    
    top = output (root)
    output_support.init(root, top)
    root.mainloop()

w = None
def create_output(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = output (w)
    output_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_output():
    global w
    w.destroy()
    w = None
ent = out =''
class output:
            
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI Semibold} -size 13 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x491+369+187")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Result - Ciphographer")
        top.configure(background="#c9c9c9")
        try:
            top.iconbitmap('i.ico')
        except:
            pass
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=391, width=594)
        self.Label1.configure(background="#c9c9c9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(wraplength = 580)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''You Entered : \n{0}\n\nOutput:\n{1}'''.format(ent,out))

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.433, rely=0.855, height=44, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Continue''')
        self.Button1.configure(command = root.destroy)

if __name__ == '__main__':
    vp_start_gui()





