import google.generativeai as genai
import time
import csv

### PARAMETERS ###
# MODEL
model_name = "gemini-1.5-flash"
api_key = ""

### GENERATE TEXTS ###
def generate_text(user_prompt, n_texts=5) :
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('models/' + model_name)

    def generate_text_from_prompt(prompt):
        answer = model.generate_content(prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=None,
                temperature=1.0,
            )
        )
        return answer.text

    time_for_5_texts = 35
    print(f"Estimation du temps de génération : {round(n_texts * time_for_5_texts/5)} secondes")

    text = generate_text_from_prompt(user_prompt)

    start = time.time()
    for _ in range(n_texts) :
        prompt = "Ecris la suite du monologue suivant, sans répéter ce qui a déjà été dit : " + text
        text += generate_text_from_prompt(prompt)

        # Save the generated text to a csv file
        # with open('texts.csv', 'a', newline='', encoding='utf-8') as csvfile:
        #     csvwriter = csv.writer(csvfile)
        #     csvwriter.writerow([text])

        # Maximum of 15 requests per minute
        time.sleep(4)

    with open('texts.txt', 'a', newline='', encoding='utf-8') as f :
        f.write(text)


    print(f"Temps de génération : {time.time() - start} secondes")

    return text