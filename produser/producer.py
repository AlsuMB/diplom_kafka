from kafka import KafkaProducer

TOPIC_NAME = 'stream_topic'
KAFKA_SERVER = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
producer.send(TOPIC_NAME, value=b'Hello World!')
producer.flush()