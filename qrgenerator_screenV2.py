import sys
import qrcode
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Widget

# this func generate the QR Code of the link passed in entry bar
def qr_gen():
    link = entry_link.get()

    qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

    qr.add_data(link)
    qr.make(fit=True)

    data = [("Image Files", "*.png *.jpg")]
    img = qr.make_image(fill_color="black", back_color="white")

    arquivo = filedialog.asksaveasfilename(filetypes=data, defaultextension=data)

    if arquivo is not None:
        print("Arquivo foi criado")    
        img.save(arquivo)
    else:
        print("Erro")     

    entry_link.delete(0,END)

    label_verify.config(text="✔️")


color1 = '#4a6c6f' #Myrtle Green
color2 = '#c0bcb5' #Silver
color3 = '#af5d63' #Redwood
color4 = '#ADFF2F' #greenyellow

window = Tk()
window.title('QR Generator')
window.geometry('500x250')
window.config(bg=color1)
window.resizable(width=False, height=False)

label_title = Label(window, width=20, text= "QR Generator", font='Times 25',  fg=color2, bg=color1)
label_title.place(x=75, y=40)

label_verify = Label(window, width=8, text= "", fg=color4, bg=color1)
label_verify.place(x=230, y=130)

button1 = Button(window, command=qr_gen, width=8, height=1, text= "QR", relief='raised', font='Times 25',  fg=color2, bg=color3)
button1.place(x=180, y=160)

entry_link = Entry(window, width=35, relief='sunken', font='Times 15')
entry_link.place(x=80, y=100)

window.mainloop()

# Powered by Ailson Guedes Da Fonseca
# GitHub: https://github.com/ailsonguedes
# linkdIn: https://www.linkedin.com/in/ailson-guedes-059795149/