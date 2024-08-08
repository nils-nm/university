import tkinter as tk
from tkinter import Tk, ttk

def down(event):
    global cols_from, dx, cols_from_id
    db= event.widget
    if db.identify_region(event.x, event.y) != 'separator':
        cols = db.identify_column(event.x)
        cols_from_id =db.column(cols, 'id')
        cols_from = int(cols[1:]) - 1

        bbox = db.bbox(db.get_children("")[0], cols_from_id)
        dx = bbox[0] - event.x
        db.heading(cols_from_id, text='')
        visual_drag.configure(displaycolumns=[cols_from_id])
        visual_drag.place(in_=db, x=bbox[0], y=0, anchor='nw', width=bbox[2], relheight=1)
    else:
        cols_from = None

def BUP(event):
    db = event.widget
    cols_to = int(db.identify_column(event.x)[1:]) - 1
    visual_drag.place_forget()
    if cols_from is not None:
        db.heading(cols_from_id, text=visual_drag.heading('#1', 'text'))
        if cols_from != cols_to:
            Tcols = list(db["displaycolumns"])
            if Tcols[0] == "#all":
                Tcols = list(db["columns"])

            if cols_from > cols_to:
                Tcols.insert(cols_to, Tcols[col_from])
                Tcols.pop(cols_from + 1)
            else:
                Tcols.insert(cols_to + 1, Tcols[cols_from])
                Tcols.pop(cols_from)
            db.config(displaycolumns=Tcols)

def BMotion(event):

    if visual_drag.winfo_ismapped():
        visual_drag.place_configure(x=dx + event.x)



col_from = 0

ws= Tk()


columns = ["D", "C", "B", "A"]

sort = ttk.Treeview(ws, columns=columns, show='headings')

visual_drag = ttk.Treeview(ws, columns=columns, show='headings')

for cols in columns:
    sort.heading(cols, text=cols)
    visual_drag.heading(cols, text=cols)


for i in range(10):
    sort.insert('', 'end', iid='line%i' % i,
                values=(i+50, i+40, i+30, i+20, i+10))
    visual_drag.insert('', 'end', iid='line%i' % i,
                       values=(i+50, i+40, i+30, i+20, i+10))

sort.grid()
sort.bind("<ButtonPress>", down)
sort.bind("<ButtonRelease>",BUP)
sort.bind("<Motion>",BMotion)

ws.mainloop()
