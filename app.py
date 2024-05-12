from flask import Flask, request, jsonify
from get_recs import predict_ranks
import os

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

