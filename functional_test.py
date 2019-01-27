from selenium import webdriver
import unittest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        gecko_driver = 'virtualenv\\Scripts\\geckodriver.exe'
        self.browser = webdriver.Firefox(firefox_binary=binary, executable_path=gecko_driver)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

