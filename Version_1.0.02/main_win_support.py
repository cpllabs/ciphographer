import sys
import os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import output
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import main_win
atbash_cap = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
atbash_sma = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def decider(pros,text,shift):
    c = globals() [pros]
    output.ent = text
    if shift != '':
        try:
            output.out = c(text,int(shift))
        except:
            output.out = c(text,shift)
    else:
        output.out = c(text)
    output.vp_start_gui()
    

def decider_file(process,file,shift):
    c = globals() [process]
    if shift != '':
        try:
            c(file,int(shift))
        except:
            c(file,shift)
    else:
        c(file)


def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def encrypt_caesar(da,y):
    x = 65
    key = y
    smalls = dict()
    s = {}
    while x+y <= 90:
        s[chr(x)]=chr(x+y)
        x += 1
    if x != 90:
        y = 65
        while x <= 90:
            s[chr(x)] = chr(y)
            x += 1 ; y+= 1
    for i in s:
        smalls[i.lower()]= s[i].lower()
    ans =''
    for i in da :
        if i in s:
            ans += s[i]
        else:
            ans += smalls.get(i,i)
    return ans
    

def decrypt_caesar(da,y):
    x = 65
    key = y
    smalls = dict()
    s = {}
    while x+y <= 90:
        s[chr(x)]=chr(x+y)
        x += 1
    if x != 90:
        y = 65
        while x <= 90:
            s[chr(x)] = chr(y)
            x += 1 ; y+= 1
    for i in s:
        smalls[i.lower()]= s[i].lower()
    des = dict(zip(s.values(),s.keys()))
    desmall = dict(zip(smalls.values(),smalls.keys()))
    del smalls, s
    ans = ''
    for i in da :
        if i in des:
            ans += des[i]
        else:
            ans += desmall.get(i,i)
    return ans

def file_decrypt_caesar(file,shift):
    f = open(file,'r')
    wf = open(file +'_decrypted.txt','w')
    for line in f:
      if line != '':
        wf.write(decrypt_caesar(line,shift))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_decrypted.txt'))
    wf.close()

def file_encrypt_caesar(file,shift):
    f = open(file,'r')
    wf = open(file +'_encrypted.txt','w')
    for line in f:
        if line != '':
            wf.write(encrypt_caesar(line,shift))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_encrypted.txt'))
    wf.close()

def encrypt_atbash(t,NoUse=None):
    ans = ''
    for i in t:
        if i in atbash_cap:
            ans += atbash_cap[i]
        else:
            ans += atbash_sma.get(i,i)
    return ans

def decrypt_atbash(t,NoUse=None):
    ans = ''
    for i in t:
        if i in atbash_cap:
            ans += atbash_cap[i]
        else:
            ans += atbash_sma.get(i,i)
    return ans

def file_decrypt_atbash(file, NoUse=None):
    f = open(file,'r')
    wf = open(file +'_decrypted.txt','w')
    for line in f:
      if line != '':
        wf.write(decrypt_atbash(line))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_decrypted.txt'))
    wf.close()
    
def file_encrypt_atbash(file,NoUse=None):
    f = open(file,'r')
    wf = open(file +'_encrypted.txt','w')
    for line in f:
        if line != '':
            wf.write(encrypt_atbash(line))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_encrypted.txt'))
    wf.close()


def encrypt_monoalphabetic(x,key):
    ans =''
    d_cap=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    d_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic_cap = dict(zip(d_cap,list(key.upper())))
    dic_small = dict(zip(d_small,list(key.lower())))
    for i in x:
        if i in dic_cap:
            ans += dic_cap[i]
        else:
            ans += dic_small.get(i,i)
    return ans

def decrypt_monoalphabetic(x,key):
    ans =''
    d_cap=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    d_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic_cap = dict(zip(list(key.upper()),d_cap))
    dic_small = dict(zip(list(key.lower()),d_small))
    for i in x:
        if i in dic_cap:
            ans += dic_cap[i]
        else:
            ans += dic_small.get(i,i)
    return ans

def file_encrypt_monoalphabetic(file,key):
    f = open(file,'r')
    wf = open(file +'_encrypted.txt','w')
    for line in f:
        if line != '':
            wf.write(encrypt_monoalphabetic(line,key))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_encrypted.txt'))
    wf.close()
def file_decrypt_monoalphabetic(file,key):
    f = open(file,'r')
    wf = open(file +'_decrypted.txt','w')
    for line in f:
      if line != '':
        wf.write(decrypt_monoalphabetic(line,key))
    f.close()
    messagebox.showinfo('Success','File Saved : {0}'.format(file +'_decrypted.txt'))
    wf.close()
    
if __name__ == '__main__':
    import main_win
    main_win.vp_start_gui()




