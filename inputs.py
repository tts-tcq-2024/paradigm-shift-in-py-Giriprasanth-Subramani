# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:54:53 2024

@author: GIU1COB
"""

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


Temperature_status_check = True
SOC_status_check = True
Chargerate_status_check = True

