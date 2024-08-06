import time
import datetime
import pyttsx3
from win10toast import ToastNotifier

# Variables
toast = ToastNotifier()
engine = pyttsx3.init()
index = 1
total_water = 1000     # To set the Total water you want to drink in milliliter
you_can_drink = 500     # To set the water you can to drink at a time in milliliter
reminder_skip = 0            
Reminder_time = 2       # To set the time in seconds

#Functions
def notification():
      toast.show_toast(      
    "Water Reminder",
    "Please drink water and take care of your health.",
    duration = 10,
    # icon_path = "icon.ico",
    threaded = True,
    )
      
def voice(VO):
    engine.say(VO)    
    engine.runAndWait()

def logFile(write):
    with open("Projects/Healthy_Programmer_Project/Pulit_Drink_log.txt","a") as p:
        p.write(write)



logFile(f"\nTotal water to drink {total_water} times.\n")
while True:
    time.sleep(Reminder_time)

    if total_water == 0:
            break 
    # Terminal Text
    print("\nPlease drink water and take care of your health.")
    
    #Notification
    notification()
  
    # Voice
    voice("Hello Pulkit! Please drink water and take care of your health.")
    
    # User Input
    user_input = input("Press D to Drink or DE to not Drink or e to exit the program: ").lower()
    while user_input not in ["d","dn","e"]:
        user_input = input("Press D if you drink it or e to exit the program: ").lower()

# to Quit 
    if user_input == "e":
        break

# if drink
    elif user_input == "d":
        logFile(f"{index}: Drank water at {datetime.datetime.now()}\
                    \nRemining water {total_water-you_can_drink}\n")
        index += 1   
        total_water -= you_can_drink
        continue

# Doesn't drink
    elif user_input == "dn":
        logFile(f"{index}: Didn't drink water {datetime.datetime.now()}\
                    \nRemining water {total_water}\n")
        index += 1
        reminder_skip += 1 
        continue

logFile(f"You skipped {reminder_skip} times.\n")
voice("Hello Pulkit! Your daily water goal is complete.")















