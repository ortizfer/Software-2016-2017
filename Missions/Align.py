from Missions import Movement

x = 0
y = 0
def start(yaw,pitch):
    x = yaw #Movement.getAngle("yaw");
    y = pitch #Movement.getAngle("pitch");
    distance = Movement.getDistance();
    centered = False;

    while not centered() :
        if(y > 200):
            print()
            #
        elif(y <= -50):
            print()
            y = Movement.moveUp(y);
        if(x >= 50):
            print()
            x = Movement.moveLeft(x)
        elif (x <= -50) :
            print()
            x = Movement.moveRight(x)
        print("x = {}".format(x));
        print("y = {}".format(y));

def centered():
    if x < 200 or x > 300:
        return False
    if y < 100 or y > 200:
        return False
    else:
        return True



"""
VERSION CONTROL:
2- Felix Gonzalez 8/03/2017 1:23pm
Tested functionality and improved time of execution.

1- Fernando Ortiz 2/03/17
Creation of version Control and print

"""
