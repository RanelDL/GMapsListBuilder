from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import tkinter as tk
from tkinter import filedialog

class Automaps:

    def __init__(self, url):
        self.url = url
        self.USER_DATA_PATH = self.set_chrome_user_path()
        self.driver = self.launch_page()

    def set_chrome_user_path(self):
        # open txt file
        path = ""
        try:
            with open("ChromeUserPath.txt", 'a+') as file:
                pos = file.tell()
                # if txt file not empty: read file contents as path
                if  pos != 0:
                    file.seek(0,0) # opened in append mode, cursor has to be reset
                    path = file.readline() 

                # empty, open file explorer 
                else: 
                    root = tk.Tk()
                    root.withdraw()
                    path = filedialog.askdirectory()
                    file.write(path)
        except Exception as e:
            print( "error opening path file: ", e)    

        return path
        
    def clear_searchbar(self):
        clear_button = self.driver.find_element(By.CSS_SELECTOR, "#searchbox > div.lSDxNd > button")
        clear_button.click()

    def launch_page(self):
        # Chrome options to load signed-in chrome profile
        chrome_options = Options()
        # Path should be something like:
        # "C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data\\") # Opens chrome profile
        chrome_options.add_argument("--user-data-dir=" + self.USER_DATA_PATH) 
        chrome_options.add_experimental_option("detach", True)

        driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(self.url)
        print( driver.title)

        # wait for webpage to load completely
        driver.implicitly_wait(3)
        return driver

    def enter_address(self, address):
        # Searchbar element
        textbox = self.driver.find_element(By.ID, "searchboxinput")
        textbox.send_keys( address )
        textbox.send_keys(Keys.ENTER)

    def save_to_list(self, listName): 
        button = self.driver.find_element(By.CSS_SELECTOR, "#QA0Szd>div>div>div.w6VYqd>div.bJzME.tTVLSc>div>div.e07Vkf.kA9KIf>div>div>div.m6QErb.Pf6ghf.ecceSd.tLjsW>div:nth-child(2)>button")
        button.click()
        bombSheltersList = self.driver.find_element(By.XPATH,"//div[.='" + listName + "']")
        bombSheltersList.click()

    def add_note(self, note):
        button = self.driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(7) > div > div.m6QErb.Duzcee > div.m6QErb.tLjsW > div:nth-child(1) > button > div")
        button.click()
        textbox = self.driver.find_element(By.CSS_SELECTOR, "#modal-dialog > div > div.hoUMge > div > div.yFnP6d > div > div > div.Xsdp7b > textarea")
        textbox.send_keys(note)
        doneButton = self.driver.find_element(By.CSS_SELECTOR, "#modal-dialog > div > div.hoUMge > div > div.yFnP6d > div > div > div.vV6Pxc > div.LKVNAb > button.okDpye.PpaGLb.mta2Ab")
        doneButton.click()

def main():
    pass
if __name__ == "__main__":
    main()
#drive.quit() #if the page opens but no action is taken(it freezes) it means the page's already open/in use elsewhere!
