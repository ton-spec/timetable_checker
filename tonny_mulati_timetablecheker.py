import datetime
import pyttsx3
# Define the timetable dictionary
timetable = {
    "Monday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- HISTORY",
        "9:20  - 9:30 ": "BREAK",
        "9:30  - 10:10 ": "FORM 4",
        "10:10  - 10:50 ": "FORM 1",
        "10:50  - 11:20 ": "FORM 2",
        "11:20  - 12:00 ": "FORM 3",
        "12:00  - 12:40 ": "FORM 4",
        "13:20  - 14:00 ": "FORM 1",
        "14:00  - 14:40 ": "FORM 2",
        "14:40  - 14:50 ": "FORM 3",
        "14:50  - 15:30 ": "FORM 4",
        "15:30  - 16:10 ": "FORM 2",
        "16:10  - 6:00 ": "FORM 3"

    },
    "Tuesday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- MATHS",
        "9:20  - 9:30 ": "BREAK",
        "9:30  - 10:10 ": "FORM 4",
        "10:10  - 10:50 ": "FORM 1",
        "10:50  - 11:20 ": "FORM 2",
        "11:20  - 12:00 ": "FORM 3",
        "12:00  - 12:40 ": "FORM 4",
        "13:20  - 14:00 ": "FORM 1",
        "14:00  - 14:40 ": "FORM 2",
        "14:40  - 14:50 ": "FORM 3",
        "14:50  - 15:30 ": "FORM 4",
        "15:30  - 16:10 ": "FORM 2",
        "16:10  - 6:00 ": "FORM 3"
     
    },
    "Wednesday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": "BREAK",
        "9:30  - 10:10 ": "FORM 4",
        "10:10  - 10:50 ": "FORM 1",
        "10:50  - 11:20 ": "FORM 2",
        "11:20  - 12:00 ": "FORM 3",
        "12:00  - 12:40 ": "FORM 4",
        "13:20  - 14:00 ": "FORM 1",
        "14:00  - 14:40 ": "FORM 2",
        "14:40  - 14:50 ": "FORM 3",
        "14:50  - 15:30 ": "FORM 4",
        "15:30  - 16:10 ": "FORM 2",
        "16:10  - 6:00 ": "FORM 3"
   
    },
    "Thursday": {
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- BIOL0GY",
        "9:20  - 9:30 ": "BREAK",
        "9:30  - 10:10 ": "FORM 4",
        "10:10  - 10:50 ": "FORM 1",
        "10:50  - 11:20 ": "FORM 2",
        "11:20  - 12:00 ": "FORM 3",
        "12:00  - 12:40 ": "FORM 4",
        "13:20  - 14:00 ": "FORM 1",
        "14:00  - 14:40 ": "FORM 2",
        "14:40  - 14:50 ": "FORM 3",
        "14:50  - 15:30 ": "FORM 4",
        "15:30  - 16:10 ": "FORM 2",
        "16:10  - 6:00 ": "FORM 3"   
    },
    "Friday": {
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- AGRICULTURE",
        "9:20  - 9:30 ": "BREAK",
        "9:30  - 10:10 ": "FORM 4",
        "10:10  - 10:50 ": "FORM 1",
        "10:50  - 11:20 ": "FORM 2",
        "11:20  - 12:00 ": "FORM 3",
        "12:00  - 12:40 ": "FORM 4",
        "13:20  - 14:00 ": "FORM 1",
        "14:00  - 14:40 ": "FORM 2",
        "14:40  - 14:50 ": "FORM 3",
        "14:50  - 15:30 ": "FORM 4",
        "15:30  - 16:10 ": "FORM 2",
        "16:10  - 6:00 ": "FORM 3" 
    }
}

now = datetime.datetime.now()
k = now.strftime("%H:%M")

def sing():
    engine = pyttsx3.init()
    engine.say("Thank you!")
    engine.runAndWait()




# Get user input for the current day


dey =input("Enter the current day's name. eg, Monday: ")

# Loop through the timetable to find the matching class
for day, classes in timetable.items():
    if day == dey:
        for time_range, class_name in classes.items():
            start_time, end_time = time_range.split(" - ")
            if start_time <= k <= end_time:
                print(f"On {day}, you have {class_name} from {time_range}.")
                sing()
                break