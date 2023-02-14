import cv2
import time
import datetime
import imutils
import pyttsx3 as tts
import numpy as npy

textSpeech = tts.init()


def Rcrd():
    vid = cv2.videoCapture(0)

    while True:

        ret, frame = vid.read()

        cv2.imshow('Autopilot Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('p'):
            break

    vid.release()
    cv2.destroyAllWindows()


def motionDect():
    video = cv2.VideoCapture(0)
    time.sleep(2)
    firstFrame = None

    print("Camera Opened!")
    textSpeech.say("Camera Opened!")
    textSpeech.runAndWait()

    while True:
        frame = video.read()[1]
        text = "No vehicle detected"

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gaussianFrame = cv2.GaussianBlur(grayFrame, (21, 21), 0)
        blurFrame = cv2.blur(gaussianFrame, (5, 5))

        grayImage = blurFrame

        if firstFrame is None:
            firstFrame = grayImage
        else:
            pass

        frame = imutils.resize(frame, width=500)
        deltaFrame = cv2.absdiff(firstFrame, grayImage)
        thresh = cv2.threshold(deltaFrame, 100, 225, cv2.THRESH_BINARY)[1]

        dilateImage = cv2.dilate(thresh, None, iterations=2)

        cnt = cv2.findContours(dilateImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        for c in cnt:
            if cv2.contourArea(c) > 800:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Vehicle detected"
            else:
                pass

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'[+] Status: {text}', (12, 24), font, 0.5, (0, 0, 0), 2)

        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), font, 0.35, (128, 0, 0), 1)

        cv2.imshow("Raaha", frame)
        cv2.imshow("Backend", gaussianFrame)
        cv2.imshow("Backend", grayFrame)
        cv2.imshow("Backend", grayImage)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("p"):
            print("Camera Closed!")
            textSpeech.say("Camera Closed!")
            textSpeech.runAndWait()

            cv2.destroyAllWindows()
            break


'''
def vehicleD():
    # capture frames from a video
    cap = cv2.VideoCapture('video.avi')

    # Trained XML classifiers describes some features of some object we want to detect
    car_cascade = cv2.CascadeClassifier('cars.xml')

    # loop runs if capturing has been initialized.
    while True:
        # reads frames from a video
        ret, frames = cap.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        # To draw a rectangle in each cars
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display frames in a window
    cv2.imshow('Raaha', frames)


# De-allocate any associated memory usage
cv2.destroyAllWindows()
'''
