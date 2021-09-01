import os
import pandas as pd 
import pyautogui 
import time

"""
This program was prepared by Enis KÜÇÜKKÖSE.
The only conditions that may vary from device to device are program opening and response times.
"""

class Sendmessage():

    def __init__(self):
        self.df= pd.read_excel("namesandphones.xls")
        self.names=list(self.df["Names"])
        self.start_wp()
        self.send()

    def start_wp(self):
        os.startfile(r"C:\Users\enisk\Desktop\MASAÜSTÜM\WhatsApp")
        time.sleep(2)

    def send(self):
        for i in self.names:
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(0.2)
            pyautogui.write(str(i), interval=0.01)
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.write("Telefon numaram degisti.Yeni numaram: '+90(5**)(***)**-**' ", interval=0.01)
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(0.2)


Sendmessage()




