from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import loadLocations


def launch_ptkSite():
    PTK_URL = 'https://www.petah-tikva.muni.il/Emergency/Pages/Receivers.aspx'
    driver = loadLocations.Automaps(PTK_URL).driver
    table = driver.find_element(By.CSS_SELECTOR, '#\{48951049-1547-45AE-997F-43DBD767B541\}-\{3AF38EB6-5029-4658-95BA-6DBC5310651D\} > tbody')
    rows = table.find_elements(By.XPATH, './/tr')
    ADDR_FILE = open("testfile.txt", mode="wt")
    for row in rows:
        cols = row.find_elements(By.XPATH, ".//td")
        # Address column
        res = cols[1].text#[::-1]
        # Format hebrew (split number from name, then append number to reversed street name)
        res = res.rsplit(" ",1)
        if len(res) >= 2:
            # res = res[1] +' '+ res[0]#[::-1]
            res =  res[0] +' '+ res[1]
        try:
            ADDR_FILE.write(str(res)+"\n")
        except Exception as err:
            print("error:{err} type:"+str(type(err)))
        print(res)

        #address = row.find_elements(By.XPATH,'./*') # //*[@id="37,114,0"] //*[@id="37,114,0"]/td[2]
        #print(address.text[::-1])
        #print(row.text)
    ADDR_FILE.close()
    print("done")
    return driver
driver = launch_ptkSite()
driver.close()