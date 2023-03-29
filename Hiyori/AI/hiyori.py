import time
import gtts
from gtts import langs
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound, PlaysoundException
import random
import os
from kivy.uix.screenmanager import Screen
import dataManager
import hiyoriResponse

r = sr.Recognizer()
langswitch = "en"
htext = "value"
errorFlag = True
processLabelFlag = True
eventLabelFlag = True

class Hiyori():
 
    def __init__(self,mysentence, hsentence, **kwargs):
        super(Hiyori, self).__init__()
        self.mysentence = mysentence
        self.hsentence = hsentence
    
    def listenningText(self):
        
        data = input("listenning...\n")
        
        self.mysentence = data
        return self.mysentence
        
    def speakingText(self):
        global htext, screens
        htext = self.hsentence
        print(htext)
        return htext
  
    def response(self):
        global htext
        if self.mysentence != None:
            dataManager.setter("pattern", self.mysentence)
            hiyoriResponse.zeynep()
            self.hsentence = dataManager.getter("response")
        elif self.mysentence == "exit":
            exit()
        htext = str(self.hsentence)  
        return htext

    def mainText(self):
        self.listenningText()
        self.response()
        self.speakingText()

    def listenning(self):
        global errorFlag
        
        print("Hiyori listennig")
        
        with sr.Microphone() as source:   
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language= langswitch)
            except sr.UnknownValueError:
                print("system unknown value error--> sentence is not understanding")
                self.hsentence = "system unknown error, please repeat"
                self.speaking()
                errorFlag = False
            except sr.RequestError:
                print("system request error")
            voice = voice.lower()
            self.mysentence = voice
            print(voice)
        print("checkpoint")
        dataManager.setter("pattern", voice)
        return voice
    

        
    def speaking(self):
        
        rand = random.randint(1,10000)
        try:
            tts = gTTS(text = self.hsentence, lang = langswitch, slow= False)
            file = 'audio-'+str(rand)+'.mp3'
            tts.save(file)
        except AssertionError:
            return False
        try:
            playsound(os.getcwd() + "\\" + file)
            time.sleep(0.2)
            os.remove(file)
        except PlaysoundException:
            return False
        return self.hsentence

    def closeProject(self):
        exit()

    def main(self):
        self.listenning()
        self.response()
        self.speaking()



hiyori = Hiyori("", "")

class App(Screen):
    def __init__(self):
        super(App, self).__init__()
    def main(self):
        global hiyori
        hiyori.main()
    def change_text(self):
        global textFlag
        if processLabelFlag == True:
            self.processLabel.text = "Processing..." 
            textFlag = False
        else:
            self.processLabel.text = " "
            textFlag = True
