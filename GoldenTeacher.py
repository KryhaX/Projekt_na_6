# Golden Teacher by Krystian Wierciak

# Necessary Packages
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import pyautogui
import datetime
import uuid
from tkinter import *
import webbrowser

print('''Main Gesture: 
screenshot
left 
thumbs up - up
thumbs down - down
stop 
Quit
right''')

# GUI window
GUIwindow = Tk()
GUIwindow.title('Golden Teacher')
GUIwindow.geometry('300x300')
GUIwindow.config(bg='gold')

# Label of GUI
Title = Label(GUIwindow, text="Golden Teacher", bg="gold", fg="black", font=('Helvetica', 10,
                                                                             'bold'), width=20, height=5, borderwidth=5,
              relief='sunken')
Title.pack()


# global variable on/off ( Boolean ) | Turned on/off main program
global isOn
isOn = True
On_Main_While = False
# Switching a color of on/off button | Turned on/off main program
def switch():
    global isOn
    if isOn:
        TurnOnOffButton.config(bg='green', text='Now is on')
        isOn = False
    elif isOn == False:
        TurnOnOffButton.config(bg='red',text='Now is off')

        # initialize mediapipe
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mpDraw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
        model = load_model('mp_hand_gesture')

        # Load class names
        with open('gesture.names', 'r') as f:
            classNames = f.read().split('\n')
            # Showing the lines of avaible gesture

        print('''
        Main Gesture: 
        screenshot
        left 
        thumbs up - up
        thumbs down - down
        stop 
        Quit
        right''')

        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        global On_Main_While
        On_Main_While = True

        while On_Main_While:
            # Read frame's
            _, frame = cap.read()
            x, y, c = frame.shape

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get hand landmark prediction
            result = hands.process(framergb)

            className = ''

            # post process the result
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)

                        landmarks.append([lmx, lmy])

                    # Drawing landmarks on frames
                    mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                    # Predict gesture
                    prediction = model.predict([landmarks])
                    # print(prediction)
                    classID = np.argmax(prediction)
                    className = classNames[classID]

            # show the prediction on the frame
            cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

            # Window of command of gesture view
            cv2.imshow("Golden Teacher View ( press q to Quit ) ", frame)

            gestures_keys = {'screenshot':'screenshot', 'slide_left': 'left', 'up': 'up', 'down': 'down', 'TurnOn_Whatsapp': 'TurnOnWhatsapp',
                             'stop': 'space', 'close': 'q', '_space': 'space', 'slide_right': 'right', 'Stop': 'space'}

            global MakeScreenshot
            MakeScreenshot = None

            global TurnOn_Whatsapp
            TurnOn_Whatsapp = None

            global isOff
            isOff = None

            def AssignKeyToGesture(gesture, key):
                if className == gesture:
                    print(gesture)
                    pyautogui.press([f'{key}'])
                    pyautogui.sleep(1)

                elif className == 'close':
                    global isOff
                    isOff = True
                elif className == 'screenshot':
                    global MakeScreenshot
                    MakeScreenshot = True
                elif className == 'TurnOn_Whatsapp':
                    global TurnOn_Whatsapp
                    TurnOn_Whatsapp = True

            # Assigment Gesture to the keyboard button
            for g, k in gestures_keys.items():
                AssignKeyToGesture(g, k)

            if MakeScreenshot:
                sc = pyautogui.screenshot()
                time_now = datetime.datetime.now()
                str_time = '{}_{}'.format(time_now.hour, time_now.minute)
                sc.save('screenshot{}{}.png'.format(str_time, uuid.uuid4()))
            if TurnOn_Whatsapp:
                webbrowser.open('https://www.whatsapp.com/')

            # press Q or make 'Okay' to stop the program
            if cv2.waitKey(1) == ord('q') or isOff:
                On_Main_While = False
                break


        cap.release()
        cv2.destroyAllWindows()


#The rest of the buttons

# Turn on/off button
TurnOnOffButton = Button(text='On', command=switch)
TurnOnOffButton.config(height='4', width='300')
TurnOnOffButton.pack()

# Open Github page ( Projekt na 6 )
def openGithub():
    webbrowser.open('https://github.com/KryhaX/Projekt_na_6')

# Github Button
GithubButton = Button(text='Github', command=openGithub)
GithubButton.config(height='4', width='300')
GithubButton.pack()

# Exit Function
def Exit():
    GUIwindow.destroy()

# Exit Button
ExitButton = Button(text='Exit', command=Exit)
ExitButton.config(height='4', width='300')
ExitButton.pack()


# GUI mainloop
GUIwindow.mainloop()