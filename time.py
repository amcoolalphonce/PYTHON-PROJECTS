import tkinter as tk
import time
def update_time():
  currrent_time = time.strftime('%H:%M:%S')
  clock_label.config(text=current_time)
  root.after(1000, update_time)

root = tk.Tk()
root.tile("DIGITAL CLOCK")
clock_label = tk.Label(root, text="", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)
update_time()
root.mainloop()
