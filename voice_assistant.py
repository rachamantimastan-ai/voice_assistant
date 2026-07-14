import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os

recognizer = sr.Recognizer()

def speak(text):
    print("Bot:", text)
    engine = pyttsx3.init(driverName="sapi5")# Windows
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen_command():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available right now.")
        return ""
    except Exception as e:
        print("Error:", repr(e))
        speak("Something went wrong.")
        return ""

def open_app_or_website(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open chat gpt" in command or "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen(["calc.exe"])

    elif "open paint" in command:
        speak("Opening Paint")
        subprocess.Popen(["mspaint.exe"])

    elif "open command prompt" in command or "open c m d" in command:
        speak("Opening command prompt")
        subprocess.Popen(["cmd.exe"])

    elif "who are you" in command:
        speak("I am your basic Python voice assistant.")

    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye. See you again.")
        return False

    elif command != "":
        speak("Command received, but I do not know that one yet.")

    return True

def main():
    speak("Hello. I am ready. Say a command.")
    running = True

    while running:
        command = listen_command()
        running = open_app_or_website(command)

if __name__ == "__main__":
    main()