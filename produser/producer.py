from pykafka import KafkaClient

if __name__ == "__main__":
    #хост подключения к кафка
    client = KafkaClient(hosts='158.160.90.238:9092')
    #имя топика в который мы собираемся отправлять сообщения
    topic = client.topics[b'stream_topic']
    #создание продюсера, который и будет отправлять сообщения
    producer = topic.get_producer()
    #отправка самих сообщений
    producer.produce(b'Hello, Streaming!')
    producer.produce(b'Kafka first Message!')
    #остановка продюсера
    producer.stop()