from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    USER_MENU = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href*='auth/logout']")

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_LINK)
