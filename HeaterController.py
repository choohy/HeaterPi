class HeaterController:
    #Heater defaults
    heater_status = 'OFF'
    auto_status = 'OFF'
    timer_status = 'OFF'
    heater_temperature = 30
    auto_start_time = '10:00:00'
    auto_end_time = '20:00:00'
    
    #Constructor
    def __init__(self, heater_status):
        self.heater_status = heater_status
        
    def show_heater_status(self):
        text = 'The heater status is '+ str(self.heater_status)
        print(text)
        return text
        
    def get_input(self,text):
        return input(text)
        
    def status_input(self):
        #Change status input
        input_value = self.get_input('0: OFF, 1: ON\n')
        ##/input_value = input('0: OFF, 1: ON\n')
    ##    print('input_value '+ input_value)
        status_switcher = {
            0: self.status_off,
            1: self.status_on
        }
        # Get the function from switcher dictionary
        func = status_switcher.get(int(input_value), lambda: "Invalid input")
        # Execute the function
        return func()
    
    def set_heater_status(self, new_status):
        self.heater_status = new_status
        return self.heater_status

    def change_heater_status(self):
        self.show_heater_status()
        self.set_heater_status(self.status_input())
    ##    store_data()
        self.show_heater_status()
        return self.heater_status

    def status_on(self):
        return 'ON'

    def status_off(self):
        return 'OFF'
    
##temp = HeaterController('OFF')
##print(temp.change_heater_status())
