FROM python:3.9-slim

ENV PYTHONBURRERED=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update \
 && apt-get install -y  build-essential \
 && apt-get install -y portaudio19-dev\
 && apt-get install -y ffmpeg\
 && apt-get install flac\
 && pip install --upgrade pip\
 && pip install -r requirements.txt \
 && pip install google-cloud-storage

ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]