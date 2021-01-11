from __future__ import print_function
from playsound import playsound
import datetime
import pickle
import os.path
import wikipedia
import wolframalpha
import webbrowser
import random
import requests
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import sys
import json
 
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('PVGTUT-KUA9GXGHLT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 2].id)

def speak(text):
    print('Maya: ' + text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    global said
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)        
        audio = r.listen(source)
        try:
            
            said = r.recognize_google(audio, language='en-in')
    
            print('User:' + said + '\n')
        except Exception as e:
            print("Exception: " + str(e))

    return said






def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        speak('Good Morning Sir!')

    elif CurrentHour >= 12 and CurrentHour < 18:
        speak('Good Afternoon Sir!')

    elif CurrentHour >= 18 and CurrentHour != 0:
        speak('Good Evening Sir!')

WAKE = "maya"
greetMe()
print("Start")

while True:
    print("Listening")
    text = get_audio()
    text = text.lower()

    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()

        if "hello" in text:
            speak("hi")

        if'open google' in text:
            speak('sure')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in text:
            speak('sure')
            webbrowser.open('www.gmail.com')
                    
        elif 'open youtube' in text:
            speak('sure')
            webbrowser.open('www.youtube.com')
        
        elif ' who is Samarth ' in text:
            speak('samarth verulkar is my master let me open his page')
            webbrowser.open('www.samarthverulkar.blogspot.com')

        elif ' who is yash ' in text:
            speak('yash singh is my master let me open his page')
            webbrowser.open('www.samarthverulkar.blogspot.com')
        

        elif "what\'s up" in text or 'how are you' in text:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power', 'I am at your service sir!']
            speak(random.choice(setReplies))
               
        elif "who are you" in text or 'where are you' in text or 'what are you' in text:
            setReplies = [' I am Maya', 'In your system', 'I am an AI']
            speak(random.choice(setReplies))
        elif 'nothing' in text or 'goodbye' in text or 'bye' in text:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()

        elif 'the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'hello' in text or 'hey' in text or 'hey Maya' in text or 'hi Maya' in text or 'hello Maya' in text or 'hi' in text:
            setReplies = [' hi Master', 'hello Master', 'at your service my Mas', 'hey ']
            speak(random.choice(setReplies))            
                        
        elif 'what is the current weather of' in text:
            text = text.replace('what is the current weather of' , '')
            city = (text)
            speak('Fetching results please wait')

            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=58f5e0be70c54ab5d6be2b0f2eef3084'.format(city)

            json_data = requests.get(url) .json() 
            temp = json_data ['main']['temp']
            wind_speed = json_data['wind']['speed']
            description = json_data['weather'][0]['description']   
            speak('Temperature : {} degree celcius'.format(temp))
            speak('Wind Speed : {} m/s'.format(wind_speed))
            speak('Description : {}'.format(description))                
        
        elif 'joke' in text:
            
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
        elif 'the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
   
        
        elif 'who is your creator' in text or 'who created you' in text or 'what is the name of your creator' in text or 'who is your creator Maya' in text or 'who built you' in text:
            speak('I was programmed by Yash Singh and Samarth Verulkar, they are students in high school and they are also a arduino and python developer')

        elif 'set alarm'in text:
            os. system('clear')
            speak("What hour do you want the alarm to ring? ")
            alarmH = int(input(get_audio))
            alarmM = int(input("What minute do you want the alarm to ring? "))
            amPm = str(input("am or pm? "))
            os. system('clear')
            print("Waiting for alarm",alarmH,alarmM,amPm)
            if (amPm == "pm"):
                alarmH = alarmH + 12
            while(1 == 1):
                if(alarmH == datetime.datetime.now().hour and
                   alarmM == datetime.datetime.now().minute) :
                   print("Time to wake up")
                   playsound(r'C:\Users\ASUS\Documents\music\Ritviz - Sage [Official Music Video].mp3')
                   break

            

        else:
            text= text
            speak('Please wait till I get the answer to your question')
            try:
                try:
                            
                    app_id = 'PVGTUT-KUA9GXGHLT'
                    client = wolframalpha.Client(app_id)
                    res = client.query(text)
                    outputs = next(res.results).text
                    speak('Gotcha')
                    speak('Fetching results')
                    speak(outputs)

                except:
                    
                    outputs = wikipedia.summary(text, sentences=3)
                    speak('Gotcha')
                    speak('Fectching results')
                    speak(outputs)


            except:
                speak("searching for" +  text)
                say = text.replace(' ', '+')
                webbrowser.open('https://www.google.co.in/search?q=' + text)


                


            setReplies = ['Anything else you want me to do Master?', 'Is there anything else I can do for you Master?', 'What are my next commands my Master?']
            speak(random.choice(setReplies))     
