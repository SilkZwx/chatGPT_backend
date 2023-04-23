FROM ubuntu:latest


RUN apt update -y && apt upgrade -y  && \
    apt install -y tzdata && \
    apt install -y python3 \
    python3-pip \
    tzdata \
    libopencv-dev \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-eng \
    libgl1-mesa-dev

RUN pip3 install pyocr \
    Pillow \
    opencv-python \
    gunicorn \
    Flask

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

CMD exec gunicorn --bind :$PORT --workers 5 --threads 8 --timeout 0 src.main:app
