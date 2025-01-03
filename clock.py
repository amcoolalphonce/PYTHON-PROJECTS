import time
import tkinter as tk 

def update_time():
    current_time = time.strftime('%H: %M: %S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title('Digital Clock')

clock_label = tk.Label(root, text ='', font=('Calibri', 40, 'bold'), pady=150, foreground='black')
clock_label.pack(anchor='center')
update_time()
root.mainloop()
