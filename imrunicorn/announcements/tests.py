from django.test import TestCase
from .models import MainPageBlurbs, WhatIsNew, PageBlurbOverrides


class MainPageBlurbsTestCase(TestCase):
    def setUp(self):
        print("\n\r*** RESETTING TEMP DATABASE ***")
        MainPageBlurbs.objects.create(Blurb="This Blurb is active.", Is_Active=True)
        MainPageBlurbs.objects.create(Blurb="This Blurb is NOT active.", Is_Active=False)

    def test_can_create_item(self):
        print("--- Testing Create MainPageBlurbs")
        active = MainPageBlurbs.objects.get(pk=1)
        not_active = MainPageBlurbs.objects.get(pk=2)
        print("\tChecking that Is_Active=True is True")
        self.assertTrue(active.Is_Active)
        print("\tChecking that Is_Active=False is False")
        self.assertFalse(not_active.Is_Active)

    def test_can_change_item(self):
        print("--- Testing Change MainPageBlurbs")
        active = MainPageBlurbs.objects.get(pk=1)
        print("\tIs_Active=True is True")
        self.assertTrue(active.Is_Active)
        print("\tSetting it to False")
        active.Is_Active = False
        print("\tIs_Active=False is False")
        self.assertFalse(active.Is_Active)
        print("\tChecking active blurb content")
        self.assertEqual(active.Blurb, "This Blurb is active.")
        active.Blurb = "Content has been changed in a test."
        print("\tChecking active blurb content after change")
        self.assertEqual(active.Blurb, "Content has been changed in a test.")

    def test_can_delete(self):
        print("--- Testing count MainPageBlurbs")
        records = MainPageBlurbs.objects.all()
        print("\tRecord count is 2")
        self.assertTrue(len(records) == 2)
        print("\tDeleting record index 1")
        records[1].delete()
        records = MainPageBlurbs.objects.all()
        print("\tRecord count is 1")
        self.assertTrue(len(records) == 1)


class PageBlurbOverridesTestCase(TestCase):
    def setUp(self):
        PageBlurbOverrides.objects.create(Blurb="magic", Page_Link_From_Base="/magic")
        PageBlurbOverrides.objects.create(Blurb="magic sub link", Page_Link_From_Base="/magic/sub/link")




# import unittest
# from selenium import webdriver
#
#
# class TestSignup(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_signup_fire(self):
#         self.driver.get("http://127.0.0.1:8000/api/announcements/main_page_blurbs/")
#         self.driver.find_element_by_id('Blurb').send_keys("automated testing")
#         self.driver.find_element_by_id('Is_Active').click()
#         self.driver.find_element_by_id('POST').click()
#         self.assertIn("http://localhost:8000/", self.driver.current_url)
#
#     def tearDown(self):
#         self.driver.quit
#
#
# if __name__ == '__main__':
#     unittest.main()
