from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.actions.action_builder import ActionBuilder
def launch_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\") #Opens my profile by freezes
    #chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_experimental_option("detach", True)

    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu")
    print( driver.title)
    driver.implicitly_wait(10)
    textbox = driver.find_element(By.ID, "searchboxinput") # or XmI62e for the form itself
    #add petah tikva prefix to each local address
    #textbox.send_keys(" פתח תקווה " +"רוטשילד 9")
    textbox.send_keys(" פתח תקווה " +"שפרינצק 7")
    textbox.send_keys(Keys.ENTER)
    #                                                   #QA1Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.Pf6ghf.ecceSd.tLjsW > div:nth-child(2) > button
    button = driver.find_element(By.CSS_SELECTOR, "#QA0Szd>div>div>div.w6VYqd>div.bJzME.tTVLSc>div>div.e07Vkf.kA9KIf>div>div>div.m6QErb.Pf6ghf.ecceSd.tLjsW>div:nth-child(2)>button")
     
    #button.click()
    actions = ActionChains(driver)
    actions.click(on_element=button).pause(1)
    driver.implicitly_wait(1)
    #for _ in range(5):
        #button.send_keys(Keys.ARROW_DOWN)
    #actions.send_keys_to_element(button,[Keys.ARROW_DOWN for _ in range(3)]).pause(1)
    actions.send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.RETURN)
    #actions.send_keys(Keys.DOWN)
        #ActionChains(driver).perform()
    actions.perform()
    #button.send_keys(Keys.ENTER)
    #button.click()
    '''
    for _ in range(5):
        ActionChains(driver).pause(1).send_keys_to_element(button, Keys.ARROW_DOWN)
    ActionChains(driver).perform()

    ActionBuilder(driver).clear_actions()''' 
    #driver.implicitly_wait(5)
    ActionBuilder(driver).clear_actions()
    return driver
drive = launch_chrome()
#drive.quit() #if the page opens but no action is taken(it freezes) it means the page's already open/in use elsewhere!
