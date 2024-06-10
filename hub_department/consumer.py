from pykafka import KafkaClient

if __name__ == "__main__":
    #хост подключения к кафка
    client = KafkaClient(hosts='158.160.90.238:9092')
    #имя топика из которого мы собираемся получать сообщения
    topic = client.topics[b'stream_topic']
    #создание простого консьюмера
    consumer =  topic.get_simple_consumer()
    #обработка сообщений если они еще есть в топике
    for message in consumer:
        if message is not None:
            print(message.value.decode('utf-8')) #берется значение сообщений и декодируется по utf-8 для валидного отображения
