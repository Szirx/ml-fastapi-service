import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf

from containers.containers import AppContainer
from routes.routes import router as app_router
from routes import texts as texts_routes


def create_app() -> FastAPI:
    container = AppContainer()
    cfg = OmegaConf.load('configs/inference_config.yaml')
    container.config.from_dict(cfg)
    container.wire([texts_routes])

    app = FastAPI()
    app.include_router(app_router, prefix='/text', tags=['text'])
    return app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, port=2444, host='0.0.0.0')