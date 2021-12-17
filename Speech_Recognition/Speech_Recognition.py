import pyttsx3 #pip install pyttsx3 and pip install speechRecognition
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia                                      #install
import os
import smtplib
import pythoncom
import pyaudio
from PyDictionary import PyDictionary
engine = pyttsx3.init('sapi5')
#inbuilt voice that u can use
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice' , voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Evening!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how can I help you sir")
def takeCommand(): #sppeech recognition
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()  #its a class which helps in recognizing audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   #second of nonspeaking audio before phrase is complete while I am speaking if I wait for 1 sec then it shoul not terminate
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio , language = 'en-in')
        print(f"User said: {query}")
    except Exception as e:
        #print(e)
        print("Say that again please")
        #return "None"
    return query
def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login('your email' , 'your password')
    server.sendmail('your email' , to , content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            speak("Any other services that you want from me")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("I have opened my friend")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("I have opened bro")
        elif 'play music' in query:
            print("I dont have any music list for now")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #represent in string format
            speak(f"The time is {strTime}")
        elif 'email to Jainam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jainamdoshi00@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except:
                speak("Sorry I am not able to send Jainam bhai")
        elif 'open dictionary' in query or 'dictionary' in query:
            speak("What word should I look up for?")
            word = takeCommand()
            dictionary = PyDictionary()
            res = dictionary.meaning(word)
            print(res)
            speak(res)
            print(dictionary.synonym(word))

        else:
            print("done")


