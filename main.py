from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

citizen ="" #your citizenship number without -
place=""  #your birthplace
dob=""  #dob MM-DD-YY without - eg:"12181998" 12-18-1998
surname=""  #your surname
options = Options()
options.add_argument("--headless=new")  
options.add_experimental_option("detach", True) 
driver = webdriver.Chrome(options=options)

if __name__=="__main__":
    driver.get('https://nepalpassport.gov.np/')

    body=driver.find_element(By.CLASS_NAME,'home')
    body.send_keys(Keys.ESCAPE)
    body.send_keys(Keys.ESCAPE)
    body.send_keys(Keys.ESCAPE)
    body.send_keys(Keys.ESCAPE)
    wait=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#citizenship')))
    citizen_box = driver.find_element(By.CSS_SELECTOR,'input#citizenship')
    dob_box = driver.find_element(By.CSS_SELECTOR,'input#date_birth')
    place_box = driver.find_element(By.CSS_SELECTOR,'select#place_birth')
    surname_box = driver.find_element(By.CSS_SELECTOR,'input#surname')

    citizen_box.send_keys(citizen)
    dob_box.send_keys(dob)
    place_box.send_keys(place)
    surname_box.send_keys(surname)
    surname_box.send_keys(Keys.ENTER)
    wait=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.alert.d-flex')))
    check_status= driver.find_element(By.CSS_SELECTOR,'div.alert.d-flex')
    print(check_status.text)





