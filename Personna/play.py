import csv
import pyttsx3
from datetime import datetime
from nltk.tokenize import sent_tokenize

# Download the necessary NLTK data for French
# nltk.download('punkt')
# nltk.download('punkt_tab')

# Function to log the time and sentence
def log_time_and_sentence(sentence):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a') as log_file:
        log_file.write(f"{current_time} - {sentence}\n")

def say(text) :
    # Initialize the TTS engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_frFR_PaulM')

    
    # Split the text into sentences (French)
    sentences = sent_tokenize(text, language='french')
    for sentence in sentences:
        print(sentence)
        # Speak the sentence
        engine.say(sentence)
        engine.runAndWait()
        # Log the time and sentence
        log_time_and_sentence(sentence)