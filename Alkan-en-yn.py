

from tkinter import *
from turtle import *

root = Tk()

root.geometry("400x300")
root.title("Kolväte uträknare / målare  - 2021, 8an")
root.resizable(False, False)
root.iconbitmap("atom.ico")

bg = PhotoImage(file="myOWN.png")

my_canvas = Canvas(root, width=600, height=600)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")

alkan_list = ["Metan:", "Etan:", "Propan:", "Butan:", "Pentan:", "Hexan:", "Heptan:", "Oktan:", "Nonan:", "Dekan:", "Undekan:", "Dodekan:", "Tridikan:", "Tetradekan:", "Pentadekan:", "Hexadekan:", "Heptadekan", "Oktadekan:", "Nonadekan:", "Eikosan:"]

alken_list = ["Eten:", "Propen:", "Buten:", "Penten:", "Hexen:", "Hepten:", "Okten:", "Nonen:", "Deken:", "Undeken:", "Dodeken:", "Tridiken:", "Tetradeken:", "Pentadeken:", "Hexadeken:", "Heptedeken:", "Oktadeken:", "Nonadeken:", "Eikosen:"]

alkyn_list = ["Etyn:", "Propyn:", "Butyn:", "Pentyn:", "Hexyn:", "Heptyn:", "Oktyn:", "Nonyn:", "Dekyn:", "Undekyn:", "Dodekyn:", "Tridikyn:", "Tetradekyn:", "Pentadekyn:", "Hexadekyn:", "Heptadekyn:", "Oktadekyn:", "Nonadekyn:", "Eikosyn:"]

def main_func():
    
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

        if int(current_value.get()) > len(alkan_list):
            screen_name = ("Okänd:", "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)
        
        else:
            screen_name = (alkan_list[int(current_value.get()) - 1], "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)


        turtle.screen.title(screen_name)

                
            
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

        
        if int(current_value.get()) > len(alken_list) + 1:
            screen_name = ("Okänd:", "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)
        else:
                

            screen_name = (alken_list[int(current_value.get()) - 2], "C", int(current_value.get()), "H", int(current_value.get()) * 2)
        

        

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
        if int(current_value.get()) <= 2:
                
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

        if int(current_value.get()) > len(alkyn_list) + 1:
            screen_name = ("Okänd:", "C", int(current_value.get()), "H", int(current_value.get()) * 2 + 2)
        
        else:   
                
            screen_name = (alkyn_list[int(current_value.get()) - 2], "C", int(current_value.get()), "H", int(current_value.get()) * 2 - 2)

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
            
            
            
            forward(80)
            if value >= 3:
                    
                    circle(15)
            else:
            
                    fillcolor("white")
                    begin_fill()
                    circle(15)
                    end_fill()
            value =+1
            
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

alkan = Label(root, text="Kolväte-uträknare-målare", font=('Times New roman', 15), bg="#FFFFFF")
alkan.place(x = 75, y = 60)



chose_lab = Label(root, text="Ange serie:", font=('Helvetica', 12), bg="#FFFFFF")
chose_lab.place(x = 10, y = 125)

alter_list = ["1. Alkanserien", "2. Alkenserien", "3. Alkynserien"]

choosed = StringVar()
choosed.set("1. Alkanserien")

alternativ = OptionMenu(root, choosed, *alter_list)
alternativ.configure(font=('Helvetica', 11))
alternativ.place(x = 10, y = 150)


lbl = Label(root, text="Ange antalet kolatomer:", font=('Helvetica', 12), bg="#FFFFFF")
lbl.place(x = 10, y = 230)


current_value = StringVar(value=0)


from_value = 1

enter = Spinbox(root, from_=from_value, to=len(alkan_list), width="27", font=('Helvetica',15), textvariable=current_value)
enter.place(x = 10, y = 260)



submit = Button(root, text="Kör!", width="6", command=main_func)
submit.place(x = 335, y = 260)


root.mainloop()


