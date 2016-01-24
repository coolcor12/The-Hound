import requests

def classify(model_name, text):
    url = 'http://apiv2.indico.io/custom/batch/predict?key=3' + \
          '74699a4e0272c79937b00688aad7da2'
    r = requests.get(url, data = {"data": [text], "collection": model_name })
    data = eval(r.text)['results'][0]
    return max(data, key=data.get)
    
