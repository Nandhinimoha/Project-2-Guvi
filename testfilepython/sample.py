from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class form:
    def __init__(self,url,firstname,email):
        self.url= url
        self.firstname = firstname
        self.email = email
    def reg_ister(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.driver.find_element(By.ID,'firstName').send_keys(self.firstname)
        self.driver.find_element(By.ID,'userEmail').send_keys(self.email)
obj=form("https://demoqa.com/automation-practice-form","moha","moha@gmail.com")
obj.reg_ister()