class StatusManager:
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
    
    
    def status_on(self):
        return 'ON'

    def status_off(self):
        return 'OFF'