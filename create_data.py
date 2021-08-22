import time
import numpy as np
from PIL import Image
import os
import keyboard
from random import random
import mss

data_file = "data/"
up_file = "data/up/"
down_file = "data/down/"
nokey_file = "data/nokey/"
monitor = {"top": 200, "left": 650, "width": 600, "height": 130}


if not os.path.isdir(data_file):
    os.mkdir(data_file)
    if not os.path.isdir(up_file):
        os.mkdir(up_file)
    if not os.path.isdir(down_file):
        os.mkdir(down_file)
    if not os.path.isdir(nokey_file):
        os.mkdir(nokey_file)

i = 1


def up():
    global i
    screenshot = np.array(mss.mss().grab(monitor))
    img = Image.fromarray(screenshot).convert('L')
    img.save(up_file + str(time.time()) + '.png')
    i += 1


def down():
    global i
    screenshot = np.array(mss.mss().grab(monitor))    
    img = Image.fromarray(screenshot).convert('L')
    img.save(down_file + str(time.time()) + '.png')
    i += 1


def nokey():
    global i
    while True:
        screenshot = np.array(mss.mss().grab(monitor))    
        img = Image.fromarray(screenshot).convert('L')
        img.save(nokey_file + str(time.time()) + '.png')
        i += 1
        time.sleep(0.5)


keyboard.on_press_key("up", lambda _: up())
keyboard.on_press_key("down", lambda _: down())
keyboard.on_press_key("q", lambda _: os._exit(0))

while True:
    print("Press space to start")
    if keyboard.read_key() == "space":
        print('The game has started')
        nokey()
        