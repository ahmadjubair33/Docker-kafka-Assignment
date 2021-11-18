FROM python:3.8
WORKDIR /kafka_consumer 
#RUN apk add --no-cache python3
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
COPY . .
EXPOSE 80
CMD [ "python", "consumer.py" ]