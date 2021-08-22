import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model
import numpy as np
import mss
from PIL import Image

model = load_model('model_file.h5')

while(True):
  
    monitor = {"top": 130, "left": 650, "width": 650, "height": 150}
    img = np.array(mss.mss().grab(monitor))
    img_gray = Image.fromarray(img).convert('L')
    x = np.expand_dims(img_gray, axis=(0, 3))
    prediction = np.argmax(model.predict(x), axis=-1)[0]

    print(prediction)