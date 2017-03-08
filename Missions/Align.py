from Missions import Movement

def start(yaw,pitch):
    x = yaw #Movement.getAngle("yaw");
    y = pitch #Movement.getAngle("pitch");
    distance = Movement.getDistance();
    centered = False;

    while(centered != True) :
        if(x > -50 and x < 50 ) :
            if(y > -50 and y < 50 ) :
                centered = True
        if(y >= 50):
            print()
            y = Movement.moveDown(y);
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


"""
VERSION CONTROL:
2- Felix Gonzalez 8/03/2017 1:23pm
Tested functionality and improved time of execution.

1- Fernando Ortiz 2/03/17
Creation of version Control and print

"""
