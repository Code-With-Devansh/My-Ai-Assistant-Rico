import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import vlc
from PyDictionary import PyDictionary
from mutagen.mp3 import MP3
import time
import requests
import json
import time
class Bot:
    def greet():
        hour = datetime.datetime.now().hour
        if hour>=12 and hour<16:
            Bot.speakGirl("Good Afternoon Sir")
        elif hour>=16 and hour<24:
            Bot.speakGirl("Good Evening Sir")
        elif hour>=0 and hour<12:
            Bot.speakGirl("Good Morning Sir")
    def getInput() ->str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    def speakGirl(str):
        engine = pyttsx3.init('sapi5')
        voices= engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        print(str)
        engine.say(str) 
        engine.runAndWait()

    def speak(str):
        engine = pyttsx3.init()
        engine.say(str)
        print(f"Bot: {str}")
        engine.runAndWait()
    def getFiles(list) -> list:
        newList = []
        for item in list:
            if '.mp3' in item:
                newList.append(item)
        return newList
    def getCommandMusic():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.5
            r.energy_threshold = 500
            r.non_speaking_duration = 0.3
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            return "None"
        return query
    def playMusic(self, musicPath):
        startTime = time.time()
        audio = MP3(musicPath)
        time.localtime()
        while True:
            if time.time() - startTime < audio.info.length:
                query = Bot.getCommandMusic().lower().replace("rico", '')
                if "stop" in query:
                    self.player.stop()
                    break
            else: 
                return
    def getNews(self):
        apiKey = 'f9da9cefd5c54983a49ed363e07d279d'
        str = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}')
        str = str.text
        self.dictstr = json.loads(str)
    def Playnews(self):
        results = len(self.dictstr['articles'])
        if self.newsIndex<results:
            Bot.speakGirl("starting the news...")
            art = self.dictstr['articles']
            Bot.speakGirl(art[self.newsIndex]['title'])
            print("click to know more: ", art[self.newsIndex]['url'])
            print()
            Bot.speakGirl("Moving on to the next News...")
            self.newsIndex +=1
    def __init__(self) -> None:
        Bot.greet()
        self.newsIndex = 0
        while True:
            query = Bot.getInput().lower().replace("rico", '')
            if query == 'none':
                 pass
            elif query == '':
                Bot.speakGirl("Hello, I am Rico. How can I help you")
            elif query =='none':
                pass
            elif "news" in query:
                self.getNews()
                while True:
                    self.Playnews()
                    print("If you don't want to listen more news say stop! else ignore this message.")
                    temp =  Bot.getCommandMusic()
                    if "stop" in temp:
                        break
                    elif temp == 'none':
                        continue
                    else:
                        continue
                
            elif "what is" in query:
                dict = PyDictionary()
                Bot.speakGirl(dict.meaning(query.replace("what is", '')))
            elif "exit" in query:
                Bot.speakGirl("Thank you for using me!")
                exit()
            elif "quit" in query:
                Bot.speakGirl("Thank you for using me!")
                exit()
            elif "day" in query:
                now = datetime.datetime.now()
                Bot.speakGirl(now.strftime("%A"))
            elif "time" in query:
                now = datetime.datetime.now()
                Bot.speakGirl(now.strftime("%I:%M %p"))
            elif "date" in query:
                now = datetime.datetime.now().strftime("%d %B, %Y")
                Bot.speakGirl(now)
            elif "hello" in query:
                Bot.speakGirl("Hii, I am Rico how can I help you")
            elif "about you" in query:
                Bot.speakGirl("Hii, I am Rico. I was made by Devansh from Mars. Email - devanshpc7017@gmail.com")
            elif "how are you" in query:
                Bot.speakGirl("I am fine, how about you.")
            elif "wikipedia" in query:
                Bot.speakGirl("Searching Wikipedia...")
                Bot.speakGirl(wikipedia.summary(query.replace("wikipedia", ""),sentences=2))
            elif "open youtube" in query:
                urL = "http://youtube.com"
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
                webbrowser.get('chrome').open_new_tab(urL)
            elif "google" in query:
                link = "https://www.google.com/search?q=<SEARCH>"
                urL = link.replace("<SEARCH>", query.replace('google', ""))
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
                webbrowser.get('chrome').open_new_tab(urL)
            elif "play music" in query:
                path = "F:\Devansh\Songs"
                music = os.listdir(path)
                musicFiles = Bot.getFiles(music)
                musicPath = os.path.join(path,musicFiles[random.randrange(len(musicFiles))])
                self.player = vlc.MediaPlayer(musicPath)
                self.player.play()
                self.playMusic(musicPath) 
            elif "search on youtube" in query:
                urL = "https://www.youtube.com/results?search_query=<search>"
                link = urL.replace("<search>", query.replace("search on youtube", ""))
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
                webbrowser.get('chrome').open_new_tab(link)
            else:
                link = "https://www.google.com/search?q=<SEARCH>"
                urL = link.replace("<SEARCH>", query)
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
                webbrowser.get('chrome').open_new_tab(urL)
Bot()
