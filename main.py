import pyautogui, time, keyboard 
 
time.sleep(1) 
 
# left corner Point(x=734, y=354) 
# right corner Point(x=959, y=350) 
#right down Point(x=960, y=579) 
#left down Point(x=731, y=582) 
 
programRun = True 
 
seconds = 1 
 
def checkEsc(): 
    exit = False 
    if keyboard.is_pressed('esc'): 
        print("ESC pressed. Breaking the loop.") 
        exit = True 
    return exit 
 
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
 
 
 
while (programRun): 
    if waitAndCheck() == True: 
        programRun = False 
 
 
    pyautogui.moveTo(750, 350) 
 
#    while countdown >= seconds: 
#        countdown = 0 
 #       if checkEsc() == True: 
 #           break 
 #       else: 
   #         time.sleep(0.01) 
  #          countdown += 0.01 
   #     programRun = False 
 
 
    if waitAndCheck() == True: 
        programRun = False 
 
 
    pyautogui.moveTo(950, 350) 
     
    
    if waitAndCheck() == True: 
        programRun = False 
 
    pyautogui.moveTo(950, 550) 
 
    if waitAndCheck() == True: 
        programRun = False 
 
    pyautogui.moveTo(750, 550) 
 
     
