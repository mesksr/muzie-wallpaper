import ctypes
import random
import os
import tkinter
import urllib
from bs4 import BeautifulSoup
from tkinter import messagebox
from PIL import Image, ImageFilter

#global variables
current_wallpaper = ''
blur_level = 0
dim_level = 1
grey_level = 0

def set_wallpaper():
    # edits and sets the wallpaper
    image = Image.open('images/'+current_wallpaper)
    image = image.filter(ImageFilter.GaussianBlur(radius=blur_level))
    image = image.point(lambda p: p * dim_level)
    image.save("e.jpeg", "JPEG")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"/e.jpeg" , 0)
    
def set_new_wallpaper():
    messagebox.showinfo("Caution!", "Function under work.")
    # CANNOT SCRAP WEB :/
    # WILL IMPLEMENT USING GOOGLE'S API

def set_random_wallpaper():
    # selects one wallpaper from images folder and sets it
    global current_wallpaper, blur_level, dim_level

    available_images = os.listdir(os.getcwd()+'/images')
    file_name = available_images[random.randint(0, len(available_images)-1)]
    current_wallpaper = file_name

    blur_level = random.randint(2, 4)
    dim_level = random.randint(5, 7)/10
    set_wallpaper()
    
def increase_blur():
    global blur_level
    blur_level += 1
    set_wallpaper()

def decrease_blur():
    global blur_level
    if (blur_level == 0):
        messagebox.showinfo("Caution!", "Blur is set to 0.")
        return
    blur_level -= 1
    set_wallpaper()

def increase_dim():
    global dim_level
    dim_level -= 0.1
    set_wallpaper()

def decrease_dim():
    global dim_level
    if (dim_level == 1):
        messagebox.showinfo("Caution!", "Dim is set to 1.")
        return
    dim_level += 0.1
    set_wallpaper()
    

# gui
root = tkinter.Tk()
root.title("Muzie-Like Wallpaper")
root.geometry('300x65')
root.iconbitmap("C:/Users/mesksr/Documents/GitHub/muzie-wallpaper-coding-challenge/my_logo.ico")
f1 = tkinter.Frame(root)
f1.pack()
f2 = tkinter.Frame(root)
f2.pack()
new_button = tkinter.Button(f1, text = "New", padx = 5, pady = 5, command = set_new_wallpaper)
refresh_button = tkinter.Button(f1, text = "Random", padx = 5, pady = 5, command = set_random_wallpaper)
increase_blur_button = tkinter.Button(f2, text = "Blur++", padx = 5, pady = 5, command = increase_blur)
decrease_blur_button = tkinter.Button(f2, text = "Blur--", padx = 5, pady = 5, command = decrease_blur)
increase_dim_button = tkinter.Button(f2, text = "Dim++", padx = 5, pady = 5, command = increase_dim)
decrease_dim_button = tkinter.Button(f2, text = "Dim--", padx = 5, pady = 5, command = decrease_dim)
new_button.pack(side = tkinter.LEFT)
refresh_button.pack(side = tkinter.RIGHT)
increase_blur_button.pack(side = tkinter.LEFT)
decrease_blur_button.pack(side = tkinter.LEFT)
increase_dim_button.pack(side = tkinter.LEFT)
decrease_dim_button.pack(side = tkinter.LEFT)
root.mainloop()

