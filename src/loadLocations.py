from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def launch_chrome():
    chrome_options = Options()

    chrome_options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\") #Opens my profile by freezes
    #chrome_options.add_argument("--profile-directory=Default")


    #chrome_driver = "C:\\Users\\USER\\AppData\\Local\\Google\\ChromeDriver\\chromedriver.exe"
    #service = Service(executable_path= chrome_driver)

    #driver = webdriver.Chrome(service = service, options = chrome_options) unnecessary, since chromedriver's already in path

    #driver = webdriver.Chrome( options = chrome_options)
    #driver = webdriver.Chrome() 
    #chrome_options.add_experimental_option("detach", True)
    #chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
    #driver = webdriver.Chrome(options=ops)


    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu")
    #title = driver.title
    driver.implicitly_wait(5)
    textbox = driver.find_element(By.ID, "searchboxinput") # or XmI62e for the form itself
    #add petah tikva prefix to each local address
    textbox.send_keys("הלל זכריה 28")
    textbox.send_keys(Keys.ENTER)
    saveButton = driver.find_element(By.CSS_SELECTOR,'#QA0Szd>div>div>div.w6VYqd>div.bJzME.tTVLSc>div>div.e07Vkf.kA9KIf>div>div>div.m6QErb.Pf6ghf.ecceSd.tLjsW>div:nth-child(2)>button')
    saveButton.click()
    #driver.quit()

    return driver
drive = launch_chrome()
#driver.quit() #if the page opens but no action is taken(it freezes) it means the page's already open/in use elsewhere!
