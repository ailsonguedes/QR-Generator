import sys
import qrcode
import tkinter as tk
from PyQt6.QtWidgets import QApplication, QFileDialog ,QWidget, QPushButton, QLabel, QLineEdit
from tkinter import filedialog

def qr_gen():
    
    qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

    qr.add_data(le.text())
    qr.make(fit=True)

    data = [("Image Files", "*.png *.jpg")]
    img = qr.make_image(fill_color="black", back_color="white")

    arquivo = filedialog.asksaveasfilename(filetypes=data, defaultextension=data)

    if arquivo is not None:
        print("Arquivo foi criado")    
        img.save(arquivo)
    else:
        print("Erro")     
    #arquivo = QFileDialog.getSaveFileName()[0]
    #str_arquivo = str(arquivo )

    le.setText("")

    label2.setText("✔️")
    label2.adjustSize()

app =  QApplication(sys.argv)

window = QWidget()
window.resize(600,300)
window.setWindowTitle("QR Generator")

label = QLabel("QR Generator", window)
label.move(200,50)
label.setStyleSheet('font-size: 30px')

label2 = QLabel("", window)
label2.move(260,220)
label2.setStyleSheet('font-size: 30px; color: green')

le = QLineEdit("", window)
le.setGeometry(130,100,350,40)

btn = QPushButton("QR", window)
btn.setGeometry(200,170,150,40)
btn.clicked.connect(qr_gen)

window.show()

app.exec()

# Powered by Ailson Guedes Da Fonseca
# GitHub: https://github.com/ailsonguedes
# linkdIn: https://www.linkedin.com/in/ailson-guedes-059795149/