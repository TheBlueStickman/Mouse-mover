import pyautogui, time, keyboard

time.sleep(1)

seconds = 1

# function for checking if ESC is being pressed, if it is pressed it returns True else it is False
def checkEsc():
    exit = False
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Breaking the loop.")
        exit = True
    return exit

# function that while counting to the amount of seconds (not fully accurate amount of time) also keeps checking if ESC is being pressed or no
# according to that it returns True or False
def waitAndCheck():
    exit = False
    countdown = 0
    while countdown <= seconds:
        if checkEsc() == True:
            exit = True
            break
        else:
            time.sleep(0.01)
            countdown += 0.01
    return exit


while (True):
    # If the waitAndCheck function returns True, ESC was pressed, so it will break out of the main loop, ending the program.
    # Else move to the specified point
    if waitAndCheck() == True:
        break
    pyautogui.moveTo(750, 350)

    if waitAndCheck() == True:
        break
    pyautogui.moveTo(950, 350)
   
    if waitAndCheck() == True:
        break
    pyautogui.moveTo(950, 550)

    if waitAndCheck() == True:
        break
    pyautogui.moveTo(750, 550)