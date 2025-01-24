from generate_text2 import generate_text
from load_and_play import say
import time

# PERSONNA
personna = "Kevin, 22 ans, passionné de football qui joue dans l'équipe du coin."

# USER PROMPT
user_prompt = f"""Ecris un monologue réaliste en se mettant dans la peau de {personna}. 
                Je veux qu'il parle comme il aurait pu parler, sans didascalies, sans indications. Juste le discours."""

# Number of texts to generate
n_texts = 10

while(True) : 
    text = generate_text(user_prompt, n_texts)
    say(text)

    time.sleep(5*60)