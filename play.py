import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model
import numpy as np
import mss
from PIL import Image
import pyautogui

model = load_model('model_file.h5')

while(True):
  
    # monitor = {"top": 205, "left": 740, "width": 115, "height": 100}
    monitor = {"top": 139, "left": 740, "width": 115, "height": 100}
    img = np.array(mss.mss().grab(monitor))
    img_gray = Image.fromarray(img).convert('L')
    x = np.expand_dims(img_gray, axis=(0, 3))
    prediction = np.argmax(model.predict(x), axis=-1)[0]
    if prediction == 2:
        pyautogui.press('up')
        print('up')
    elif prediction == 0:
        pyautogui.press('down')
        print('down')
    elif prediction == 1:
        print('right')

