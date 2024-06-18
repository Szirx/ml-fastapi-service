# ml-fastapi-service

## Описание
FastAPI-сервис для распознавания депрессивного поведения у человека по тексту.\
Для быстрого и удобного ввода команд используется [Makefile](Makefile).

## Команды

#### Установка зависимостей: 
```
make install
```
#### Сухой запуск: 
```
make example_run
```
#### Docker Compose: 
```
make compose
```
#### Kubernetes:
```
make apply_manifests
```
#### Для локального внешнего доступа к сервису в K8S:
```
minikube tunnel
```

## Примеры использования

### Docker

#### Запрос
```shell
curl -X 'POST' \
  'http://0.0.0.0:2444/text/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "anyone else instead of sleeping more when depressed stay up all night to avoid the next day from coming sooner may be the social anxiety in me but life is so much more peaceful when everyone else is asleep and not expecting thing of you"
}'
```

#### Ответ
```shell
"depression"
```

### Kubernetes

#### Запрос

```shell
curl -X 'POST' \
  'http://localhost:2444/text/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "anyone else instead of sleeping more when depressed stay up all night to avoid the next day from coming sooner may be the social anxiety in me but life is so much more peaceful when everyone else is asleep and not expecting thing of you"
}'
```
#### Ответ

```shell
"depression"
```