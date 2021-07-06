from django.test import TestCase
from  api.library.utilities import Utilities

class UtilitiesTest(TestCase):

    def setUp(self):
        """ 
        Set up required test variables
        """
        self.closing_hour=17
        # the closing hour is save in the app_settings table in hour format

    def test_is_slot_within_closing_hour(self):
        """ 
        Test to ensure that our customer slot time is always within our closing hour limit

        A customer must not schedule a slot that will extend beyond our closing hour
        """
        slot_time_value=170000     # this is equivalent to ``17:00:00``  format equiv to ``5:00PM`            

        valid_slot= Utilities.is_slot_within_closing_hour(closing_hour=self.closing_hour, slot_end_time=slot_time_value)

        self.assertIs(valid_slot, True, " Shedule slot cannot exceed {}:00 hours".format(self.closing_hour))

    def test_response_formatter(self):
        """ 
        Response formater must be an  object  containing ``error``, ``message`` and ``data`` keys and values
        """
        formatter_response=Utilities.response_formatter(True, "Test formatter Return")
        # sample response formatter return value Response formatter must return data key all the time

        self.assertIn('error', formatter_response, "Must have error key")
        self.assertIn('message', formatter_response, "Must have message key")
        self.assertIn('data', formatter_response, "Must have data key")
        # asserts dictionary keys

