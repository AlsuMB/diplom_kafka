from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='158.160.90.238:9092')

for i in range(10):
    message = f"Message {i}"
    producer.send('stream_topic', value=message.encode('utf-8'))
    time.sleep(1)

producer.close()