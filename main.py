import requests
import json

def pars():
    result = []
    r = requests.get('https://rickandmortyapi.com/api/character')
    jsonData = r.json()['results']
    for person in jsonData:
        for episodes in person['episode']:
            sp = episodes.split('/')[-1]
            numbers = ['30', '31', '32', '33']
            if sp in numbers:
                result.append(person['image'])

    return list(set(result))

if __name__ == '__main__':
    with open('big_data.json', 'w') as file:
        json.dump(pars(), file)
    file.close()
