from settings import BASE_URL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class TripPlanTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def _teardown(self):
        self.driver.quit()
        return

    def _input_text(self, input_id, text, dropdown_id=None):
        input_element = self.driver.find_element_by_id(input_id)
        input_element.send_keys(text)
        input_element.click()

        # Need to wait the dropdown to load
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, dropdown_id)))
        suggestion_element = self.driver.find_element_by_id(dropdown_id)
        suggestion_element.click()

        return

    def _get(self, url):
        self.driver.get(url)
        return

    def _click(self, id_value):
        go_button = self.driver.find_element_by_id(id_value)
        go_button.click()
        return

    def _should_be_visible(self, id_value):
        element = self.driver.find_element_by_id(id_value)
        if element is None:
            return False
        return True

    def test_make_a_trip_plan(self):
        # Give a user to the trip plan page
        self._get(BASE_URL + "/trip")

        # When he executes a trip plan from "North Sydney Station" To "Town Hall Station"
        self._input_text(input_id='search-input-From', text="North Sydney Station", dropdown_id="suggestion-From-0")
        self._input_text(input_id='search-input-To', text="Town Hall Station", dropdown_id="suggestion-To-0")
        self._click(id_value="search-button")

        # Then a list of trips should be provided
        results = self._should_be_visible(id_value="tp-result-list")
        self._teardown()
        assert(results)


if __name__ == "__main__":
    unittest.main()