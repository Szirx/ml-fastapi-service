from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import BaseModel
from containers.containers import AppContainer
from routes.routes import router
from services.text_classifier import DepressionClassifier

class TextInput(BaseModel):
    text: str

@router.post('/predict')
@inject
def predict(
    data: TextInput,
    service: DepressionClassifier = Depends(Provide[AppContainer.text_classifier]),
):
    return service.predict(data.text)

@router.post('/predict_proba')
@inject
def predict(
    data: TextInput,
    service: DepressionClassifier = Depends(Provide[AppContainer.text_classifier]),
):
    return service.predict_proba(data.text)