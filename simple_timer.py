import time
import threading
import sys
# import getpass
import os
import platform

timer = 0
bResume = False
bKeepRunningProgram = True
bAlreadyStarted=False

print("Input s and Press enter to Start")
print("Input p and Press enter to Pause")
print("Input r and Press enter to Resume")
print("Input e and Press enter to End")

def background():
    global bResume,timer
    while bResume:
        print(f"{convertSecondsToTime(timer)}")
        time.sleep(1)
        timer+=1

def convertSecondsToTime(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%02d:%02d:%02d" % (hour, minutes, seconds)

def start_timer():
    global bResume,bAlreadyStarted
    if(not bAlreadyStarted):
        print('\nTimer Started\n')
        bResume=True
        threading.Thread(target=background).start()
        bAlreadyStarted=True

def pause_timer():
    global bResume
    print('\nTimer Paused\n')
    print(f"{convertSecondsToTime(timer)}")
    bResume=False

def resume_timer():
    global bResume
    print('\nTimer Resumed \n')
    bResume=True
    threading.Thread(target=background).start()

def quit():
    global timer,bResume
    print('\nTimer Stopped\n')
    bResume=False
    print(f"Time elapsed - {convertSecondsToTime(timer)}")
    sys.exit()

while True:
    inp = input()

    #Hack to not display user input in the console
    # inp = getpass.getpass(input(), stream = None)
    if(platform.platform().find("Linux") or platform.platform().find("mac")):
        os.system('clear')
    else:
        os.system('cls')

    if inp == 's':
        start_timer()
    elif inp == 'p':
        pause_timer()
    elif inp == 'r':
        resume_timer()
    elif inp == 'e' or inp == 'q':
        quit()
