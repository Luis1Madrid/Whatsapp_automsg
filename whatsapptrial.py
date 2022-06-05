from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
from datetime import date, datetime

#Random page size use each  time
sx = random.randint(1000, 1500)
sn = random.randint(3000, 4500)

#Chrome options at the time of opening it
option= webdriver.ChromeOptions()
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches",["enable-automation"])
option.add_argument("user-data-dir=selenium")
#option.add_argument("disable-client-side-phishing-detection")
option.add_experimental_option("detach", True)              #keep browser open after test
#option.add_argument("window-size=1280,800")
#option.add_argument("user-agent= Chrome/102.0.5005.61")
#option.add_argument(f'user-agent={userAgent1}')

# Using Chrome to access web
driver = webdriver.Chrome(executable_path="/Users/local/bin/chromedriver", options= option)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)

#driver.set_window_size(str(sx), str(sn))
driver.get("https://web.whatsapp.com/")

#List of People
list_people = ["John Doe", "18059989204", "18059989205", "18059989204"]

def msg(name1, message1):
    
    try:
        
        #Find whom to message
        action.move_to_element(wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title = '{}']".format(name1))))).click().perform()
        
        msg_send(message1)
    
    except:
        
        driver.get("https://web.whatsapp.com/send?phone=" + name1)
        
        try:
            time.sleep(1)
            acc_user = driver.find_element(
                by=By.XPATH,
                value = "(//div[@class = '_20C5O'])[3]"
            )
            acc_user.click()
        
            time.sleep(1)
            msg_send(message1)
        except:
            time.sleep(1)
            msg_send(message1)

def msg_send(msg_to_send):
    #Find Text Box
    time.sleep(2)
    text_box = driver.find_element(
        by=By.XPATH,
        value = "//div[@title = 'Type a message']"
    )
        
    #Send Button
    text_box.send_keys(msg_to_send)
    driver.find_element(
        by = By.CLASS_NAME,
        value = "_1Ae7k"
    ).click()


for i in list_people:
    
    #Time sent
    today1 = date.today()
    d2 = today1.strftime("%B %d, %Y")
    now1 = datetime.now()
    currenttime1 = now1.strftime("%H:%M:%S")
    
    #Message to send
    messageT = d2 + '/ ' + currenttime1 + ": Dear " + i + ": thank your for subscribing"
    msg(i, messageT)
    
    #Random timer to avoid being banned
    time.sleep(random.randint(3,6))

