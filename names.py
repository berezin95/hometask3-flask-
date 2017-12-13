import requests

_api_key = 'c7c02e97f617c43fe537a11c49b9b9da'
def get_names(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Something wrong')

if __name__ == "__main__":
    data = get_names("http://api.data.mos.ru/v1/datasets/2009/rows?api_key=%s" % _api_key)
    print(data)

    with open('names.txt', 'w', newline='', encoding='utf-8') as f:
        for user in data:
            f.write(str(user['Cells']) + '\n')