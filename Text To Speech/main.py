from gtts import gTTS
import os

file = open("speech.txt", "r")
myText = file.read().replace("\n", "")
language = 'en'

output = gTTS(text=myText, lang = language, slow = False)
output.save("output.mp3")

file.close()

os.system("output.mp3")
