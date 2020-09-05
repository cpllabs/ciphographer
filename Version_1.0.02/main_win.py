import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import filedialog
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from tkinter import messagebox
import main_win_support
import starter
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    
    main_win_support.set_Tk_var()
    top = Ceasar_root (root)
    main_win_support.init(root, top)
    root.mainloop()

w = None
def create_Ceasar_root(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    main_win_support.set_Tk_var()
    top = Ceasar_root (w)
    main_win_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Ceasar_root():
    global w
    w.destroy()
    w = None
algo_name = {'Caesar Cipher':'caesar','Hill Top':'hill_top','Atbash Cipher':'atbash','Monoalphabetic Cipher':'monoalphabetic'}
what = ''
algo = ''
import starter
class Ceasar_root:
    def go_back(self):
        root.destroy()
        starter.vp_start_gui()
        
    def open_file(self):
        global x
        x = filedialog.askopenfilename()
        self.Label4.configure(text='Current File : {0}'.format(x))
        if x[:3] == 'C:/':
            messagebox.showwarning('Admin Permissions Required','To Use a File From C Drive, We Suggest\
 You To Run The Software as Administrator As Writing And Reading Files From Some Locations Require Special Permissions')
        if x != '' and x.endswith('.txt') == False:
            messagebox.showwarning('File Format Checkup','File You Selected in not a Text File (.txt) . Software May Fail To\
 Process This File.\nTry Chosing .txt - Text File')

    def key_validate(self,algo,key):
        c = True
        if algo == 'caesar':
            if key.isdigit() == False:
                messagebox.showerror('Invalid Key','Key Must Be Positive Integer')
                c = False
        elif algo == 'atbash' and key != '':
            messagebox.showinfo('Information','Key Not Required For Atbash Cipher Technique')
        elif algo == 'monoalphabetic' and key != '':
            if len(key) != 26:
                messagebox.showerror('Invalid Key','Key Must Contain All Alphabets Without Repetation (In Any Order)')
                c = False
        elif algo == 'monoalphabetic' and key == '':
            messagebox.showerror('Invalid Key','Key Must Contain All Alphabets Without Repetation (In Any Order)')
            c = False
        return c
    def file_enc_dec(self):
        process = 'file_'+what.lower()+'_'
        if x =='':
             messagebox.showerror('Select File','No File Selected. Please Select a File First')
        file = x
        if self.key_validate(algo_name.get(algo),self.file_shift_ent.get()) :
            shift = self.file_shift_ent.get()
            process += algo_name.get(algo)
            main_win_support.decider_file(process,file,shift)
        else:
            return False
    
        
    def text_enc_dec(self):
        process = what.lower()+'_'
        text = self.text_ent.get()
        if self.key_validate(algo_name.get(algo),self.shift_ent_inp.get()) :
            shift = self.shift_ent_inp.get()
            process += algo_name.get(algo)
            main_win_support.decider(process,text,shift)
            
        else:
            return False
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI Emoji} -size 11 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family Arial -size 13 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family {Sitka Subheading} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font16 = "-family {Sitka Subheading} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family Arial -size 11 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x520+351+152")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,1)
        top.title("{0} Algorithm - Ciphographer".format(algo))
        top.configure(background="#c9c9c9")
        try:
            top.iconbitmap('i.ico')
        except:
            pass
        
        self.text_ent = tk.Entry(top)
        self.text_ent.place(relx=0.2, rely=0.143,height=30, relwidth=0.373)
        self.text_ent.configure(background="white")
        self.text_ent.configure(disabledforeground="#a3a3a3")
        self.text_ent.configure(font="-family {Courier New} -size 10")
        self.text_ent.configure(foreground="#000000")
        self.text_ent.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.017, rely=0.122, height=51, width=104)
        self.Label1.configure(background="#c9c9c9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter Text :''')

        self.text_pro = tk.Button(top) #from normal input
        self.text_pro.place(relx=0.45, rely=0.347, height=34, width=87)
        self.text_pro.configure(activebackground="#ececec")
        self.text_pro.configure(activeforeground="#000000")
        self.text_pro.configure(background="#d9d9d9")
        self.text_pro.configure(disabledforeground="#a3a3a3")
        self.text_pro.configure(font=font14)
        self.text_pro.configure(foreground="#000000")
        self.text_pro.configure(highlightbackground="#d9d9d9")
        self.text_pro.configure(highlightcolor="black")
        self.text_pro.configure(pady="0")
        self.text_pro.configure(text='{0}'.format(what))
        self.text_pro.configure(command =self.text_enc_dec)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.068, rely=0.449, relwidth=0.85)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.02, height=51, width=154)
        self.Label2.configure(background="#c9c9c9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''From Input -''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.0, rely=0.469, height=51, width=154)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#c9c9c9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Arial} -size 13 -weight bold")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''From File -''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.067, rely=0.592, height=44, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.open_file)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font16)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open File''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.017, rely=0.224, height=41, width=104)
        self.Label3.configure(background="#c9c9c9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Shift / Key :''')

        self.shift_ent_inp = tk.Entry(top)
        self.shift_ent_inp.place(relx=0.2, rely=0.245, height=20, relwidth=0.373)

        self.shift_ent_inp.configure(background="white")
        self.shift_ent_inp.configure(disabledforeground="#a3a3a3")
        self.shift_ent_inp.configure(font="-family {Courier New} -size 10")
        self.shift_ent_inp.configure(foreground="#000000")
        self.shift_ent_inp.configure(insertbackground="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.283, rely=0.571, relheight=0.133
                , relwidth=0.692)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.024, rely=0.154, height=41, width=384)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font17)
        self.Label4.configure(wraplength = 380)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='Current File : No File Selected')

        self.Label3_2 = tk.Label(top)
        self.Label3_2.place(relx=0.017, rely=0.755, height=41, width=104)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#c9c9c9")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font=font11)
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Shift / Key :''')

        self.file_shift_ent = tk.Entry(top)
        self.file_shift_ent.place(relx=0.2, rely=0.776, height=20
                , relwidth=0.357)
        self.file_shift_ent.configure(background="white")
        self.file_shift_ent.configure(disabledforeground="#a3a3a3")
        self.file_shift_ent.configure(font="-family {Courier New} -size 10")
        self.file_shift_ent.configure(foreground="#000000")
        self.file_shift_ent.configure(insertbackground="black")

        self.text_pro_file = tk.Button(top) #from file
        self.text_pro_file.place(relx=0.45, rely=0.857, height=44, width=87)
        self.text_pro_file.configure(activebackground="#ececec")
        self.text_pro_file.configure(activeforeground="#000000")
        self.text_pro_file.configure(background="#d9d9d9")
        self.text_pro_file.configure(disabledforeground="#a3a3a3")
        self.text_pro_file.configure(font="-family {Sitka Subheading} -size 10")
        self.text_pro_file.configure(foreground="#000000")
        self.text_pro_file.configure(highlightbackground="#d9d9d9")
        self.text_pro_file.configure(highlightcolor="black")
        self.text_pro_file.configure(pady="0")
        self.text_pro_file.configure(text='{0}'.format(what))
        self.text_pro_file.configure(command = self.file_enc_dec)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.583, rely=0.245, height=21, width=51)
        self.Label5.configure(background="#c9c9c9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''( If Any )''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.840, rely=0.904, height=34, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=root.destroy)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Exit''')
 
        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.05, rely=0.904, height=34, width=67)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=self.go_back)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Back''')

        self.Label5_1 = tk.Label(top)
        self.Label5_1.place(relx=0.255, rely=0.960, height=21, width=311)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(background="#c9c9c9")
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''Ciphographer - 1.0.01   (C) CREATORS PVT LTD''')


if __name__ == '__main__':
    vp_start_gui()





