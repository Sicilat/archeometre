from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
capa_lbl = ttk.Label(content, text="val_capA")
capb_lbl = ttk.Label(content, text="val_capB")
capc_lbl = ttk.Label(content, text="val_capC")
calculate = ttk.Button(content, text="Calculer")
copy = ttk.Button(content, text="Copier")
ref = ttk.Frame(content)
pos = ttk.Frame(content)


content.grid(column=0, row=0, sticky=(N, S, E, W))
capa_lbl.grid(column=0, row=0, sticky=(N, S, E, W))
capb_lbl.grid(column=1, row=0)
capc_lbl.grid(column=2, row=0)
calculate.grid(column=0, row=1)
copy.grid(column=2, row=1)
ref.grid(column=0, row=2)
pos.grid(column=2, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.rowconfigure(0, weight=3)
content.rowconfigure(1, weight=3)
content.rowconfigure(2, weight=3)

root.mainloop()
