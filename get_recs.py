import pandas as pd
import joblib

def load_model(filename):
    return joblib.load(filename)

def predict_ranks(features):
    try:
        # Загрузка модели
        loaded_model = load_model('model.pkl')

        # Предсказание на данных
        y_pred = loaded_model.predict(features)

        # Ранжирование предсказаний
        ranked_predictions = pd.DataFrame({'pred': y_pred})
        ranked_predictions['rank'] = ranked_predictions['pred'].rank(method='dense', ascending=False).astype(int)

        return ranked_predictions['rank'].tolist()
    except Exception as e:
        print("Error:", e)
        return []
