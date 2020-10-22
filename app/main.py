#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:40:54 2020

@authors: evaanderson, Jessica Yen

Server Code file:
Eva focused on server to ESP
Jessica focused on server to app
url: https://pnat-server.herokuapp.com/
"""

from flask import Flask, session, request
app = Flask(__name__)
app.secret_key = "bo7YMBYR7MYq4o7"


# Global Variables
button_pressed = False
light_on = False 


########################################
#### Routing paths for GET requests ####
########################################

# Home page
@app.route('/')  
def welcome_home():
    return "Welcome Home!"


# Current status of button and light
@app.route('/data')
def data():
    return f"Button is {button_pressed} and light is {light_on}"


# Current status of button with optional parameter 'button' to specify a push
@app.route('/app')
def button_info():
    global button_pressed
    button_parameter = request.args.get('button')
    if button_parameter is None:
        return "button status is " + str(button_pressed)
    
    button_pressed = bool(request.args.get('button'))
    return "button status is " + str(button_pressed)


# Current status of ESP with optional parameter 'light' to specify an on/off
@app.route('/esp')
def light_info():
    global light_on
    light_parameter = request.args.get('light')
    if light_parameter is None:
        return "light status is " + str(light_on)
    light_on = bool(request.args.get('light'))
    return "light status is " + str(light_on)


if __name__ == '__main__':
	app.debug = True
	app.run()