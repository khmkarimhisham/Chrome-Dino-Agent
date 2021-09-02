# Chrome Dino Agent
Chrome dinosaur game is a built-in browser game in the Google Chrome web browser. The player guides a pixelated Tyrannosaurus rex across a side-scrolling landscape, avoiding obstacles to achieve a higher score.

In this repository I built an agent that plays the game using CNN (Convolutional Neural Networks)

***
![Game Screenshot](https://9to5google.com/wp-content/uploads/sites/4/2018/09/chrome-offline-dino-game.jpg?quality=82&strip=all)

You will need to install **Tensorflow**, **numpy**, **mss**, **PIL**, **pyautogui**, and **keyboard** to make the agent work
```
pip install tensorflow numpy mss pil PyAutoGUI keyboard
```
Use this link **chrome://dino/** to access the game even when you have internet (*use chrome*).
***

# Theory
**1- Creating the dataset**
The first phase is creating the dataset, I wrote **create_data.py** file for creating the dataset by capturing screenshots for every key press while playing the game.

**2- Training the model**
The second phase is training the model on the three classes, Up, Down, and Right.
I trained a Convolutional Neural Network by using keras.

**3- make the agent plays**
The third phase is righting a script to make the model play the game by capturing screenshots and send it to the model to predict the next move then press the key.
