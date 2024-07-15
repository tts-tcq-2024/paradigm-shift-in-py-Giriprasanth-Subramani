def CheckTemperatureInRange(temperature):
    if temperature >= 0 and temperature <= 45:
        return 1
    else:
        PrintMessageonConsole('Temperature is out of range!')
        return 0
    

def CheckSocInRange(soc):
    if soc >=20 and soc <= 80:
        return 1
    else:
        PrintMessageonConsole('State of Charge is out of range!')
        return 0
    

def CheckChargeRateInRange(charge_rate):
    if 0.8 > charge_rate:
        return 1       
    else:
        PrintMessageonConsole('charge rate is out of range!')
        return 0    

def PrintMessageonConsole(message):
    print(message)
    
def battery_is_ok(temperature, soc, charge_rate):
           
   battery = CheckTemperatureInRange(temperature) + CheckSocInRange(soc) + CheckChargeRateInRange(charge_rate)
     
   if battery == 3:
       return True
   else:
       return False

if __name__ == '__main__':
        assert(battery_is_ok(25, 70, 0.7) is True)
        assert(battery_is_ok(50, 85, 0) is False)
        assert(battery_is_ok(-10, 15, 1.0) is False)

