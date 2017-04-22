from selenium import webdriver
import unittest

class test_new_group(unittest.TestCase):
    def setUp(self):
        self.wd=webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def test_test_new_group(self):
        success=True
        wd=