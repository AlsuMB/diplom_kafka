from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'),
                         compression_type='gzip')
my_topic = 'transaction'
data = get_random_value()

try:
    future = producer.send(topic=my_topic, value=data)
    record_metadata = future.get(timeout=10)

    print('--> The message has been sent to a topic: \
            {}, partition: {}, offset: {}' \
          .format(record_metadata.topic,
                  record_metadata.partition,
                  record_metadata.offset))

except Exception as e:
    print('--> It seems an Error occurred: {}'.format(e))

finally:
    producer.flush()