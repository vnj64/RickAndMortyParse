import requests
import json


def pars():
    result = []
    for i in range(30, 34):
        r = requests.get(f'https://rickandmortyapi.com/api/character/?page={i}')
        jsonData = r.json()['results']
        for person in jsonData:
            result.append(person['image'])

    return list(set(result))


if __name__ == '__main__':
    with open('big_data.json', 'w') as file:
        json.dump(pars(), file)
    file.close()
