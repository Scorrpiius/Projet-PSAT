# Open intersection.txt and read it, word by word

# Open the file
with open('intersection.txt', 'r', encoding="utf-8") as f:
    words = f.read().split()

print(len(words))

# Read with tts and play the word
import pyttsx3
import time
import random

engine = pyttsx3.init()
engine.setProperty('rate', 170)     # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)   # Volume 0-1

# Shuffle the words
random.shuffle(words)
counter = 0
for word in words:
    engine.say(word)
    engine.runAndWait()
    engine.stop()

    # LOG THE OUTPUT OF THE COMMAND WITH THE WORD
    with open('log_words.csv', 'a', encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{word}\n")