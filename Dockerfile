FROM python:2.7.15-slim

RUN mkdir -p /opt/coin
WORKDIR /opt/coin
COPY . /opt/coin
RUN pip install -r requirements.txt

CMD ["python", "main.py"]