import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import starter_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    starter_support.set_Tk_var()
    top = starter (root)
    starter_support.init(root, top)
    root.mainloop()

w = None
def create_starter(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    starter_support.set_Tk_var()
    top = starter (w)
    starter_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_starter():
    global w
    w.destroy()
    w = None

class starter:
    def send_values(self):
        what = self.TCombobox1.get()
        algo = self.TCombobox2.get()
        if what == '':
            messagebox.showerror('There is a Problem','Please Select What To Do')
            return None
        if algo == '':
            messagebox.showerror('There is a Problem','Please Select Cipher Algorithm To Continue')
            return None
        import main_win
        main_win.algo = algo
        main_win.what = what
        root.destroy()
        main_win.vp_start_gui()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("523x391+394+210")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Start Ciphographer")
        top.configure(background="#c9c9c9")
        try:
            top.iconbitmap('i.ico')
        except:
            pass

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.516, rely=0.256, relheight=0.054
                , relwidth=0.273)
        self.value_list = ['Encrypt','Decrypt']
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=starter_support.enc_de_sel)
        self.TCombobox1.configure(takefocus="")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.400, rely=0.793, height=54, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#e9e9e9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start Ciphographer''')
        self.Button1.configure(command = self.send_values)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.249, rely=0.23, height=41, width=124)
        self.Label1.configure(background="#c9c9c9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''What To Do :''')

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.268, rely=0.665, relheight=0.054
                , relwidth=0.503)
        self.value_list = ['Caesar Cipher','Atbash Cipher','Monoalphabetic Cipher']
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=starter_support.combobox)
        self.TCombobox2.configure(takefocus="")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.229, rely=0.563, height=31, width=294)
        self.Label2.configure(background="#c9c9c9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Select Algorithm Used/To Be Used :''')

if __name__ == '__main__':
    vp_start_gui()
    




