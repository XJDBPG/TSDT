from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):
    def setUp(self): self.browser = webdriver.Chrome()

    def tearDown(self): self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy flowers', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()