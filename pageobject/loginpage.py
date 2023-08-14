from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Med:
    Text_Clinic_XPATH = (By.XPATH,"//mtab-input-text[@id='clinic']//input[@type='TEXT']")
    Text_Username_XPATH = (By.XPATH,"//mtab-input-text[@id='username']//input[@type='TEXT']")
    Text_Password_XPATH = (By.XPATH, "//input[@type='PASSWORD']")
    Click_Login_button_XPATH =(By.XPATH,"//span[@class='ui-button-text ui-clickable']")
    Massage_XPATH =(By.XPATH,"//span[@class='mtab-login-error-message']")

    def __init__(self,driver):
        self.driver = driver


    def LOGI_URL(self):
        self.driver.get("https://iemodemoindia.meditab.com/")


    def Enter_clinic_name(self,name):
        self.driver.find_element(*Med.Text_Clinic_XPATH).send_keys(name)

    def Enter_Username(self,username):
        self.driver.find_element(*Med.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Med.Text_Password_XPATH).send_keys(password)

    def Click_login_button(self):
        self.driver.find_element(*Med.Click_Login_button_XPATH).click()


    def Success_message(self):
        try:
            self.driver.find_element(*Med.Massage_XPATH)
            return True
        except NoSuchElementException:
            return False






