# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and speaker
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Network error. Try again.")
        return None

def calculate(expression):
    expression = expression.replace("plus", "+").replace("minus", "-")
    expression = expression.replace("into", "*").replace("times", "*")
    expression = expression.replace("divide", "/").replace("by", "/")
    try:
        return eval(expression)
    except:
        return None

def main():
    speak("Hello mathesh! I am your voice calculator. Please say your expression.")
    while True:
        text = get_audio()
        if text:
            if "exit" in text or "stop" in text or "quit" in text:
                speak("Goodbye!")
                break
            result = calculate(text)
            if result is not None:
                print(f"Result: {result}")
                speak(f"The result is {result}")
            else:
                speak("Sorry, I couldn't calculate that.")
        else:
            speak("Please say that again.")

if __name__ == "__main__":
    main()
