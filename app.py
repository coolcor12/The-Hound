from domain_classify import *
from flask import Flask
from difflib import SequenceMatcher

app = Flask(__name__)

def load_memory():
    f = open('memory.txt', 'r')
    s = f.read()
    f.close()
    return s

def save_memory(s):
    f = open('memory.txt', 'w')
    f.write(s)
    f.close()

def similar(s1, s2):
   return SequenceMatcher(None, s1, s2).ratio() > .6

@app.route('/<user_input>')
def api_root(user_input):
   text = ' '.join(user_input.split('-'))
   domain = classify('Test02', text)
   if domain != 'Flattery':
       return domain
   memory = load_memory()
   if memory == '':
       save_memory(text)
       return 'Flattery'
   else:
       if similar(memory, text):
           return 'Taunt'
       else:
           save_memory('')
           return 'Flattery'
       
app.run()
