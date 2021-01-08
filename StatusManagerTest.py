from StatusManager import StatusManager
import unittest
from unittest.mock import patch

class StatusManagerTest(unittest.TestCase):

    def setUp(self):
        #Intial Utilties
        self.status_manager = StatusManager() 

    ##Status On
    def test_status_on(self):
        print('test_status_on')
        self.assertEqual(self.status_manager.status_on(),'ON','status is not on')

    ##Status Off
    def test_status_off(self):
        print('test_status_off')
        self.assertEqual(self.status_manager.status_off(),'OFF','status is not off')

class StatusManagerOnTest(unittest.TestCase):

    def setUp(self):
        #Intial Utilties
        self.status_manager = StatusManager() 

    ##Change status on
    @patch('StatusManager.StatusManager.get_input', return_value='1')
    def test_status_input(self,input):
        print('test_input_1')
        input_text = self.status_manager.status_input()
        self.assertEqual(input_text,'ON','input not 1')

class StatusManagerOffTest(unittest.TestCase):

    def setUp(self):
        #Intial Utilties
        self.status_manager = StatusManager() 

    ##Change status on
    @patch('StatusManager.StatusManager.get_input', return_value='0')
    def test_status_input(self,input):
        print('test_input_0')
        input_text = self.status_manager.status_input()
        self.assertEqual(input_text,'OFF','input not 0')

if __name__ == '__main__':
    unittest.main(exit=False)
