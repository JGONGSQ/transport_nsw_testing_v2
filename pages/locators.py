from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'search-button')
    ORIGIN_DROPDWON = (By.ID, 'suggestion-From-0')
    DESTINATION_DROPDWON = (By.ID, 'suggestion-To-0')
    TP_RESULTS = (By.ID, 'tp-result-list')

