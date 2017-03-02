from Missions import Movement

def start():
    x = Movement.getAngle("yaw");
    y = Movement.getAngle("pitch");
    distance = Movement.getDistance();
    centered = False;

    while(centered != True) :
        if(x > -50 and x < 50 ) :
            if(y > -50 and y < 50 ) :
                centered = True
            elif(y > 0):
                print()
                #Movement.moveUp();
            else:
                print()
                #Movement.moveDown();
        elif(x > 0):
            print()
            #Movement.moveLeft()
        else :
            print()
            #Movement.moveRight()
    print()

"""
VERSION CONTROL:
1- Fernando Ortiz 2/03/17
Creation of version Control and print

"""
