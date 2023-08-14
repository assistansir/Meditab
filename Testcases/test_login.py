from pageobject.loginpage import Med


class Test_Login:

    def test_login_001(self,setup):
        self.driver = setup
        self.md = Med(self.driver)
        self.md.LOGI_URL()
        self.md.Enter_clinic_name("xyz")
        self.md.Enter_Username("prajwal")
        self.md.Enter_Password("PRAJWAL123")
        self.md.Click_login_button()
        if self.md.Success_message()== True:
            self.driver.save_screenshot("D:\\meditab\\Screenshot\\test_login_001_pass.PNG")
            assert True
        else:
            self.driver.save_screenshot("D:\\meditab\\Screenshot\\test_login_001_fail.PNG")
            assert False
