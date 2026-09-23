import pyttsx3

engine = pyttsx3.init()

names = ["Shakira", "Princess Leonor", "Infanta Sofia", "Lamine Yamal", "Cristiano Ronaldo"]

for name in names:
    engine.say(f"Shoutout to {name}")

engine.runAndWait()