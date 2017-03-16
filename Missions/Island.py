# Island Mission
from Missions import Movement

def start():
    print()
    infront= Movement.listen()
    aligned = False


    while not aligned:
        #move
        infront = Movement.listen()
        if infront == "":
            aligned = True
    Movement.forward(10)

    alignedTop = False

    while not alignedTop:
        direction = Movement.listen()
        x = direction.angle
        y = direction.vector


        if -50 < x < 50:
            print()
            x=0

        elif x > 0:
            Movement.left()

        elif x < 0:
            Movement.right()

        if -50 < y < 50:
            print()
            y=0

        elif y > 0:
            Movement.move_front()

        elif y < 0:
            Movement.move_back()

        else:
            alignedTop = True

    Movement.surface(10)

    if Movement.get_depth() == 0:
        Movement.stop()




"""
VERSION CONTROL:

5- Esteban Lopez 15/03/17
definicion de x y, arreglar pal de cosas de movement

4- Esteban Lopez 08/03/17
ifs

3 - Fernando Ortiz 22/02/17
Commented possible collision code to be fixed

2- Esteban 22/02/17
Island code implementation

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""