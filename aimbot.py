import time
import pyautogui
import keyboard
active=True


def checkScreen():#takes about 363ms to clear the test
    #needs optimization
    #either use numpy or use a while so the lookup is faster
    global active
    try:
        while(active):
            found=False
            #print(str(pyautogui.position()))
            regionScreenshot = pyautogui.screenshot(region=(476, 180, 979, 429))#screenshoot the blue thing
            width,height=regionScreenshot.size
            if(not active):
                break
            if(keyboard.is_pressed('esc')):
                    active=False
                    print("script has been stopped")
                    break
            pixel=regionScreenshot.load()
            for x in range(width):
                for y in range(height):
                    if pixel[x,y]==(149,195,232):
                            pyautogui.moveTo(486+x,181+y)
                            pyautogui.click(button="left",clicks=1)
                            found=True
                            break
                if(found):
                    break

                        
                    

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("script has been stopped")



checkScreen() 