# Golden Teacher by Krystian Wierciak

import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
import pyautogui
import datetime
import uuid
from tkinter import *
import webbrowser

# Function and name gesture
print('''
Main Gesture: 
okay - screenshot
peace - slideLeft
thumbs up - scroll up
thumbs down - scroll up
call me - turn_on_whatsapp
stop - space
rock - Quit GoldenTeacher.py
fist - slide right
''')
TITLE = 'Golden Teacher'
GUI_SIZE = '400x475'
button_height = '4'
button_width = '300'
whatsapp_url = 'https://www.whatsapp.com/'
github_url = 'https://github.com/KryhaX/Projekt_na_6'

gui_window = Tk()
gui_window.title(TITLE)
gui_window.geometry(GUI_SIZE)
gui_window.config(bg='gold')

label_title = Label(
    gui_window,
    text=TITLE,
    bg="gold",
    fg="black",
    font=('Helvetica', 10, 'bold'),
    width=20,
    height=5,
    borderwidth=5,
    relief='sunken'
)
label_title.pack()

global is_on
is_on = True

global make_screenshot
make_screenshot = None

global turn_on_whatsapp
turn_on_whatsapp = None

global is_off
is_off = None

on_main_while = False


# Switching a color of on/off button | Turned on/off main program
def switch():
    global is_on
    if is_on:
        turn_on_off_button.config(bg='green', text='Now is on')
        is_on = False
    elif not is_on:
        turn_on_off_button.config(bg='red', text='Now is off')

        # initialize mediapipe
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mp_draw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
        model = load_model('mp_hand_gesture')

        # Load class gesture names
        with open('gesture.names', 'r') as f:
            class_names = f.read().split('\n')

        # Function and name gesture
        print('''
        Main Gesture: 
        okay - screenshot
        peace - slideLeft
        thumbs up - scroll up
        thumbs down - scroll up
        call me - turn_on_whatsapp
        stop - space
        rock - Quit GoldenTeacher.py
        fist - slide right
        ''')

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        global on_main_while
        on_main_while = True
        # Main Loop
        while on_main_while:
            # Read frame's
            _, frame = cap.read()
            x, y, c = frame.shape

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get hand landmark prediction
            result = hands.process(frame_rgb)

            class_name = ''

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
                    mp_draw.draw_landmarks(frame, handslms, mp_hands.HAND_CONNECTIONS)

                    # Predict gesture
                    prediction = model.predict([landmarks])

                    class_id = np.argmax(prediction)
                    class_name = class_names[class_id]

            # show the prediction on the frame
            cv2.putText(
                frame,
                class_name,
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
                cv2.LINE_AA
            )

            # Window of command of gesture view
            cv2.imshow("{} View ( press q to Quit ) ".format(TITLE), frame)

            gestures_keys = {
                'screenshot': 'screenshot',
                'slideLeft': 'left',
                'up': 'up',
                'down': 'down',
                'turn_on_whatsapp': 'turn_on_whatsapp',
                'stop': 'space',
                'close': 'q',
                '_space': 'space',
                'slideRight': 'right',
                'Stop': 'space'
            }

            global make_screenshot
            global turn_on_whatsapp
            global is_off

            def assign_key_to_gesture(gesture, key):
                if class_name == gesture:
                    print(gesture)
                    pyautogui.press([f'{key}'])
                    pyautogui.sleep(1)

                elif class_name == 'close':
                    global is_off
                    is_off = True

                elif class_name == 'screenshot':
                    global make_screenshot
                    make_screenshot = True

                elif class_name == 'turn_on_whatsapp':
                    global turn_on_whatsapp
                    turn_on_whatsapp = True


            # Assignment Gesture to the keyboard button
            for g, k in gestures_keys.items():
                assign_key_to_gesture(g, k)

            if make_screenshot:
                sc = pyautogui.screenshot()
                time_now = datetime.datetime.now()
                str_time = '{}_{}'.format(time_now.hour, time_now.minute)
                sc.save('screenshot{}{}.png'.format(str_time, uuid.uuid4()))
                make_screenshot = False
            if turn_on_whatsapp:
                webbrowser.open(whatsapp_url)
                turn_on_whatsapp = False

            # press Q or make 'Okay' to stop the program
            if cv2.waitKey(1) == ord('q') or is_off:
                on_main_while = False
                break

        cap.release()
        cv2.destroyAllWindows()


turn_on_off_button = Button(text='On', command=switch)
turn_on_off_button.config(height=button_height, width=button_width)
turn_on_off_button.pack()


def open_github():
    webbrowser.open(github_url)


github_button = Button(text='Github', command=open_github)
github_button.config(height=button_height, width=button_width)
github_button.pack()


def close():
    gui_window.destroy()


close_button = Button(text='close', command=close)
close_button.config(height=button_height, width=button_width)
close_button.pack()

gui_window.mainloop()
