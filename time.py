import tkinter as tk
import time
def update_time():
  currrent_time = time.strftime('%H:%M:%S')
  clock_label.config(text=current_time)
  root.after(1000, update_time)

root = tk.Tk()
