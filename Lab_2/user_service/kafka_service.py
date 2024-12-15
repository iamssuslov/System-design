from kafka import KafkaProducer

KAFKA_TOPIC = 'my_topic'


def get_producer():
    return KafkaProducer(bootstrap_servers='kafka:9092')
