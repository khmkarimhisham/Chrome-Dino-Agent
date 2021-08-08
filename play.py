from keras.models import load_model
import numpy as np
import pyautogui
from skimage import color


model = load_model('model_file.h5')

while(True):
    screenshot = np.array(pyautogui.screenshot(region=(950, 130, 650, 150)))
    grayscale = color.rgb2gray(screenshot)
    img = np.expand_dims(grayscale, axis=(0, 3))

    prediction = np.argmax(model.predict(img), axis=-1)[0]
    print(prediction)

