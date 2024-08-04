# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:23:40 2024

@author: GIU1COB
"""
from Language_Handler import LanguageHandler as lh

class statusmessagehandler:     
    
    def StatusMessage(value,value_range, language):
        language_index = lh.language_selection(language)            
        status_message = next((status[language_index] for range_tuple, status in value_range.items()
                       if range_tuple[0] <= value <= range_tuple[1]), "INVALID_VALUE")      
        return(status_message)
    
