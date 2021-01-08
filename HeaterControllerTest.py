from HeaterController import HeaterController
import unittest
from unittest.mock import patch

class HeaterControllerTestOn(unittest.TestCase):

    def setUp(self):
        #Intial heater status is off
        self.controller = HeaterController('OFF') 

    ##Heater on
    def test_heater_status_on(self):
        print('test_set_heater_status_on')
        self.controller.set_heater_status(self.controller.status_on())
        self.assertEqual(self.controller.heater_status,'ON','heater status is not on')

    def test_show_heater_status_on(self):
        print('test_show_heater_status_on')
        self.controller.set_heater_status(self.controller.status_on())
        self.assertEqual(self.controller.show_heater_status(),'The heater status is ON','heater status is not on')

    ##Change heater on
    @patch('HeaterController.HeaterController.get_input', return_value='1')
    def test_status_input(self,input):
        print('test_input_1')
        input_text = self.controller.status_input()
        self.assertEqual(input_text,'ON','input not 1')
    
    @patch('HeaterController.HeaterController.status_input', return_value='ON')
    def test_change_heater_status_on(self,input):
        print('test_change_heater_status_on')
        input_text = self.controller.change_heater_status()
        self.assertEqual(input_text,'ON','heater is not on')


class HeaterControllerTestOff(unittest.TestCase):

    def setUp(self):
        #Intial heater status is off
        self.controller = HeaterController('ON') 

    ##Heater off
    def test_heater_status_off(self):
        print('test_set_heater_status_off')
        self.controller.set_heater_status(self.controller.status_off())
        self.assertEqual(self.controller.heater_status,'OFF','heater status is not off')

    def test_show_heater_status_off(self):
        print('test_show_heater_status_off')
        self.controller.set_heater_status(self.controller.status_off())
        self.assertEqual(self.controller.show_heater_status(),'The heater status is OFF','heater status is not off')

    ##Change heater off
    @patch('HeaterController.HeaterController.get_input', return_value='0')
    def test_status_input(self,input):
        print('test_input_0')
        input_text = self.controller.status_input()
        self.assertEqual(input_text,'OFF','input not 0')
    
    @patch('HeaterController.HeaterController.status_input', return_value='OFF')
    def test_change_heater_status_on(self,input):
        print('test_show_heater_status_off')
        input_text = self.controller.change_heater_status()
        self.assertEqual(input_text,'OFF','heater is not off')

if __name__ == '__main__':
    unittest.main()
