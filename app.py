from flask import Flask, request, jsonify
from get_recs import predict_ranks

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получение данных из запроса
        data = request.json

        # Предсказание рангов
        ranks = predict_ranks(data['features'])

        # Формирование ответа
        response = {
            'success': True,
            'ranks': ranks
        }

    except Exception as e:
        # Обработка ошибок
        response = {
            'success': False,
            'error': str(e)
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


