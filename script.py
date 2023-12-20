import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voices',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold=1
        audio = r.listen(source,0,8)

    try:
        print("Speech recognizing ...")
        query = r.recognize_google(audio,language="english")
        return query.lower()
    except:
        return "None"

genai.configure(api_key='YOUR API KEY HERE')

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
        
model = genai.GenerativeModel('gemini-pro')

# while True:
#     awake = speechrecognition().lower()
#     if "hello jarvis" in awake:
#         while True:
#             Query = response = model.generate_content(speechrecognition())
#             speak(Query.text)
#             if Query == "off":
#                 break
                
#     else:
#         speak("un-Authorized voice")
#         print("Try Hello Jarvis")

def check_wake_word():
    while True:
        awake = speechrecognition().lower()
        if "hello jarvis" in awake:
            return True
        else:
            speak("Unauthorized voice")
            print("Try saying 'Hello Jarvis'")
            return False

def assistant_interaction():
    while check_wake_word():
        while True:
            query = speechrecognition().lower()
            if query == "off":
                break
            response = model.generate_content(query)
            speak(response.text)

# Start assistant interaction
assistant_interaction()