from StatusManager import StatusManager

class HeaterController(StatusManager):
    #Heater defaults
##    heater_status = 'OFF'
##    auto_status = 'OFF'
##    timer_status = 'OFF'
##    heater_temperature = 30
##    auto_start_time = '10:00:00'
##    auto_end_time = '20:00:00'
##    utilities = Utilities()
    
    #Constructor
    def __init__(self, heater_status):
        self.heater_status = heater_status
        
    def show_heater_status(self):
        text = 'The heater status is '+ str(self.heater_status)
        print(text)
        return text
    
    def set_heater_status(self, new_status):
        self.heater_status = new_status
        return self.heater_status

    def change_heater_status(self):
        self.show_heater_status()
        self.set_heater_status(self.status_input())
    ##    store_data()
        self.show_heater_status()
        return self.heater_status
    
##temp = HeaterController('OFF')
##print(temp.change_heater_status())
