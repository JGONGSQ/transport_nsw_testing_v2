from pages.base_page import BasePage
from pages.elements import BasePageElement
from pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OriginTextElement(BasePageElement):
    locator = 'search-input-From'


class DestinationTextElement(BasePageElement):
    locator = 'search-input-To'


class TripPlanPage(BasePage):

    origin_text_element = OriginTextElement()
    destination_text_element = DestinationTextElement()

    def click_origin_dropdown(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainPageLocators.ORIGIN_DROPDWON))
        element = self.driver.find_element(*MainPageLocators.ORIGIN_DROPDWON)
        element.click()

    def click_destination_dropdown(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainPageLocators.DESTINATION_DROPDWON))
        element = self.driver.find_element(*MainPageLocators.DESTINATION_DROPDWON)
        element.click()

    def click_go_button(self):
        """Trigger the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def results_list_should_be_visible(self):
        element = self.driver.find_element(*MainPageLocators.TP_RESULTS)
        if element is None:
            return False
        return True
