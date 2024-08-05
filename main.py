from Language_Handler import LanguageHandler as lh
from BMS_Utilities import BMSstatuscheck as sc

def PrintMessageonConsole(message):
    print(message)
    
def battery_is_ok(temperature, soc, charge_rate,language = 'English'):    
  #  language_index = lh.language_selection(language)
  #  if language_index == "Language not supported":
   #     PrintMessageonConsole(language_index)
     #   return False
    else:
        Temperature_status = sc.CheckTemperatureInRange(temperature,language)        
        SOC_status = sc.CheckSocInRange(soc,language)        
        Chargerate_status = sc.CheckChargeRateInRange(charge_rate,language)
        battery_status = {
            "Temperature_status": Temperature_status[1],
            "SOC_status": SOC_status[1],
            "Chargerate_status": Chargerate_status[1]
            }
        PrintMessageonConsole(battery_status)
        battery =Temperature_status[0] + SOC_status[0] + Chargerate_status[0]     
        if battery == 3:
           return True
        else:
           return False     
   
if __name__ == '__main__':     
        def allvaluesinnormalrange(): 
            assert(battery_is_ok(25, 70, 0.5,'English') is True)
        def allvaluesinwarningrange():   
            assert(battery_is_ok(43, 22, 0.7,'English') is True)
        def germanlanguagecheck():
            assert(battery_is_ok(50, 85, 0,'German') is False)
        def allvaluesinbreach():
            assert(battery_is_ok(-10, 15, 1.0,'English') is False)
        def laguagenotsupported():
            assert(battery_is_ok(-10, 15, 1.0,'Spanish') is False)
        def valuenotingivenrange():
            assert(battery_is_ok(-25, 15, 1.0) is False)
