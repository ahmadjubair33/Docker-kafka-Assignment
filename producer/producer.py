import time 
import json 
import random 
from datetime import datetime

from kafka import KafkaProducer
from data_generator import generate_message



# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    api_version=(2),
    value_serializer=serializer
)


if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        first_kafka_topic = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(first_kafka_topic)}')
        producer.send('first_topic', first_kafka_topic)
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)