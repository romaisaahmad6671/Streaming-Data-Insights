from kafka import KafkaConsumer
from collections import defaultdict
import json

def generate_candidate_itemsets(frequent_itemsets, k):
    candidate_itemsets = []
    for itemset1 in frequent_itemsets:
        for itemset2 in frequent_itemsets:
            if itemset1[:-1] == itemset2[:-1] and itemset1[-1] < itemset2[-1]:
                candidate = itemset1 + [itemset2[-1]]
                candidate_itemsets.append(candidate)
    return candidate_itemsets

def prune_infrequent_itemsets(candidate_itemsets, transaction_list, min_support):
    item_counts = defaultdict(int)
    for transaction in transaction_list:
        for candidate in candidate_itemsets:
            if set(candidate).issubset(transaction):
                item_counts[tuple(candidate)] += 1

    frequent_itemsets = [list(itemset) for itemset, count in item_counts.items() if count >= min_support]
    return frequent_itemsets

def mine_frequent_itemsets(consumer, topic, min_support):
    frequent_itemsets = []
    transaction_list = []

    consumer.subscribe([topic])

    try:
        for message in consumer:
            transaction = json.loads(message.value.decode('utf-8'))
            transaction_list.append(set(transaction))

            for item in transaction:
                frequent_itemsets.append([item])

            k = 2
            while True:
                candidate_itemsets = generate_candidate_itemsets(frequent_itemsets, k)
                frequent_itemsets = prune_infrequent_itemsets(candidate_itemsets, transaction_list, min_support)
                if not frequent_itemsets:
                    break
                print("Frequent Itemsets (length {}):".format(k), frequent_itemsets)
                k += 1

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    bootstrap_servers = 'localhost:9092'
    group_id = 'my_consumer_group'
    topic = 'preprocessed_data'
    min_support = 2

    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        auto_offset_reset='earliest'
    )

    mine_frequent_itemsets(consumer, topic, min_support)

