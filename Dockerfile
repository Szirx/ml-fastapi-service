FROM python:3.9.18-slim-bullseye

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt wordnet stopwords omw-1.4

COPY . .

CMD ["python", "app.py"]