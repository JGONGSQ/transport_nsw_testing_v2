import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from settings import BASE_URL
from selenium import webdriver
from pages.trip_plan_page import TripPlanPage
import unittest
import requests


class TripPlanTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.stop_api_url = "http://www.transportnsw.info/web/XML_STOPFINDER_REQUEST" \
                            "?TfNSWSF=true" \
                            "&language=en" \
                            "&name_sf={stopname}" \
                            "&outputFormat=rapidJSON" \
                            "&type_sf=any" \
                            "&version=10.2.2.48"

    def tearDown(self):
        self.driver.quit()

    def test_make_a_trip_plan(self):
        # Go to the page
        self.driver.get(BASE_URL + "/trip")
        trip_plan_page = TripPlanPage(self.driver)

        # Set the input text and click go
        trip_plan_page.origin_text_element = 'North Sydney Station'
        trip_plan_page.click_origin_dropdown()
        trip_plan_page.destination_text_element = 'Town Hall Station'
        trip_plan_page.click_destination_dropdown()
        trip_plan_page.click_go_button()

        # Then a list of trip should bbe provided
        self.assertTrue(trip_plan_page.results_list_should_be_visible())

    def test_stop_finder_api(self):
        # object station
        stopanme = "Wynyard Station"

        # form the url
        full_request_url = self.stop_api_url.format(stopname=stopanme)

        # get the url via requests package
        response = requests.get(full_request_url).json()

        # compare the name
        self.assertEqual(response['locations'][0]['name'], "Wynyard Station, Sydney")

        # compare the number of travel modes
        self.assertTrue(len(response['locations'][0]['modes']) > 1)


if __name__ == "__main__":
    unittest.main()
