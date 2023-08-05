from tkinter import Label, Tk

import time
#GUI window
app_window=Tk()
app_window.title("MY DIGITAL CLOCK")     #tiltel my guy
app_window.geometry("500x600")           #size of the window
app_window.resizable(1,1)                #resizable or not
text_font=("ARIAL", 70, 'bold')
background=("#32a852")
foreground=("#a83279")
border_width=25

label=Label(app_window, font="arial", background="green", foreground="black", borderwidth="10").grid(row=4, column=1)
#label.grid=( row=4, column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock())
digital_clock
app_window.mainloop()
