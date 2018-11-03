#! python3
#the following program is my very first Python program
#installation #sudo zypper install python3-xlib
#sudo pip install keyboard
#cd ~/Documents/Code/Python/DesktopAssistant / xhost +
def exiting():
    print('Exiting')
import sys
def type_unicode(word):
    for c in word:
        c = '%04x' % ord(c)
        import pyautogui
        pyautogui.keyDown('optionleft')
        pyautogui.typewrite(c)
        pyautogui.keyUp('optionleft')
def main():
    try:
        import getpass
        import os
        import shelve
        import pyautogui
        import keyboard
        import pytesseract
        import time
        pyautogui.FAILSAFE = True
        from sys import platform
        OS_environment=os.environ['XDG_CURRENT_DESKTOP'].lower()
        if not sys.platform.startswith('linux'):
            print('ERROR! ' +platform + ', ' + OS_environment + ' host detected! This code will only run on a Linux a platform with GNOME!')
            exiting()
            sys.exit(1)
        else:
            if OS_environment!='gnome':
                print('ERROR! ' +platform + ', ' + OS_environment + ' host detected! This code will only run on a Linux a platform with GNOME!')
                exiting()
                sys.exit(1)
            else:
                # OS X
                print('SUCCESS! ' +platform + ' host with ' + OS_environment + ' DE detected! This code only executes on a Linux a platform with GNOME! Execution may continue')
                print('Welcome, ' + getpass.getuser())
        print('The current working directory: ' + os.getcwd())
        print('Initiating application')
        #the master file index should contain all the subsequent tables iT might need
        MasterDataIndex="PythonMasterDataIndex.csv"
        if  os.path.isfile(MasterDataIndex):
            print('SUCCESS: The MasterDataIndex file "' + MasterDataIndex +'" was FOUND in the working directory.')
        else:
            print('ERROR: The MasterDataIndex file "' + MasterDataIndex +'" was NOT FOUND in the working directory.')
            exiting()
            sys.exit(1)
        MemoryFolder="Memory"
        if  os.path.isdir(MemoryFolder):
            print('SUCCESS: The "' + MemoryFolder +'" was FOUND in the working directory.')

        else:
            print('ERROR: The  Memory folder "' + MemoryFolder +'" was NOT FOUND in the working directory.')
            exiting()
            sys.exit(1)
        screenwidth,screenheight=pyautogui.size()
        print("INFO: The screensize is: {} x {}".format(screenwidth,screenheight))
        # im = pyautogui.screenshot()
        # text = pytesseract.image_to_string(im)
        # print (text)
        # shelfFile = shelve.open('mydata')
        # sonnetFile = open(MasterDataIndex)
        # print(sonnetFile.readlines())
        # shelfFile.close()
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        #from selenium import webdriver
        #browser= webdriver.Firefox()
        #browser.get("http://google.com/ncr")
        #pyautogui.typewrite('Hello world!')
        #xpyautogui.press('enter')
        #pyautogui.scroll(200)
        #time.sleep(10)
        #browser.close()
        pyautogui.press('apps')
        pyautogui.typewrite('firefox')
        print('attempting to locate the firefox.png')
        coords=pyautogui.locateCenterOnScreen('firefox.png',grayscale=True)
        print(coords)
        pyautogui.rightClick(coords)
        coords=pyautogui.locateCenterOnScreen('NewWindow.png',grayscale=True,minSearchTime=10)

        if coords is None:
            pyautogui.rightClick()
            pyautogui.press('apps')
            raise Exception('Failed to find image "NewWindow.png" on the screen. Exiting')
        print('SUCCESS: The NewWindow.png \'s coordinates are:',coords)
        pyautogui.click(coords)
        time.sleep(10)
        coords=pyautogui.locateCenterOnScreen('https.png',grayscale=True,minSearchTime=10)
        if coords is None:
            pyautogui.rightClick()
            pyautogui.press('apps')
            raise Exception('ERROR:Failed to find image "https.png" on the screen. Exiting')
        print('SUCCESS: The https.png \'s coordinates are:',coords)
        pyautogui.doubleClick(coords)
        import pyperclip
        pyperclip.copy(R"http://www.mnb.hu/Jegybanki_alapkamat_alakulasa")
        #type_unicode("http://www.mnb.hu/Jegybanki_alapkamat_alakulasa")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        time.sleep(10)
        coords=pyautogui.locateCenterOnScreen('AlapKamatLekerese.png',grayscale=True,minSearchTime=10)
        if coords is None:
            raise Exception('ERROR:Failed to find image "AlapKamatLekerese.png" on the screen. Exiting')
        print('SUCCESS: The AlapKamatLekerese.png \'s coordinates are:',coords)

        pyautogui.press('apps')
        time.sleep(10)
        print("The execution had been completed")
    except Exception as err:
        print('An exception happened: ', sys.exc_info()[:3])

if __name__ == '__main__':
    main()
    sys.exit(0)
