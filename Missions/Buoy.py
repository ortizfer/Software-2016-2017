# Buoy Mission
from Missions import Movement, Align
from Vision import FrameGrab, messPassing, BoyasExoticas
import time

'''
    The Buoy mission commences by  searching for  buoy's. The
    buoys'  general  direction  is given by the  orange  line
    marker. Once the buoys are detected, the sub will attempt
    to bop the  red buoy, then  the green.  After both  buoys
    have been touched,  the sub  will try to navigate between
    them to begin searching for the next orange line marker.
'''

'''
************************************************************************************************************************
Dictionary:
--Variables--
x: global variable denoting a position
y: global variable denoting a position
percentage: PENDING
near: global variable denoting whether a boolean is near or not

--Functions--
start(): essentially the main function, orders all other functions so the AUV may complete the buoy mission.
    parameter: void
    return: void

position(): Modifies the global variables x and y to current position
    parameter: void
    return: void

isAligned(): it provides whether or not is in the right parameters
    parameter: void
    return: boolean, whether or not it is align
************************************************************************************************************************
'''
x = 0
y = 0
distance = 100
near = False


def start():
    _maxrangex = 630
    _maxrangey = 400
    print("Starting Buoy mission")

    while not near:
        position()
        while not isAligned():
            Align.start()

        Movement.forward(2)

    Movement.forward(0)#to substitute with new algorithm

    """ Exit protocol """

    # Go over buoys
    Movement.depth(3)
    Movement.forward(0)
    Movement.depth(6)

    # Turn accordinly back to center of buyos
    if Align.getFirstTurn() < 0:
        Movement.align(90)
    else:
        Movement.align(-90)

    # Move toward middle of buoys
    Movement.forward(0)

    # Turn back facing gate 2
    if Align.getFirstTurn() < 0:
        Movement.align(-90)
    else:
        Movement.align(90)


def position():
    FrameGrab.frontFrame()
    # add bouy detection findBouy( bool, bool,bool)
    boya = messPassing.messPassing()
    boya = BoyasExoticas.start()
    x = boya.impBuoyX()
    y = boya.impBuoyY()
    distance = boya.impDistance()


def isAligned():
    if x == -1 or y == -1:
        Search()
    if x < 265 or x > 365:
        return False

    if y < 150 or y > 250:
        return False
    if distance <= 3:
        near = True
    else:
        return True

    print("Exiting Buoy mission")


def Search():
    counter = 0

    while counter < 2:

        Movement.align(45)  # Gira hacia la derecha y toma foto para buscar alguna boya.
        position()# Toma foto de Vision

        if (x>0): #Identificó un objeto, sigue corriendo el codigo.
            return

        Movement.align(-90) #Si no identifica objeto hacia la derecha, rota hacia la izquierda y repite el proceso.
        position()

        if (x>0):
            return

        Movement.align(45) # Regresa al punto inicial

        Movement.backward(2) # Retrocede dos segundos y entra otra vez al loop hasta que se cumpla las condiciones.
        counter= counter +1 # De no encontrar boya vuelve a entrar al while hasta 2 veces.

    counter = 0
    while counter <2:
        Movement.align('180')
        time.sleep(2)
        Movement.align('180')
        time.sleep(2)
        counter = counter +1



"""
    while direction.x > 365 or direction.x < 265:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with redBuoy")
        aligned = True

    # move 10 feet then touch the Buoy
    if aligned:

        Movement.forward(10)
        Movement.bop_it()
        Movement.backward()

    greenBuoy = True
    redBuoy = False
    # aligning with green Buoy

    if greenBuoy:

        direction = Movement.get_direction()

        aligned = False

    while direction.angle == 0:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with greenBuoy")
        aligned = True

    if aligned:
        Movement.forward(10)
        Movement.bop_it()
        Movement.backward()

# Exit algorithm
    Movement.forward(5)
"""

"""
VERSION CONTROL:
14- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 6:28 PM
Added documentation and dictionary for the code

13- Sachy Romero 27/02/2017 12:28pm
Added Maxrange X and Maxrange Y

12- Carlos J. Figueroa 23/02/2017 5:01pm
Added basic documentation. Added a naming convention suppressant(line 14).

11- Sachy Romero 22/02/2017
Exit algorithm and pass between the Buoys

10- Sachy Romero 22/02/2017
Touch Green Buoy

9- Sachy Romero 22/02/2017
Aligned with Green Buoy

7- Sachy Romero 22/02/2017
Moved backward to align with green Buoy

6- Sachy Romero Rosado 22/02/2017
Touch Red Buoy

5- Sachy Romero 22/02/2017
Aligned to Red Buoy

4- Sachy Romero 21/02/17
Added boolean variable for Buoy mission

3- Fernando Ortiz 20/02/17
Added debugging prints

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""
