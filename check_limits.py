def temperature_ok(temperature):
    if temperature >= 0 and temperature <= 45:
        return True
    else:
        print('Temperature is out of range!')
        return False
    

def soc_ok(soc):
    if soc >=20 and soc <= 80:
        return True
    else:
        print('State of Charge is out of range!')
        return False
    

def charge_rate_ok(charge_rate):
    if 0.8 > charge_rate:
        return True       
    else:
        print('charge rate is out of range!')
        return False    
      
    
def battery_is_ok(temperature, soc, charge_rate):
           
   temperature_1 = temperature_ok(temperature)
   soc_2 = soc_ok(soc)
   charge_rate_3 = charge_rate_ok(charge_rate)
     
   if temperature_1 and soc_2 and charge_rate_3:
       return True
   else:
       return False

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(-10, 15, 1.0) is False)

