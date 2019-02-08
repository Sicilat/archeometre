from tkinter import *
from tkinter import ttk

root = Tk()

capa = 3
capb = 2
capc = 1
x_pos = 4
y_pos = 5
z_pos = 6

def reset():
    global capa
    global capb
    global capc
    global x_pos
    global y_pos
    global z_pos
    global x_pos_val_lbl
    global y_pos_val_lbl
    global z_pos_val_lbl
    capa = 0
    capb = 0
    capc = 0
    x_pos = 0
    y_pos = 0
    z_pos = 0
    print("Reset")







while True:
    content = ttk.Frame(root, padding=(3,3,12,12))

    capa_lbl = ttk.Label(content, text=capa)
    capb_lbl = ttk.Label(content, text=capb)
    capc_lbl = ttk.Label(content, text=capc)
    calculate = ttk.Button(content, text="Calculer")

    copy = ttk.Button(content, text="Copier")
    ref = ttk.Frame(content)
    pos = ttk.Frame(content)
    x_ref_lbl = ttk.Label(ref, text="X")
    x_ref_val_lbl = ttk.Label(ref, text="x_val_ref")
    y_ref_lbl = ttk.Label(ref, text="Y")
    y_ref_val_lbl = ttk.Label(ref, text="y_val_ref")
    z_ref_lbl = ttk.Label(ref, text="Z")
    z_ref_val_lbl = ttk.Label(ref, text="z_val_ref")
    x_pos_lbl = ttk.Label(pos, text="X")
    x_pos_val_lbl = ttk.Label(pos, text=x_pos)
    y_pos_lbl = ttk.Label(pos, text="Y")
    y_pos_val_lbl = ttk.Label(pos, text=y_pos)
    z_pos_lbl = ttk.Label(pos, text="Z")
    z_pos_val_lbl = ttk.Label(pos, text=z_pos)
    reset = ttk.Button(content, text="Reset", command=reset)


    content.grid(column=0, row=0, sticky=(N, S, E, W))
    capa_lbl.grid(column=0, row=0, sticky=(N, S, E, W))
    capb_lbl.grid(column=1, row=0)
    capc_lbl.grid(column=2, row=0)
    calculate.grid(column=0, row=1)
    reset.grid(column=1, row=1)
    copy.grid(column=2, row=1)
    ref.grid(column=0, row=2)
    pos.grid(column=2, row=2)
    x_ref_lbl.grid(column=0, row=0)
    x_ref_val_lbl.grid(column=1, row=0)
    y_ref_lbl.grid(column=0, row=1)
    y_ref_val_lbl.grid(column=1, row=1)
    z_ref_lbl.grid(column=0, row=2)
    z_ref_val_lbl.grid(column=1, row=2)
    x_pos_lbl.grid(column=0, row=0)
    x_pos_val_lbl.grid(column=1, row=0)
    y_pos_lbl.grid(column=0, row=1)
    y_pos_val_lbl.grid(column=1, row=1)
    z_pos_lbl.grid(column=0, row=2)
    z_pos_val_lbl.grid(column=1, row=2)


    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.rowconfigure(0, weight=3)
    content.rowconfigure(1, weight=3)
    content.rowconfigure(2, weight=3)
    ref.columnconfigure(0, weight=1)
    ref.columnconfigure(1, weight=1)
    ref.rowconfigure(0, weight=1)
    ref.rowconfigure(1, weight=1)
    ref.rowconfigure(2, weight=1)
    pos.columnconfigure(0, weight=1)
    pos.columnconfigure(1, weight=1)
    pos.rowconfigure(0, weight=1)
    pos.rowconfigure(1, weight=1)
    pos.rowconfigure(2, weight=1)

    root.mainloop()
