# from plyer import notification
import pyttsx3


# notification.notify(
#     title="Hello World!",
#     message="hello world",
#     timeout=5  
# )


engine = pyttsx3.init()

engine.say("Call of duty modern warfare 4 2026")
engine.runAndWait()
