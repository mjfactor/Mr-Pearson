import random
import json
import torch
from core.model import NeuralNet
from core.main import tokenize, bag_of_words
import time
import sys


def pearson():
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.25)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    with open("brain.json", "r", encoding='utf-8') as file:
        brain = json.load(file)

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = "Mr. Pearson"
    print("Hi! I am Mr. Pearson. I sometime Joke about dead people. Type 'quit' to exit.")
    while True:
        sentence = input("You: ")
        if sentence in ["quit", "exit"]:
            break
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in brain["intents"]:
                if tag == intent["tag"]:
                    print(f"{bot_name}: ", end="")
                    delay_print(random.choice(intent["responses"]))
                    print("\n")

        else:
            print(f"{bot_name}: I do not understand...")
