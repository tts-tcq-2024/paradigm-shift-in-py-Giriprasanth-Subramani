# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:34:07 2024

@author: GIU1COB
"""
from Status_message_handler import statusmessagehandler as sm
import inputs


class BMSstatuscheck:
    def CheckTemperatureInRange(temperature,Language,status_message = None):        
        if inputs.Temperature_status_check:
            TEMPERATURE_RANGES = inputs.TEMPERATURE_RANGES            
            status_message = sm.StatusMessage(temperature, TEMPERATURE_RANGES, Language)     
        if temperature >= 0 and temperature <= 45:
            return 1,status_message
        else:
            return 0,status_message
        

    def CheckSocInRange(soc,Language,status_message = None):        
        if inputs.SOC_status_check:            
            SOC_RANGES = inputs.SOC_RANGES            
            status_message = sm.StatusMessage(soc, SOC_RANGES, Language)      
        if soc >=20 and soc <= 80:
            return 1,status_message
        else:
            return 0,status_message
        

    def CheckChargeRateInRange(charge_rate,Language,status_message = None):        
        if inputs.Chargerate_status_check:            
            CHARGERATE_RANGES = inputs.CHARGERATE_RANGES            
            status_message = sm.StatusMessage(charge_rate, CHARGERATE_RANGES, Language)
        if 0.8 > charge_rate:
            return 1,status_message   
        else:
            return 0,status_message