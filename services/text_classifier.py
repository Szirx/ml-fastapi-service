from typing import List
import joblib
from services.preprocess_utils import preprocess_text


class DepressionClassifier:
    def __init__(self, config):
        print(config)
        self._vectorizer_path = config['vectorizer_path']
        self._model_path = config['model_path']
        
        self._vectorizer = joblib.load(self._vectorizer_path)
        self._model = joblib.load(self._model_path)

        self.keys = ['no depression', 'depression']
    
    def _predict(self, text: str):
        text = self._vectorizer.transform(preprocess_text(text))
        return self._model.predict(text)
    
    def _predict_proba(self, text: str):
        text = self._vectorizer.transform(preprocess_text(text))
        return self._model.predict_proba(text)
    
    def _postprocess_predict(self, predict):
        return self.keys[0] if int(predict) == 0 else self.keys[1]
    
    def _postprocess_predict_proba(self, predict_proba):
        return {self.keys[idx]: value for idx, value in enumerate(predict_proba[0])} 
    
    def predict(self, text: str):
        return self._postprocess_predict(self._predict(text))
    
    def predict_proba(self, text: str):
        return self._postprocess_predict_proba(self._predict_proba(text))
    
