# !/usr/bin/env python
#  -*- coding: utf-8 -*-
# whoisharrison.com
# api https://home.openweathermap.org/

import urllib2
import json
from os import system, name
import time
import sys

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

clear() 

print('       *          *  *    *     *     *       *      *        *  *     *     *       *      * ') 
print('  *          *      *    *   * *     *      *      *     *    *      *   *     * *     *   *  ')
print(' * ████████╗██╗  ██╗███████╗ *  ██╗  * ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗    ')
print('   ╚══██╔══╝██║  ██║██╔════╝    ██║ *  ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗  *')
print('   *  ██║   ███████║█████╗ *    ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝*  ')
print(' *    ██║ * ██╔══██║██╔══╝   *  ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗  *')
print('    * ██║   ██║  ██║███████╗    ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║ * ')
print('      ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ')
print('                                                                                 bot v0.0.1   ')
print('                                                                                              ') 
print('')

welcome = "Welcome to The Weather Bot\nYou can say things like, 'Weather' or 'Sunset' \nLet's begin\n"
for l in welcome:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.02)

# def hello():
#     print('')
#     the_zipcode = raw_input()

# hello()

# def first_question():
#     if the_zipcode == 'Help':
#         print("okay, here are your options...")
#         print('')
#         print("1. Author     2. Version    3. Location    4. How does this work?    5. More")
#         more_options = raw_input("Which would like like information on?")
#         # get_weather(the_zipcode)
#     else:
#         print("Sorry, I have not yet learned that request")
#         hello()

print('')
print("What would you like to know?")
request = raw_input()
def get_request():
    if request == "Weather" or request == "weather":
        print("Enter your zipcode. ")
        the_zipcode = raw_input() 
        api_key = "e70a4b7f391668d9516d1e13385a6117"
        url = "https://api.openweathermap.org/data/2.5/weather?zip="
        final_url = url + the_zipcode + ",us&APPID=" + api_key
        json_obj = urllib2.urlopen(final_url)
        data = json.load(json_obj)

        print "The current weather in " + data['name'] + " is:\n "
        for item in data['weather']:
            print item['description']

    elif request == "Sunset" or request == "sunset":
        print("Enter your zipcode. ")
        the_zipcode = raw_input() 
        api_key = "e70a4b7f391668d9516d1e13385a6117"
        url = "https://api.openweathermap.org/data/2.5/weather?zip="
        final_url = url + the_zipcode + ",us&APPID=" + api_key
        json_obj = urllib2.urlopen(final_url)
        data = json.load(json_obj)

        print "The current sunset for " + data['name'] + " will be:\n "
        for item in data['sys']:
            print str(item['sunset'])
    else:
        print("Im not sure I understand that request. You can enter 'Weather' or 'Help' if you need help")

get_request()


