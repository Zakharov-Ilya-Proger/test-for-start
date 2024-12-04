import argparse
from kafka import KafkaProducer, KafkaConsumer

def produce(message, topic, kafka_server):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    producer.send(topic, message.encode('utf-8'))
    producer.flush()
    print(f"Message '{message}' sent to topic '{topic}'")

def consume(topic, kafka_server):
    consumer = KafkaConsumer(topic, bootstrap_servers=kafka_server, auto_offset_reset='earliest')
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kafka Producer/Consumer Script")
    subparsers = parser.add_subparsers(dest="command")

    produce_parser = subparsers.add_parser('produce', help="Produce a message to a Kafka topic")
    produce_parser.add_argument('--message', required=True, help="Message to send")
    produce_parser.add_argument('--topic', required=True, help="Kafka topic")
    produce_parser.add_argument('--kafka', required=True, help="Kafka server IP:PORT")

    consume_parser = subparsers.add_parser('consume', help="Consume messages from a Kafka topic")
    consume_parser.add_argument('--topic', required=True, help="Kafka topic")
    consume_parser.add_argument('--kafka', required=True, help="Kafka server IP:PORT")

    args = parser.parse_args()

    if args.command == 'produce':
        produce(args.message, args.topic, args.kafka)
    elif args.command == 'consume':
        consume(args.topic, args.kafka)
