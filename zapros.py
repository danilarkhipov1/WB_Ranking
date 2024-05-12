import requests
import json

# URL для запроса
url = 'http://127.0.0.1:5000/predict'

data = {
    'features': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
}

# Преобразование данных в формат JSON
payload = json.dumps(data)

# Выполнение POST-запроса
response = requests.post(url, json=data)

# Вывод ответа
print(response.json())

