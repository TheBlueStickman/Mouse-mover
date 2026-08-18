import pyautogui, time, keyboard

time.sleep(1)

# left corner Point(x=734, y=354)
# right corner Point(x=959, y=350)
#right down Point(x=960, y=579)
#left down Point(x=731, y=582)

programRun = True

def checkEsc():
    exit = False
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Breaking the loop.")
        exit = True
    return exit

def couunt():
    while countdown >= seconds:
        if checkEsc() == True:
            break
        else:
            time.sleep(0.01)
            countdown += 0.01
        programRun = False

seconds = 1

countdown = 0

while (programRun):
    if checkEsc() == True:
        programRun = False

    pyautogui.moveTo(750, 350)

    while countdown >= seconds:
        if checkEsc() == True:
            break
        else:
            time.sleep(0.01)
            countdown += 0.01
        programRun = False

    if checkEsc() == True:
        programRun = False

    pyautogui.moveTo(950, 350)
    time.sleep(seconds)

    if checkEsc() == True:
        programRun = False

    pyautogui.moveTo(950, 550)
    time.sleep(seconds)

    if checkEsc() == True:
        programRun = False

    pyautogui.moveTo(750, 550)
    time.sleep(seconds)
    
    if checkEsc() == True:
        programRun = False

somethign like this?