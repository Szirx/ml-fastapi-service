from dependency_injector import containers, providers
from services.text_classifier import DepressionClassifier

class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    text_classifier = providers.Singleton(
        DepressionClassifier,
        config=config.services.depression_classifier,
    )