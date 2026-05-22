import speech_recognition as sr
import pyttsx3

class JarvisSpeech:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        # Set professional voice attributes
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id) # Default local system voice
        self.engine.setProperty('rate', 175) # Clear speaking pace
    
    def speak(self, text):
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        with sr.Microphone() as source:
            print("\nListening for voice pulse...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Processing audio signal...")
                command = self.recognizer.recognize_google(audio)
                print(f"User Pulse: {command}")
                return command.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                print("Signal distorted: Speech unrecognized.")
                return ""
            except Exception as e:
                print(f"Hardware Link Error: {e}")
                return ""
