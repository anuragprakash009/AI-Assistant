import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
from word2number import w2n
import random
import json
import requests 
from urllib.request import urlopen
import wolframalpha
import time
engine = pyttsx3.init()
wolframalpha_app_id ="2XUEWP-XPRQLYAYJ9"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Anurag Prakash!")
    time_()
    speak("and")
    date_()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !")
    elif hour>=18 and hour<24:    
        speak("Good Evening Sir !")
    else:
        speak("Good Night Sir !")
    speak("Jarvis at your service. Please tell me how can I help you today ?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.adjust_for_ambient_noise(source, duration=1) 
        #r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing..........")
            query = r.recognize_google(audio, language='en-US')
            print("You just said: "+query)
        except Exception as e:
            print(e)

            print("Say that again please.....")
            return "None"
        return query  

def sendEmail(to, content) :
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    
    server.login('wshadow884@gmail.com','@Snlj')
    server.sendmail('wshadow884@gmail.com',to,content)
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)
    print('CPU is at '+usage)
    speak('and')
    battery = psutil.sensors_battery()
    speak('Battery is at')
    print('Battery is at '+ str(battery.percent))
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/anura/OneDrive/Pictures/Screenshot.png')
if __name__ == "__main__":
    wishme()
    while True:
        query = TakeCommand().lower()
        
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("Searching.....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'email' in query:
            try:
                speak("What should I say ?")
                content=TakeCommand()
                speak("Who is the Reciever ?")
                receiver=input("Enter Reciever's Email: ")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak("email has been sent...")
            except Exception as e:
                print(e)
                speak("Unable to send email...")
        elif 'search in chrome' in query:
            speak('What should I search ?')
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak("what should I search ?")
            search_Term = TakeCommand().lower()
            speak("Here we go to YOUTUBE !")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'google search' in query:
            speak("what should I search ?")
            search_Term = TakeCommand().lower()
            speak("Searching on Google !")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'status' in query:
            cpu()

        elif 'joke' in query:
            joke()
        
        elif 'go offline' in query:
            speak('Going offline sir.......')
            quit()

        elif 'word' in query:
            speak("Opening MS Word.....")
            ms_word = r'C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.exe'
            os.startfile(ms_word)
        elif 'write a note' in query:
            speak('What should I write, Sir ?')
            notes = TakeCommand()
            file = open('notes.txt','a')
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(':-')
            file.write(notes+"\n")

            speak("Done Taking Notes, Sir !")

        elif 'show notes' in query:
            speak("showing notes....")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
        
        elif 'capture' in query or 'screenshot' in query:
            screenshot()
            speak("Screenshot has been taken sir !")
        
        elif 'play music' in query:
            songs_dir = os.path.abspath(os.getcwd())+"/"+"songs"
            music = os.listdir(songs_dir)
            num = 1
            for i in music:
                print(str(num)+" -> "+i)
                num=num+1
            speak("What should I play ?, Please tell me a number")
            speak("Or say choose yourself")
            ans = TakeCommand().lower()
            if 'random' or 'choose yourself' in ans:
                print("Random")
                no = random.randint(1,len(music))
                print("plating song number "+str(no))
            else:
                no = int(w2n.word_to_num(ans.replace('number','')))
            os.startfile(os.path.join(songs_dir,music[no-1]))
        
        elif 'remember that' in query:
            speak("What shoud I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that "+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt')
            speak("You asked me to remember that "+remember.read())
        
        elif 'news' in query:
            try:
                jsonObj = str(urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=9b11d918181a4fbeb1dd6a704c8b032d"))
                data = json.load(jsonObj)
                print(jsonObj)
                print(data)
                i=1
                speak("Here are some top headlines")
                print("##############TOP HEADLINES##################")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i=i+1
            except Exception as e:
                    print(str(e))
                    speak("Sorry could not fetch news")

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("You Just asked to locate "+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            try:       
                client = wolframalpha.Client(wolframalpha_app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(''.join(query))
                answer = next(res.results).text
                print('The Answer is '+answer)
                speak('The Answer is '+answer)        
            except Exception as e:
                print(e)
                speak("Could not Calculate, please try again !")
        
        elif 'what is' in query:
            try:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception as e:
                print(e)
                speak("Please try again !") 

        elif 'stop listening' in query:
            try:
                speak("For How Many Seconds you want me to stop listing to your commands ?")
                com = TakeCommand().lower()
                print(com)
                ans = int(w2n.word_to_num(com))
                time.sleep(ans)
                print("Going to sleep for "+str(ans)+" seconds")
                speak("Going to sleep for "+str(ans)+" seconds") 
            except Exception as e:
                print(e)
                speak("Could not understand please try again !")
        