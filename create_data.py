import time
import numpy as np
from PIL import Image
import os
import keyboard
import mss

data_file = "data/"
up_file = "data/up/"
down_file = "data/down/"
right_file = "data/right/"
monitor = {"top": 205, "left": 740, "width": 115, "height": 100}


if not os.path.isdir(data_file):
    os.mkdir(data_file)
    if not os.path.isdir(up_file):
        os.mkdir(up_file)
    if not os.path.isdir(down_file):
        os.mkdir(down_file)
    if not os.path.isdir(right_file):
        os.mkdir(right_file)


def up():
    screenshot = np.array(mss.mss().grab(monitor))
    img = Image.fromarray(screenshot).convert('L')
    img.save(up_file + str(time.time()) + '.png')


def down():
    screenshot = np.array(mss.mss().grab(monitor))    
    img = Image.fromarray(screenshot).convert('L')
    img.save(down_file + str(time.time()) + '.png')


def right():
    screenshot = np.array(mss.mss().grab(monitor))    
    img = Image.fromarray(screenshot).convert('L')
    img.save(right_file + str(time.time()) + '.png')


keyboard.on_press_key("up", lambda _: up())
keyboard.on_press_key("down", lambda _: down())
keyboard.on_press_key("right", lambda _: right())
keyboard.on_press_key("q", lambda _: os._exit(0))

print('The game has started')

while True:
    pass        