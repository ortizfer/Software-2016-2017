# Software-2016-2017
Code for Proteus 2.0 Missions

"""
31- Juan G. Lastra Febles 10/05/2017 7:18 PM
Documented the Line.py and the Searching.py

30- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 7:02 PM
Documented the Cleanup and moved the file to Utils. Documented the Buoy.py, documented the Directon.py, documented the
Gate1.py, documented Gate2.py, documented Island.py

29- Juan G. Lastra Febles and Carlos Figueroa  10/05/2017 5:46 PM
Edited the Documentation of the Movement.py and the CenterPath.py

28- Juan G. Lastra Febles, Carlos Figueroa and Jose Montes 10/05/2017  3:58 pm
Commented on the Align code and Hydrophone

27- Juan G. Lastra Febles 10/05/2017 3:01 PM
Documented the movement code

26 -Juan G.Lastra and Estaban Lopez 1/04/2017 6:10 P.M
Alterated the forward, badkward and stop functions and eliminated forward a and backward a.

25- Fernando Ortiz 27/03/2017 3:00PM
Added first vision codes for further integration with missions

24- Fernando Ortiz 14/03/2017 10:52am
fixed path for logs on multiple OS

23- Juan G. Lastra Febles 14/03/2017 9.16 a.m
Add documentation the program log and use a print function in the lof functions.

22- Carlos J. Figueroa 11/03/2017 9:15pm
Modified Log and Timer to use better visually pleasing dateTime formats.

21- Carlos J. Figueroa 11/03/2017 8:46pm
Modified Logs and Timer, functioning as intended.
Modified all files calling the log to use the new
functions properly.

20- Fernando Ortiz 02/03/2017 9:35AM
Organized Documents in folders and fixed imports in all classes

19- Carlos J. Figueroa 01/03/2017 11:59pm
Added System Logs calls, as well as necessary imports to:
Main.py, Line.py, Gate1.py, and Gate2.py. Added datetime
to log entries in Log.py. Needs more work:
Duplicates files, incorrect formatting, dummy files

18- Carlos J. Figueroa 01/03/2017 10:51pm
Initial commit for Log.py
Imported Log and created logs in Main.py
Modified Timer to better aid Log.py
Calls broken, not commiting yet.

17- Carlos J. Figueroa 01/03/2017 7:04pm
Added a submersion check at Movement.py, used as
part of diagnostics in HealthTest.py

16- Carlos J. Figueroa 01/03/2017 6:48pm
Modified the HealthTest.py IMU and PSENSE diagnostics.
Added at SerialCom.py write methods for IMU and PSENSE.

15- Carlos J. Figueroa 28/02/2017 11:55am
Implemented HealthTest.py

14- Carlos J. Figueroa 28/02/2017 11:13am
Added specific commands to SerialCom.py

13- Sachy Romero 27/02/2017 12:28pm
Added Maxrange X and Maxrange Y

21- Carlos J. Figueroa 23/02/2017 5:04pm
Added basic documentation for Buoy.py

20- Carlos J. Figueroa 23/02/2017 4:42pm
Added basic some documentation for Main.py

19- Carlos J. Figueroa 23/02/2017 4:28pm
Added basic documentation for SerialCom.py

18- Carlos J. Figueroa 23/02/2017 4:00pm
Implemented do_magic() at Movement.py

17 - Esteban 22/02/17
Island code implementation

16- Fernando Ortiz 22/02/17 5:47PM
FUnction left and right added in movement

15- Sachy Romero 22/02/2017 5:38pm
Exit algorithm and pass between the Buoys

14- Sachy Romero 22/02/2017 5:38pm
Touch Green Buoy

13- Sachy Romero 22/02/2017 5:38pm
Aligned with Green Buoy

12- Sachy Romero 22/02/2017 5:38pm
Moved backward to align with green Buoy

11- Sachy Romero Rosado 22/02/2017 5:38pm
Touch Red Buoy

10- Sachy Romero 22/02/2017 5:38pm
Aligned to Red Buoy

9- Carlos J. Figueroa 22/02/2017 5:30pm
Created function listen() at hydrophone and imported it to movement.

8-Fernando Ortiz 22/02/17 4:54PM
created additional functions listen and bop_it for logic on missions

7- Carlos J. Figueroa 22/02/2017 4:31pm
Modified Timer class, removed redundant methods and properties.

6- Carlos J. Figueroa 22/02/2017 4:15pm
Added Timer metaclass to project.

5- Sachy Romero 21/02/17 4:25PM
Added boolean variable for Buoy mission

4- Fernando Ortiz 21/02/17 11:09AM
Documentation and implementation of Gate2 mission logic

3- Fernando Ortiz 20/02/17 8:05PM
Creation of SerialCom and Direction files, further implementation of gate1, line, main and movement files

2- Fernando Ortiz 19/02/17 9:20AM
Creation of main and movement files and implementation of gate1

1- Fernando Ortiz 17/02/17 8:45PM
Initial Commit and creation of class.


"""
