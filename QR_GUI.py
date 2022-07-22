import os
os.system('cls')
import tkinter as tk
import pyqrcode
from tkinter import Frame, ttk

window = tk.Tk()
fram= ttk.Frame()
fram.pack()

window.title('QR generator')
window.geometry('300x500')
window.configure(background='white')


Entry_user = tk.Entry(
    master=window, 
    width=20, 
    border=3,
)

def QR_generator(*args):

    global QR_img
    user_input = Entry_user.get()
    user_input = pyqrcode.create(user_input)
    QR_img = tk.BitmapImage(data= user_input.xbm(scale=5), foreground="black", background='white')
    lbl_result1.config(image=QR_img)
    lbl_result2.config(text=str(Entry_user.get()))


lbl = tk.Label(
    master=window,
    text="Enter your link in box below", 
    font="Times 13 bold",
    foreground='darkred', 
    background='white',
    border=5
)
btn = tk.Button(
    master=window,
    text="Generate", 
    font="Times 12 bold",
    command=QR_generator,
    border=3,
)
lbl_result1 = tk.Label(
    master=window, 
    borderwidth=2, 
    border=3
)

lbl_result2 = tk.Label(
    master=window,
    text = 'waiting for your input ...' ,
    font= 'Times 12 ', 
    foreground='blue', 
    background='yellow')


# create hyperlink
import webbrowser
def callback(url):
    webbrowser.open_new(url)

window.bind('<Return>' , QR_generator)
lbl_result2.bind("<Button-1>", lambda e: callback(str(Entry_user.get())))


exit_btn = tk.Button(
    master=window,
    command=window.destroy, 
    text='Exit',
    font="Times 12 bold",
    border=3,
    padx=20
)


lbl.pack()
Entry_user.pack()
btn.pack()
exit_btn.pack()
lbl_result1.pack()
lbl_result2.pack()
window.mainloop()