# !/usr/bin/env python
#  -*- coding: utf-8 -*-
# whoisharrison.com
# api https://home.openweathermap.org/

import urllib2
import json

print('                                                                                             ') 
print('                                                                                             ')
print('   ████████╗██╗  ██╗███████╗    ██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗   ')
print('   ╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗  ')
print('      ██║   ███████║█████╗      ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝  ')
print('      ██║   ██╔══██║██╔══╝      ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗  ')
print('      ██║   ██║  ██║███████╗    ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║  ')
print('      ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ')
print('                                                                                     v0.0.1  ')
print('                                                                                             ') 
print('')
print("Enter your zip code")
the_zipcode = raw_input() 

api_key = "e70a4b7f391668d9516d1e13385a6117"
url = "https://api.openweathermap.org/data/2.5/forecast?zip="
final_url = url + the_zipcode + "&APPID=" + api_key
json_obj = urllib2.urlopen(final_url)
data = json.load(json_obj)
print(data)
    

