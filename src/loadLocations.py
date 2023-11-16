from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Automaps:

    def __init__(self, url):
        self.url = url
        self.driver = self.launch_page()

    def clear_searchbar(self):
        clear_button = self.driver.find_element(By.CSS_SELECTOR, "#searchbox > div.lSDxNd > button")
        clear_button.click()

    def launch_page(self):
        # Chrome options to load signed-in chrome profile
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\") # Opens chrome profile
        #chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_experimental_option("detach", True)

        driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(self.url)
        print( driver.title)

        # wait for webpage to load completely
        driver.implicitly_wait(3)
        return driver

    def enter_address(self, address):
        # Searchbar element
        textbox = self.driver.find_element(By.ID, "searchboxinput") # or XmI62e for the form itself
        # Input address into searchbox , add petah tikva prefix to each local address
        textbox.send_keys("פתח תקווה," + address )#text)#address + " פתח תקווה ")
        textbox.send_keys(Keys.ENTER)

    def save_to_list(self, listName): 
        button = self.driver.find_element(By.CSS_SELECTOR, "#QA0Szd>div>div>div.w6VYqd>div.bJzME.tTVLSc>div>div.e07Vkf.kA9KIf>div>div>div.m6QErb.Pf6ghf.ecceSd.tLjsW>div:nth-child(2)>button")
        foo = "Bouldering"
        button.click()
        # bombSheltersList = self.driver.find_element(By.CSS_SELECTOR, "#fDahXd div:nth-of-type(6)") # this just saves to the 6th indexed list in the dropdown menu
        # bombSheltersList = self.driver.find_element(By.XPATH,"//div[text()='" + foo + "']") # why does this xpath leads to error: Message:elemnt click intercepted:... 
        # ... Other element would receive the click: ...
        bombSheltersList = self.driver.find_element(By.XPATH,"//div[.='" + foo + "']")
        bombSheltersList.click()
    def add_note(self, note):
        button = self.driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(7) > div > div.m6QErb.Duzcee > div.m6QErb.tLjsW > div:nth-child(1) > button > div")
        button.click()
        textbox = self.driver.find_element(By.CSS_SELECTOR, "#modal-dialog > div > div.hoUMge > div > div.yFnP6d > div > div > div.Xsdp7b > textarea")
        textbox.send_keys(note)
        doneButton = self.driver.find_element(By.CSS_SELECTOR, "#modal-dialog > div > div.hoUMge > div > div.yFnP6d > div > div > div.vV6Pxc > div.LKVNAb > button.okDpye.PpaGLb.mta2Ab")
        doneButton.click()

def main():
    GMAPS_URL ="https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu" 
    auto = Automaps(GMAPS_URL)
    LIST_NAME = ""
    '''
    #driver = launch_gmaps()
    # with open("addresses_wrk_cpy.txt", 'rt') as ADDR_FILE:
    notes = open("notes.txt",'rt')
    with open("testfile.txt", 'rt') as ADDR_FILE:
        for address in ADDR_FILE:

            note = notes.readline()
            
            auto.enter_address(address)

            # Click "save" button (opens save-dropdown menu) & save to 'bombshelters' list
            time.sleep(1)
            try:
                # adding notes modification:
                # auto.save_to_list(LIST_NAME)
                auto.add_note(note)

            except Exception as e:
                print(e, " coudn't add: " + address)
            time.sleep(1) 
            # Clear searchbox
            auto.clear_searchbar()
    '''
    auto.enter_address("orlife")
    time.sleep(2)
    try:
        auto.save_to_list()
    except Exception as e:
        print(e)
    time.sleep(4)
    auto.driver.quit()
    # notes.close()
if __name__ == "__main__":
    main()
#drive.quit() #if the page opens but no action is taken(it freezes) it means the page's already open/in use elsewhere!
