import requests

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Something wrong')

if __name__ == "__main__":
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=06ea01fdf1cd596d4316ba016dbdf654&units=metric")
    print(data)
