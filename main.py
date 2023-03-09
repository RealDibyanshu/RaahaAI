from datetime import datetime
import pyttsx3 as tts
import cam
import database as dataB
import arduino as myA

textSpeech = tts.init()
voice = textSpeech.getProperty('voices')
textSpeech.setProperty('voice', voice[0].id)

arduinoAI = myA

timeNow = datetime.now()
current_time = timeNow.strftime("%H:%M:%S")

print("Time: ", current_time)

# Basic calculation for system check
va = 60
vb = 69
vc = va * vb

enterPass = dataB.enterPass


# def = function, pStart is the name of the function
def pStart():
    print("System okay")

    enterPassword()


def pPro(user=dataB.user_):
    print("welcome " + user)
    textSpeech.say("Welcome" + user)
    textSpeech.runAndWait()

    print("Starting Camera!")

    cam.motionDect()


def pClose():
    quit()
    print("Errors in system")


def enterPassword(pass_=dataB.pass_):
    count = 0
    tries = 5
    while count < 5:
        _pass_ = int(input("Enter Password: "))
        if _pass_ == pass_:
            print("Access Granted")
            pPro()
        else:
            print("Access denied, Maximum tries reached")


if vc == 4140:
    pStart()
else:
    pClose()
