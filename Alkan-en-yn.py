

from tkinter import *
from turtle import *

from tkinter import font
from tkinter import messagebox
root = Tk()

root.geometry("400x300")
root.title("ALKANSERIE uträknare / målare")
root.resizable(False, False)
root.iconbitmap("atom.ico")

bg = PhotoImage(file="myOWN.png")

my_canvas = Canvas(root, width=600, height=600)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")

alkan_list = ["Metan:", "Etan:", "Propan:", "Butan:", "Pentan:", "Hexan:", "Heptan:", "Oktan:", "Nonan:", "Dekan:", "Undekan:", "Dodekan:", "Tridikan:"]

alken_list = ["Eten:", "Propen:", "Buten:", "Penten:", "Hexen:", "Hepten:", "Okten:", "Nonen:", "Deken:", "Undeken:", "Dodeken:", "Tridiken:"]

alkyn_list = ["Etyn:", "Propyn:", "Butyn:", "Pentyn:", "Hexyn:", "Heptyn:", "Oktyn:", "Nonyn:", "Dekyn:", "Undekyn:", "Dodekyn:", "Tridikyn:"]

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

    if choosed.get() == "1. Alkanserien":
        
      

        c = (alkan_list[int(current_value.get()) - 1], "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)

        turtle.screen.title(c)


        # FIXA SÅ ATT NAMNET DYKER UPP MITTEN HÖGST UPP!
        #
        # style = ('Arial', 30, 'italic')
        # turtle.write(alkan_list[int(current_value.get()) - 1], font=style, align='center')



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

                
    elif choosed.get() == "2. Alkenserien":
    

        screen_name = (alken_list[int(current_value.get()) - 2], "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)

        turtle.screen.title(screen_name)




        forward(-350)



        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()


        forward(25)
        pencolor("black")
        write("=", font=('Arial', 20))

        pencolor("lightgrey")

        right(90)
        forward(10)

        right(90)
        forward(25)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()

        forward(15)
        right(90)
        forward(50)
        right(90)
        forward(15)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()


        forward(50)
        right(90)
        forward(25)
        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()

        forward(-40)
        if int(current_value.get()) <= 2:
                
            fillcolor("white")
            begin_fill()
            circle(15)
            end_fill()
        
        forward(80)
        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()
        
        forward(-40)
        
        value = int(current_value.get())
                
        vat = value * 2 + 2
        
        rig = value - 1

        if rig == 1:
            rig = 0

        for x in range(rig):
        
            fillcolor("black")
            begin_fill()
            circle(15)
            end_fill()

            forward(-40)

            if value >= 3:
                
                circle(15)
            else:
            
                fillcolor("white")
                begin_fill()
                circle(15)
                end_fill()
            
            value =+1
            
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


       
    elif choosed.get() == "3. Alkynserien":
        
        screen_name = (alkyn_list[int(current_value.get()) - 2], "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)

        turtle.screen.title(screen_name)


        forward(-330)


        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()


        forward(25)
        pencolor("black")
        write("≡", font=('Arial', 20))
        
        pencolor("lightgrey")

        forward(40)
        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()



        forward(15)
        right(-90)
        forward(55)

        if int(current_value.get()) <= 2:
                
            fillcolor("white")
            begin_fill()
            circle(15)
            end_fill()
            
        forward(-65)
        right(-90)
        forward(80)

        fillcolor("white")
        begin_fill()
        circle(15)
        end_fill()


        forward(-50)
        right(90)
        forward(25)
        right(180)

        
        value = int(current_value.get())
                
        vat = value * 2 + 2
        
        rig = value - 1

        if rig == 1:
            rig = 0

        for x in range(rig):
        

            fillcolor("black")
            begin_fill()
            circle(15)
            end_fill()

            forward(-40)

            if value >= 3:
                    
                    circle(15)
            else:
            
                    fillcolor("white")
                    begin_fill()
                    circle(15)
                    end_fill()
            
            value =+1
            
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



chose_lab = Label(root, text="Ange serie:", font=('Helvetica', 12), bg="#FFFFFF")
chose_lab.place(x = 10, y = 125)

alter_list = ["1. Alkanserien", "2. Alkenserien", "3. Alkynserien"]

choosed = StringVar()
choosed.set("1. Alkanserien")

alternativ = OptionMenu(root, choosed, *alter_list)
alternativ.configure(bg="white", font=('Helvetica', 11), highlightbackground="white")
alternativ.place(x = 10, y = 150)


lbl = Label(root, text="Ange antalet kolatomer:", font=('Helvetica', 12), bg="#FFFFFF")
lbl.place(x = 10, y = 230)


current_value = StringVar(value=0)


from_value = 1

enter = Spinbox(root, from_=from_value, to=len(alkan_list), width="27", font=('Helvetica',15), textvariable=current_value)
enter.place(x = 10, y = 260)



submit = Button(root, text="Kör!", width="6", command=hej)
submit.place(x = 335, y = 260)


root.mainloop()
