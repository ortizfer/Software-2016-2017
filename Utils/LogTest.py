from Utils import Log
import time
sleep = 1


Log.Logging.createLogs()
print("System Log")

time.sleep(sleep)
Log.Logging.logSys("Starting")
time.sleep(sleep)
Log.Logging.logSys("gate1")
time.sleep(sleep)
Log.Logging.logSys("Spinning")
time.sleep(sleep)
Log.Logging.logSys("Boba Fett")
time.sleep(sleep)
Log.Logging.logSys("Stopping")
time.sleep(sleep)
Log.Logging.logSys("Surfacing")
time.sleep(sleep)
Log.Logging.logSys("Stopping")
time.sleep(sleep)
Log.Logging.logSys("Shutting down")
time.sleep(sleep)

print("Error Log")
Log.Logging.logErr("Critical meltdown")
time.sleep(sleep)
Log.Logging.logErr("Motor failure")
time.sleep(sleep)
Log.Logging.logErr("AI turned evil")
time.sleep(sleep)
Log.Logging.logErr("Cabin leak")
time.sleep(sleep)
Log.Logging.logErr("Engaging killswitch")
time.sleep(sleep)
Log.Logging.logErr("Killswitch on fire")
time.sleep(sleep)

print("Navigation Log")
Log.Logging.logNav("Starting")
time.sleep(sleep)
Log.Logging.logNav("Moving forward")
time.sleep(sleep)
Log.Logging.logNav("Full speed ahead")
time.sleep(sleep)
Log.Logging.logNav("Stopping")
time.sleep(sleep)
Log.Logging.logNav("Submerging to 10")
time.sleep(sleep)
Log.Logging.logNav("Rotate 45")
time.sleep(sleep)
Log.Logging.logNav("Backward 10%")
time.sleep(sleep)
Log.Logging.logNav("Stopping")
time.sleep(sleep)
Log.Logging.logNav("Surfacing")
time.sleep(sleep)
Log.Logging.logNav("Run Complete!")
time.sleep(sleep)
Log.Logging.logNav("Shutting down")
