# Searchin Algorithm
from Missions import Movement
from Vision import FrameGrab
from Vision import AngleTest

def start():

    object = 0;
def Search():
    counter = 0

    while counter < 2:

        Movement.align(45)  # Gira hacia la derecha y toma foto para buscar alguna boya.
        FrameGrab.frontFrame()# Toma foto de Vision

        if (AngleTest.sendX()>0): #Identificó un objeto, sigue corriendo el codigo.
            return 0

        Movement.align(-90) #Si no identifica objeto hacia la derecha, rota hacia la izquierda y repite el proceso.
        FrameGrab.frontFrame()

        if (AngleTest.sendX()>0):
            return 0

        Movement.align(45) # Regresa al punto inicial

        Movement.backward(2) # Retrocede dos segundos y entra otra vez al loop hasta que se cumpla las condiciones.
        counter= counter +1 # De no encontrar boya vuelve a entrar al while hasta 2 veces.

    Movement.rotate() #De correr dos veces y no enoontrar objeto comienza a rotar para recuperarse



"""
VERSION CONTROL:

4- Sachy Romero Rosado 02/04/2017 1:55am
Called Movement.backward to go back 2 seconds after each iteration.

3. Sachy Romero Rosado 02/04/2017 1:38am
Rotate in case that after the iterations, the bouys are not found.

2. Sachy Romero Rosado 02/04/2017 1:37am
Created a counter loop to run the code 2 times to check if it finds the buoy

1. Sachy Romero Rosado 02/04/2017  1:19am
Implementario of moving right and left






    """














