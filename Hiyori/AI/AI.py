import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
def setup():
    setup_flag = json.loads(open("setup.json").read())
    if setup_flag['nltk.download'] == 'false':
        nltk.download('all')
        setup_flag = '{"nltk.download": "true"}'
        with open('setup.json', "w") as s:
            s.write(setup_flag)
            s.close()
        print('setup done!')
    else:
        print('setup done!')



lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = []
classes = []
documents = []
ignore_letters =  ['?', '!', '.', ",", "'"]

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))
print(words)
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

setup()
