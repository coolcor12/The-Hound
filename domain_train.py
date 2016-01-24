import indicoio
from indicoio.custom import Collection
import pandas as pd
import requests

requests.packages.urllib3.disable_warnings()
indicoio.config.api_key = '374699a4e0272c79937b00688aad7da2'

# only 2 models trained so far are named "Test01" and "Test02"
def train(model_name):
    # initialize collection
    collection = Collection(model_name)
    
    # import data from csv and make dataset
    data = pd.read_csv('data/sentences3.csv')
    dataset = [[data[key][i], key] for key in list(data) \
                for i in range(len(data[key]))]
    
    # add data
    for to_train in dataset:
        collection.add_data(to_train)
    collection.train()
    collection.wait()

def classify(model_name, text):
    collection = Collection(model_name)
    response = collection.predict(text)
    domain = max(response, key=response.get)
    #keywords = indicoio.keywords(text, version=2)
    #keyword = max(keywords, key=keywords.get)
    return domain#, keyword
    
