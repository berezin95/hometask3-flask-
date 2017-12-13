from flask import Flask, abort, request
from req import get_weather
from datetime import datetime
from news_list import all_news
from names import get_names

city_id = 524901
apikey = '06ea01fdf1cd596d4316ba016dbdf654'
_api_key = 'c7c02e97f617c43fe537a11c49b9b9da'

app = Flask(__name__)

@app.route("/")
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id,apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    #print(cur_date)
    result = "<p><b>Температура:</b> %s</p>" % weather['main']['temp']
    result += "<p><b>Город:</b> %s</p>" % weather['name']
    result += "<p><b>Дата:</b> %s</p>" % cur_date
    return result

@app.route("/names")
def kids_names():
    url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key=%s" % _api_key
    names = get_names(url)
    years = ['2015', '2016', '2017']
    year = int(request.args.get('year')) if request.args.get('year') in years else ''
    result = "<table><tr><th>№</th><th>Имя</th><th>Кол-во человек</th><th>Год</th><th>Месяц</th></tr>"
    cnt = 1
    for user in names:
        name = user['Cells']['Name']
        num = user['Cells']['NumberOfPersons']
        #year = user['Cells']['Year']
        month = user['Cells']['Month']
        if year == '':
            result += "<tr align=center><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (cnt, name, num, user['Cells']['Year'], month)
            cnt += 1
        elif year == user['Cells']['Year']:
            result += "<tr align=center><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (cnt, name, num, year, month)
            cnt += 1
    result += "</table>"
    return result

@app.route("/news")
def all_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)

@app.route("/news/<int:news_id>")
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
        result = result % news_to_show[0]
        return result
    else:
        abort(404)

if __name__ == "__main__":
    app.run()