import pyautogui, time, keyboard

time.sleep(1)

left corner Point(x=734, y=354)
right corner Point(x=959, y=350)

#right down Point(x=960, y=579)
#left down Point(x=731, y=582)

programRun = True

def checkEsc():
if keyboard.is_pressed('esc'):
print("ESC pressed. Breaking the loop.")

while (programRun):

if keyboard.is_pressed('esc'):
    print("ESC pressed. Breaking the loop.")
    programRun = False

if checkEsc() == True:
    programRun == False



pyautogui.moveTo(730, 350)
time.sleep(1)

if checkEsc() == True:
    break    


pyautogui.moveTo(960, 350)
time.sleep(1)

pyautogui.moveTo(960, 580)
time.sleep(1)

pyautogui.moveTo(730, 580)
time.sleep(1)