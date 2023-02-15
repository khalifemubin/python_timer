import time
from pynput import keyboard

timer = 0
bResume = False
bKeepRunningProgram = True

print("Press s to Start")
print("Press p to Pause")
print("Press r to Resume")
print("Press e to End")

def convertSecondsToTime(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%02d:%02d:%02d" % (hour, minutes, seconds)

def start_timer():
    global bResume
    bResume=True

def pause_timer():
    global bResume
    print('\nTimer Paused\n')
    bResume=False

def resume_timer():
    global bResume
    print('\nTimer Resumed \n')
    bResume=True

def quit():
    global bResume,bKeepRunningProgram
    print('\nTimer Stopped\n')
    bResume=False
    print(f"\nTime elapsed - {convertSecondsToTime(timer)}")
    # sys.exit()
    bKeepRunningProgram=False

def on_press(key):
    # the timer will reset if a key is pressed
    # global timer
    # timer = 0
    if key.char == 's':
        start_timer()
    elif key.char == 'p':
        pause_timer()
    elif key.char == 'r':
        resume_timer()
    elif key.char == 'e' or key.char == 'q':
        quit()
    elif key == Key.esc:
        quit()

# Collecting events
listener = keyboard.Listener(on_press=on_press,suppress=True)
listener.start()

while bKeepRunningProgram:
    while bResume:
        print(f"{convertSecondsToTime(timer)}")
        # print(timer)
        time.sleep(1)
        timer+=1
