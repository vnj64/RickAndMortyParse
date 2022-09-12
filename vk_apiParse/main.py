import requests
import statistics



def parse(URL_TEMPLATE):
    r = requests.get(URL_TEMPLATE)
    json_data = r.json()
    result = []
    for element in json_data['response']['items']:
        
        try:
            json_data = (element["bdate"])

            if len(json_data) > 2:
                bdate_list = int(json_data[-4:])
                result.append(bdate_list)
                average_age = statistics.mean(result)
        except:
            pass

    return "Average: " + str(2022 - average_age)[:4]

print(parse('https://api.vk.com/method/friends.get?fields=bdate&access_token=TOKEN&v=5.131'))
