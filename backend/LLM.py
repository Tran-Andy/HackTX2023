import requests
import json

url = 'http://localhost:8080/getall'

def getData():
    response = requests.get(url)
    data = json.loads(response.content)
    return data

def getLLM():

    data = getData()

    values = []
    for item in data:
        value = item['value']
        values.append(int(value))

    hash = {}
    result = [[] for i in range(len(values)+1)]

    for i in values:
        hash[i] = 1 + hash.get(i,0)

    for n, c in hash.items():
        result[c].append(n)

    res = 0
    for i in range(len(result) - 1, 0, -1):
        for n in result[i]:
            if n is not None:
                res = n
                return res # return here