import json
from main import tokenize, stem, bag_of_words


with open("brain.json", "r") as file:
    brain = json.load(file)

all_words = []
tags = []
xy = []
for intent in brain["intents"]:
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))