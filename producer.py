from kafka import KafkaProducer
import json
import time

def produce_data(producer, topic, data_file):
    with open(data_file, 'r') as file:
        for line in file:
            try:
                transaction = json.loads(line)
                producer.send(topic, json.dumps(transaction).encode('utf-8'))
                time.sleep(1)  
            except Exception as e:
                print(f"Error producing message: {e}")
                continue

if __name__ == '__main__':
    bootstrap_servers = 'localhost:9092'  
    topic = 'preprocessed_data'
    data_file = 'preprocessed_data.json'

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    produce_data(producer, topic, data_file)

    producer.close()
