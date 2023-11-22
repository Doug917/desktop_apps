from tkinter import *
from tkinter import messagebox


def gen_color():

    try:
        rval = int(rbox.get())
        gval = int(gbox.get())
        bval = int(bbox.get())
    except ValueError:
        messagebox.showerror(title="Error", message="One or more RGB fields empty or invalid.")

    if any([rval>255,gval>255,bval>255]) or any([rval<0,gval<0,bval<0]):
        messagebox.showerror(title="Error", message="Color inputs must be in the range 0 - 255.")
        return 1
    
    x,y = divmod(rval, 16)
    xp,yp = divmod(gval, 16)
    xpp,ypp = divmod(bval, 16)

    Hexlist = ['0','1','2','3','4','5','6','7','8','9','A',
               'B','C','D','E','F']

    result = "".join([Hexlist[i] for i in [x,y,xp,yp,xpp,ypp]])
    hexcode.config(text='#'+result)
    canvas.itemconfig(rectangle, fill='#'+result, outline='#'+result)


window = Tk()
window.minsize(600,300)
window.maxsize(1200,600)
window.title("RGB Codes")
window.config(padx=50, pady=50)

canvas = Canvas(width=120, height=120, highlightthickness=0)
rectangle = canvas.create_rectangle(-50, 0, 50, 50)
canvas.grid(row=6, column=3)

r = Label(text="Red [0-255]", font=("Calibri",12,"normal"))
r.grid(row=0,column=0)
rbox = Entry()
rbox.grid(row=1,column=0)
rbox.focus()
g = Label(text="Green [0-255]", font=("Calibri",12,"normal"))
g.grid(row=2,column=0)
gbox = Entry()
gbox.grid(row=3,column=0)
b = Label(text="Blue [0-255]", font=("Calibri",12,"normal"))
b.grid(row=4,column=0)
bbox = Entry()
bbox.grid(row=5,column=0)

hexcode = Label(text="HexCode", font=("Calibri",12,"normal"))
hexcode.grid(row=3, column=2)

generate = Button(text="Generate Color", font=("Calibri",12,"normal"), command=gen_color)
generate.grid(row=3, column=1)






window.mainloop()