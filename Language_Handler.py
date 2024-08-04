# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 22:19:25 2024

@author: GIU1COB
"""

import inputs

class LanguageHandler:
    def language_selection(input_value):
        Languages = inputs.Languages
        if input_value in Languages:
            language_index = Languages.index(input_value)
            return language_index
        else:
            return "Language not supported"