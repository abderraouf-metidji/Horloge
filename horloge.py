import time
import datetime

current_time = None
alarm_time = None
time_format = "24" # "12" or "24"

def set_time(new_time):
    global current_time
    current_time = new_time

def set_alarm(new_alarm):
    global alarm_time
    alarm_time = new_alarm

def set_time_format(new_format):
    global time_format
    time_format = new_format


def display_time():
    while True:
        global current_time
        if current_time is None:
            current_time = datetime.datetime.now().time()
            current_time = (current_time.hour, current_time.minute, current_time.second)
        if time_format == "12":
            hour = current_time[0] % 12
            if hour == 0:
                hour = 12
            am_pm = "AM" if current_time[0] < 12 else "PM"
            print(f"{hour:02d}:{current_time[1]:02d}:{current_time[2]:02d} {am_pm}")
            current_time = (current_time[0], current_time[1], current_time[2] + 1)
            if current_time[2] == 60:
                current_time = (current_time[0], current_time[1] + 1, 0)
            if current_time[1] == 60:
                current_time = (current_time[0] + 1, 0, 0)
            if current_time[0] == 24:
                current_time = (0, 0, 0)
        else:
            print(f"{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}")
            current_time = (current_time[0], current_time[1], current_time[2] + 1)
            if current_time[2] == 60:
                current_time = (current_time[0], current_time[1] + 1, 0)
            if current_time[1] == 60:
                current_time = (current_time[0] + 1, 0, 0)
            if current_time[0] == 24:
                current_time = (0, 0, 0)
            if alarm_time is not None and current_time == alarm_time:
                print("Alarm!")
        time.sleep(1)

display_time()