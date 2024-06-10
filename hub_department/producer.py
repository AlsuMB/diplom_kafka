import time
from json import dumps

from kafka import KafkaProducer

from hub_department.generate_data import get_random_values

producer = KafkaProducer(bootstrap_servers=['158.160.90.238:9092'],
                         value_serializer=lambda x: dumps(x, default=str).encode('utf-8'),
                         compression_type='gzip')
my_topic = 'stream_topic'

for i in range(1000000):
    # time.sleep(5)
    try:
        data = get_random_values()
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