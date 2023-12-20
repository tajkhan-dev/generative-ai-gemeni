import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voices',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speech_recognition():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        rec.pause_threshold=1
        audio = rec.listen(source,0,8)

    try:
        print("Speech recognizing ...")
        query = rec.recognize_google(audio,language="english")
        return query.lower()
    except:
        return "None"

genai.configure(api_key='YOUR API KEY HERE')


        
model = genai.GenerativeModel('gemini-pro')


def check_wake_word():
    while True:
        speech = speech_recognition().lower()
        if "hello jarvis" in speech:
            return True
        else:
            text_to_speech("Unauthorized voice")
            print("Try saying 'Hello Jarvis'")
            return False

def assistant_interaction():
    while check_wake_word():
         query = speech_recognition().lower()
         if query == "off":
            break
         response = model.generate_content(query)
         text_to_speech(response.text)

# Start assistant interaction
assistant_interaction()