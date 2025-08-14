import time
import pyautogui
import keyboard
import sys
active=True
targets=0

def checkScreen():#takes about 363ms to clear the test
    #needs optimization
    #either use numpy or use a while so the lookup is faster
    global active
    global targets
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
            for x in range(width):#this shit is the bottleneck
                for y in range(height):#i should convert the pixel array onto a vector and use numpy to do matrix calculations
                    if pixel[x,y]==(149,195,232):
                            pyautogui.moveTo(486+x,181+y)
                            pyautogui.click(button="left",clicks=1)
                            found=True
                            break
                if(found):
                    targets+=1
                    break
                if(targets==32):#32 because otherwise it ends 2 targets early
                    sys.exit()

                        
                    

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("script has been stopped")



checkScreen() 