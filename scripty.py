import requests
import random
import board
import neopixel
import threading
import time
import random

num_pixels=8
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D21, 8)

movieID = ["5cd95395de30eff6ebccde5c", "5cd95395de30eff6ebccde5b","5cd95395de30eff6ebccde5d"]

# print(dialog)

def active_led():
    choice = random.choice(movieID)
    # base url
    url = 'https://the-one-api.dev/v2/movie/'
    url += choice
    url += "/quote?limit=10"
    headers = {"Authorization": "Bearer G0VIFOb94ZUGUB46-K90"}
    response = requests.get(url, headers=headers)
    results = response.json()
    dialog = results['docs'][random.randint(0,9)]['dialog']
    val = len(dialog)%8
    pixels[val] = (255,0,0)
    print(val)
    pixels.show()
    threading.Timer(3.0, active_led).start()
def blank_led():
    pixels.fill((255,255,255))
    threading.Timer(12, blank_led).start()

active_led()
blank_led()
