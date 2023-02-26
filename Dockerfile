FROM python:3.9-slim

ENV PYTHONBURRERED=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update \
 && apt-get install -y  build-essential \
 && apt-get install -y portaudio19-dev\
 && pip install --upgrade pip\
 && pip install -r requirements.txt \
 && pip install google-cloud-storage

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]