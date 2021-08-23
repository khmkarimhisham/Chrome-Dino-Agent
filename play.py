import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model
import numpy as np
import mss
from PIL import Image
import pyautogui

model = load_model('model_file.h5')

while(True):
  
    monitor = {"top": 200, "left": 650, "width": 600, "height": 130}
    img = np.array(mss.mss().grab(monitor))
    img_gray = Image.fromarray(img).convert('L')
    x = np.expand_dims(img_gray, axis=(0, 3))
    prediction = np.argmax(model.predict(x), axis=-1)[0]
    if prediction == 2:
        pyautogui.press('up')
    elif prediction == 0:
        pyautogui.press('down')

