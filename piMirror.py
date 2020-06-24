import requests, json
import RPi.GPIO as gpio
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_drver.lcd()


BASE_URL = "https://openweathermap.org/data/2.5/weather"

API_KEY = "9bd89b63579804f4c39bd23c18f121e6"
CITY = "albuquerque"
URL = BASE_URL + "q=" + CITY + "&appid" + API_KEY

response = requests.get(URL)

if(response.status_code == 200):
    data = response.json
    main = data['main']
    temp = main['main']
    report = data['weather']
    mylcd.lcd_display_string("temp: {temp}", 0, 0)
    mylcd.lcd_display_string("weather: {report}", 0, 1)
