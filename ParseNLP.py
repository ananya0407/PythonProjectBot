import random, json
from snips_nlu import SnipsNLUEngine
import io
with io.open('trained_engine.json') as f:
    engine_dict = json.load(f)
nlp_engine = SnipsNLUEngine(engine_dict)
greeting_responses = ["*Hi! I'm Reo. I book meeting rooms for you*", "*Yo! Reo here! To book a meeting room, type book me a meeting room.*"]
thank_responses = ["*You are always welcome*", "I'm here to help you", "Please don't mention it", "Don't mention it", "Welcome"]
filler_responses = ["Sure", "Okay", "Right", "Cool"]
askbot_responses = ["I'm amazing as well","Hey.I'm great", "I'm great. Thanks for asking.", "I'm awesome. That's all."]
goodbye_responses = ["Goodbye!", "Bye. Bye", "See you later!"]

def parse_nlp(message):
    if message:
        print("User message: " + message)
        understand = nlp_engine.parse(message)
        print(understand)
        if understand['intent'] == None:
            return 1, "Sorry didn't get that! FYI, I can help you with meetings."
        elif understand['intent']['intentName']=='greeting':
            return 1, random.choice(greeting_responses)
        elif understand['intent']['intentName']=='fillers':
            return 1, random.choice(filler_responses)
        elif understand['intent']['intentName']=='askaboutbot':
            return 1, random.choice(askbot_responses)
        elif understand['intent']['intentName']=='thanks':
            return 1, random.choice(thank_responses)
        elif understand['intent']['intentName']=='goodbye':
            return 1, random.choice(goodbye_responses)
        elif understand['intent']['intentName']=='userschedule':
            return 2, ""
        elif understand['intent']['intentName']=='meeting_setup':
            return 3,
    return None, None
