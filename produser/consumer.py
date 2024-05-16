from kafka import KafkaConsumer

TOPIC_NAME = 'stream_topic'
consumer = KafkaConsumer(TOPIC_NAME,)
for msg in consumer:
    print(msg)