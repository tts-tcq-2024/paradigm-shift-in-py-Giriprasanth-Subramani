def temperature_ok(temperature):
    if temperature >= 0 and temperature <= 45:
        return 1
    else:
        print('Temperature is out of range!')
        return 0
    

def soc_ok(soc):
    if soc >=20 and soc <= 80:
        return 1
    else:
        print('State of Charge is out of range!')
        return 0
    

def charge_rate_ok(charge_rate):
    if 0.8 > charge_rate:
        return 1       
    else:
        print('charge rate is out of range!')
        return 0    
      
    
def battery_is_ok(temperature, soc, charge_rate):
           
   battery = temperature_ok(temperature) + soc_ok(soc) + charge_rate_ok(charge_rate)
     
   if battery == 3:
       return True
   else:
       return False

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(-10, 15, 1.0) is False)

