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
textSpeech.say(current_time)
textSpeech.runAndWait()

# Basic calculation for system check
va = 60
vb = 69
vc = va * vb


# def = function, pStart is the name of the function
def pStart(pass_=dataB.pass_):
    print("System okay")
    textSpeech.say("System Okay!")
    textSpeech.runAndWait()

    textSpeech.say("Enter Password to Start: ")
    textSpeech.runAndWait()
    __pass__ = input("Enter Password to Start: ")

    if __pass__ != pass_:
        print("wrong password, Try again!")
        textSpeech.say("wrong password, Try again!")
        textSpeech.runAndWait()

        textSpeech.say("Initiating Password Recovery Function")
        textSpeech.runAndWait()

        print("Initiating Password Recovery Function")
        forgotPass()
    else:
        pPro()


def pPro(user=dataB.user_):
    print("welcome " + user)
    textSpeech.say("Welcome" + user)
    textSpeech.runAndWait()

    print("Starting Camera!")
    textSpeech.say("Starting Camera!")
    textSpeech.runAndWait()

    cam.motionDect()


def pClose():
    quit()
    print("Errors in system")


def forgotPass(pass_=dataB.fPass_):
    __mQ__ = input("What's my imaginary dog name ?")
    if __mQ__ != pass_:
        textSpeech.say("Wrong answer!")
        textSpeech.runAndWait()

        print("Wrong Answer")
        quit()
    else:
        textSpeech.say("Enter new password")
        textSpeech.runAndWait()

        __nP__ = input("Enter new password : ")
        pPro()


if vc == 4140:
    pStart()
else:
    pClose()
