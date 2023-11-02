from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Automaps:
    def __init__(self):
        self.driver = self.launch_gmaps()

    def clear_searchbar(self):
        clear_button = self.driver.find_element(By.CSS_SELECTOR, "#searchbox > div.lSDxNd > button")
        clear_button.click()

    def launch_gmaps(self):
        # Chrome options to load signed-in chrome profile
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\") # Opens chrome profile
        #chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_experimental_option("detach", True)

        driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu")
        print( driver.title)

        # wait for webpage to load completely
        driver.implicitly_wait(10)
        return driver

    def enter_address(self, address):
        # Searchbar element
        textbox = self.driver.find_element(By.ID, "searchboxinput") # or XmI62e for the form itself
        # Input address into searchbox , add petah tikva prefix to each local address
        textbox.send_keys(" פתח תקווה " +"שפרינצק 7")
        textbox.send_keys(Keys.ENTER)

    # Generalize this method to take list name as string and integrate in xpath search or by name
    def save_to_list(self): #def save_to_list(driver, locations_list):
        button = self.driver.find_element(By.CSS_SELECTOR, "#QA0Szd>div>div>div.w6VYqd>div.bJzME.tTVLSc>div>div.e07Vkf.kA9KIf>div>div>div.m6QErb.Pf6ghf.ecceSd.tLjsW>div:nth-child(2)>button")
        button.click()
        bombSheltersList = self.driver.find_element(By.CSS_SELECTOR, "#fDahXd div:nth-of-type(6)")
        bombSheltersList.click()

def main():
    auto = Automaps()
    #driver = launch_gmaps()
    
    for address in range(1):
        auto.enter_address(address)

        # Click "save" button (opens save-dropdown menu)
        auto.save_to_list()
        # Save location in "bombshelters" (or other name) list

        # Clear searchbox
        #clear_searchbar(driver)
        
if __name__ == "__main__":
    main()
#drive.quit() #if the page opens but no action is taken(it freezes) it means the page's already open/in use elsewhere!
