Languages = ['English', 'German']

SOC_RANGES = {
    (0, 20): ["LOW SOC BREACH", "LOW SOC VERLETZUNG"],
    (21, 24): ["LOW SOC WARNING", "WARNUNG ZU NIEDRIGEM SOC"],
    (25, 75): ["NORMAL SOC", "NORMALER SOC"],
    (76, 80): ["HIGH SOC WARNING", "WARNUNG ZU HOHEM SOC"],
    (81, 100): ["HIGH SOC BREACH", "HIGH SOC VERLETZUNG"]
}

TEMPERATURE_RANGES = {
    (-20, 0): ["LOW TEMPERATURE BREACH", "NIEDRIGE TEMPERATURVERLETZUNG"],
    (0, 2.25): ["LOW TEMPERATURE WARNING", "WARNUNG NIEDRIGE TEMPERATUR"],
    (2.25, 42.75): ["NORMAL TEMPERATURE", "NORMALE TEMPERATUR"],
    (42.75, 45): ["HIGH TEMPERATUE WARNING", "WARNUNG ZU HOHER TEMPERATUR"],
    (45, 60): ["HIGH TEMPERATURE BREACH", "VERLETZUNG DER HOHEN TEMPERATUR"]
}

CHARGERATE_RANGES = {
    (0, 0.2): ["LOW CHARGERATE WARNING", "Warnung vor niedrigem Ladestand"],
    (0.2,0.6 ): ["NORMAL CHARGERATE ", "NORMALES LADEN"],
    (0.6, 0.8): ["HIGH CHARGERATE WARNING", "Warnung vor hoher Ladung"],
    (0.8, 1.0): ["HIGH CHARGERATE BREACH", "HOHE LADEVERLETZUNG"]
}

def language_selection(input_value):
    if input_value in Languages:
        language_index = Languages.index(input_value)
        return language_index
    else:
        return "Language not supported"
    
    
def status_message(value,value_range, language_index):        
    status_message = next((status[language_index] for range_tuple, status in value_range.items()
                       if range_tuple[0] <= value <= range_tuple[1]), "INVALID_VALUE")      
    PrintMessageonConsole(status_message)


def CheckTemperatureInRange(temperature,language_index):
    status_message(temperature, TEMPERATURE_RANGES, language_index)
    if temperature >= 0 and temperature <= 45:
        return 1
    else:
        return 0
    

def CheckSocInRange(soc,language_index):
    status_message(soc, SOC_RANGES, language_index)    
    if soc >=20 and soc <= 80:
        return 1
    else:
        return 0
    

def CheckChargeRateInRange(charge_rate,language_index):
    status_message(charge_rate, CHARGERATE_RANGES, language_index)
    if 0.8 > charge_rate:
        return 1       
    else:
        return 0    

def PrintMessageonConsole(message):
    print(message)
    
def battery_is_ok(temperature, soc, charge_rate,language):    
    language_index = language_selection(language)
    if language_index == "Language not supported":
        PrintMessageonConsole(language_index)
        return False
    else:
        battery = CheckTemperatureInRange(temperature,language_index) + CheckSocInRange(soc,language_index) + CheckChargeRateInRange(charge_rate,language_index)        
        if battery == 3:
           return True
        else:
           return False     
   

if __name__ == '__main__':        
        assert(battery_is_ok(25, 70, 0.5,'English') is True)
        assert(battery_is_ok(43, 22, 0.7,'English') is True)
        assert(battery_is_ok(50, 85, 0,'German') is False)
        assert(battery_is_ok(-10, 15, 1.0,'English') is False)
        assert(battery_is_ok(-10, 15, 1.0,'Spanish') is False)
        assert(battery_is_ok(-25, 15, 1.0,'English') is False)
