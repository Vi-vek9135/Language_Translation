from google.cloud import translate_v2 as translate
from transformers import pipeline
translate_client = translate.Client()
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def translate_text(text, target_language):
    # Detect the source language
    result = translate_client.detect_language(text)
    source_language = result["language"]
    
    # Translate the text
    translation = translate_client.translate(text, target_language=target_language)
    # Generate a response in the target language
    response = generator(f"translate from {source_language} to {target_language}: {text}")[0]["generated_text"]
    return response, translation["input"], translation["translatedText"], translation["detectedSourceLanguage"]


text = '''Introduction
This text discusses a judgment from the Supreme Court of India regarding a 
complaint filed under Section 138 of the Negotiable Instruments Act. 
The case involves a dispute over a cheque issued by the respondent, 
which was returned due to insufficient funds. The Trial Court initially 
dismissed the complaint, but the Supreme Court upheld it, finding that 
the cheque was indeed issued by the respondent.'''


print(translate_text(text,"gu"))