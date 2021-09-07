

from tkinter import *
from turtle import *

root = Tk()

root.geometry("400x300")
root.title("ALKANSERIE uträknare / målare")
root.resizable(0, 0)
root.iconbitmap("atom.ico")

bg = PhotoImage(file="myOWN.png")

my_canvas = Canvas(root, width=600, height=600)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")




def hej(*args):
    
    root.destroy()
    turtle = Turtle()
    speed(0)
    pencolor("lightgrey")
    turtle.hideturtle()
    hideturtle()
        
    bgcolor("lightgrey")

    height = 360
    width = 860
    turtle.screen.setup(width, height)

   

    coal_list = ["Metan:", "Etan:", "Propan:", "Butan:", "Pentan:", "Hexan:", "Heptan:", "Oktan:", "Nonan:", "Dekan:", "Undekan:", "Dodekan:", "Tridikan:"]



    c = (coal_list[int(current_value.get()) - 1], "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)

    

    turtle.screen.title(c)


    

    kol = "black"
    vate = "white"

    
    
        
    forward(-350)



    fillcolor("black")
    begin_fill()
    circle(15)
    end_fill()

    fillcolor("white")
    begin_fill()
    forward(-40)
    circle(15)

    forward(80)
    circle(15)
    end_fill()

    right(90)
    forward(10)
    right(90)
    forward(40)

    fillcolor("white")
    begin_fill()
    circle(15)

    end_fill()

    forward(-15)
    right(90)
    forward(50)
    right(90)
    forward(-15)

    fillcolor("white")
    begin_fill()
    circle(15)
    end_fill()


    forward(25)
    right(90)
    forward(25)


    value = int(current_value.get())
    
    vat = value * 2 + 2

    rig = value - 1
    
    for x in range(rig):
    
        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()

        forward(-40)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()

        forward(80)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()

        forward(-25)
        right(-90)
        forward(55)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()

        forward(-15)
        right(90)
        
        forward(-15)

            
    turtle.getscreen()._root.mainloop()

name = Label(root, text="Samuel Maniscalchi Bäckmans", font=('Times New roman', 20), bg="#FFFFFF")
name.place(x = 20, y = 20)

alkan = Label(root, text="Alkanserie-uträknare-målare", font=('Times New roman', 15), bg="#FFFFFF")
alkan.place(x = 75, y = 60)

lbl = Label(root, text="Ange antalet kolatomer:", font=('Helvetica', 12), bg="#FFFFFF")
lbl.place(x = 10, y = 230)


current_value = StringVar(value=0)

enter = Spinbox(root, from_=1, to=30, width="27", font=('Helvetica',15), textvariable=current_value)
enter.place(x = 10, y = 260)



submit = Button(root, text="Kör!", width="6", command=hej)
submit.place(x = 335, y = 260)


root.mainloop()


