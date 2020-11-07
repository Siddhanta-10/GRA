import cv2
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import pyautogui as pag
from plyer import notification


application_toggle = True
print('Application is turned ', 'ON' if application_toggle else 'OFF')

list_of_gestures = []

_file = open("converted_keras/labels.txt", "r")
lines = _file.readlines()
for line in lines:
    line = line.strip()
    if(line != ""):
        print(line)
        list_of_gestures.append(line.split(' ')[1])

print(list_of_gestures)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('converted_keras/keras_model.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


capture = cv2.VideoCapture(0)
print('width: ', capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height: ', capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

one_active = False
swipe_down_active = False
swipe_up_active = False
swipe_right_active = False
swipe_left_active = False

pinch_in_given = False
pinch_out_given = False
two_fingers_left_given = False
two_fingers_right_given = False

while True:
    # Read the camera
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    roi = frame[100:480, 300:640]

    cv2.imwrite('temp.jpg', roi)

    # Replace this with the path to your image
    image = Image.open('temp.jpg')

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # print(prediction)

    gestures = dict(zip(list_of_gestures, prediction[0]))
    # print(gestures)
    detection = max(gestures, key=gestures.get)
    if application_toggle == True:
        print(detection)

    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, detection, (0, 140), font, 2, (0, 0, 0), 3, cv2.LINE_AA)

    if True:
        if detection == 'swipe_down':
            if swipe_down_active == False:
                if application_toggle:
                    pag.hotkey('win', 'd')
            elif swipe_down_active == True:
                pass
            elif swipe_up_active == True:
                if application_toggle:
                    pag.hotkey('win', 'tab')
            swipe_down_active = True

        elif detection == 'swipe_up':
            if swipe_up_active == False:
                if application_toggle:
                    pag.hotkey('win', 'tab')
            elif swipe_up_active == True:
                pass
            elif swipe_down_active == True:
                if application_toggle:
                    pag.hotkey('win', 'd')
            swipe_up_active = True

        # elif detection == 'two_fingers_left':
        #     if swipe_left_active == False and swipe_up_active == False:
        #         if application_toggle:
        #             pag.hotkey('ctrl', 'win', 'left')
        #     elif swipe_left_active == True:
        #         pass
        #     swipe_left_active = True
        #
        # elif detection == 'two_fingers_right':
        #     if swipe_right_active == False and swipe_up_active == False:
        #         if application_toggle:
        #             pag.hotkey('ctrl', 'win', 'right')
        #     elif swipe_right_active == True:
        #         pass
        #     swipe_right_active = True

        elif detection == 'pinch_in':
            pinch_in_given = True
            if pinch_out_given == True:
                if application_toggle:
                    pag.hotkey('ctrl', '-')
                pinch_out_given = False
                pinch_in_given = False

        elif detection == 'pinch_out':
            pinch_out_given = True
            if pinch_in_given == True:
                if application_toggle:
                    pag.hotkey('ctrl', '+')
                pinch_out_given = False
                pinch_in_given = False

        elif detection == 'two_fingers_left':
            two_fingers_left_given = True
            if two_fingers_right_given == True:
                if application_toggle:
                    pag.hotkey('ctrl', 'win', 'right')
                two_fingers_left_given = False
                two_fingers_right_given = False

        elif detection == 'two_fingers_right':
            two_fingers_right_given = True
            if two_fingers_left_given == True:
                if application_toggle:
                    pag.hotkey('ctrl', 'win', 'left')
                two_fingers_left_given = False
                two_fingers_right_given = False

        elif detection == 'one':
            if one_active == False:
                application_toggle = not application_toggle
                print('Application is turned ', 'ON' if application_toggle else 'OFF')
                notification.notify(
                    title='GRA',
                    message='Gestures have been turned ON' if application_toggle else 'Gestures have been turned OFF',
                    timeout=5,  # seconds
                )
            else:
                pass
            one_active = True
        elif detection == 'None':
            one_active = False
            swipe_down_active = False
            swipe_up_active = False
            swipe_right_active = False
            swipe_left_active = False

            pinch_out_given = False
            pinch_in_given = False
            two_fingers_left_given = False
            two_fingers_right_given = False

    # Display
    cv2.imshow('Original', frame)
    cv2.imshow('ROI', roi)

    # Exit handle
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

    if (cv2.waitKey(1) & 0xFF) == ord('s'):
        cv2.imwrite('image_save.jpg', frame)

# Release resources
capture.release()
cv2.destroyAllWindows()