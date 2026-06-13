import tkinter as tk
from time import sleep

host_value = ""
port_value = 0

def save():
    global host_value, port_value
    host_value = host_entry.get()
    port_value = int(port_entry.get())
    status_label.config(text=f"{host_value}:{port_value}")
    sleep(1)
    root.destroy()
root = tk.Tk()
root.title("Launcher")
root.geometry("300x200")

tk.Label(root, text="Host").pack()
host_entry = tk.Entry(root)
host_entry.pack()

tk.Label(root, text="Port").pack()
port_entry = tk.Entry(root)
port_entry.pack()

tk.Button(root, text="Save", command=save).pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()