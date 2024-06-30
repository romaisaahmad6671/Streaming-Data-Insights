# Streaming Data Insights with Kafka

Welcome to our repository dedicated to exploring streaming data insights using Apache Kafka, developed for the Fundamentals of Big Data Analytics (DS2004) course. This project features a Kafka-based streaming data pipeline that processes large-scale e-commerce data to perform real-time analytics with frequent itemset mining algorithms such as Apriori and PCY.

## Project Dependencies

Ensure you have the following software installed:

- **Ubuntu**: [Install Ubuntu](https://ubuntu.com/download)
- **Apache Kafka**: [Install Kafka](https://kafka.apache.org/downloads)
- **Python**: [Install Python](https://www.python.org/downloads/)
- **Jupyter Notebook**: [Install Jupyter Notebook](https://docs.jupyter.org/en/latest/install.html)
- **Pandas**: [Install Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- **NumPy**: [Install NumPy](https://numpy.org/install/)

## Project Overview

This project uses Apache Kafka to build a robust streaming data pipeline, managing large volumes of e-commerce data to perform real-time analytics. The system incorporates algorithms like Apriori and PCY to provide insights into customer buying patterns and product associations.

## Dataset

We utilize the Amazon Metadata dataset, which contains product IDs, names, features, and pricing information. The dataset is initially 12 GB and expands to 105 GB when extracted. Our analysis is based on a 15 GB subset to ensure manageability and performance.

## Detailed Description of Producer and Consumer Scripts

### Producer: `producer.py`

- **Data Loading**: Loads preprocessed JSON data.
- **Kafka Connection**: Establishes connection with Kafka, setting up the topic and server details.
- **Streaming Data**: Publishes data to Kafka in a serialized format, ensuring continuous data flow.
- **Fault Tolerance**: Includes error handling for data streaming issues.

### Consumers: Detailed Workflow

#### `consumer_Apriori.py`

- **Data Subscription**: Subscribes to Kafka topic for data.
- **Data Processing**: Applies Apriori algorithm to find frequent itemsets.
- **Result Storage**: Stores itemsets in MongoDB.

#### `consumer_PCY.py`

- **Data Reception**: Receives data from Kafka topic.
- **Algorithm Application**: Implements PCY algorithm, using hash tables to improve efficiency.
- **Storage of Insights**: Stores results in MongoDB.

#### `consumer_sentiment_analysis.py`

- **Listening to Stream**: Retrieves data from the Kafka stream.
- **Sentiment Analysis**: Analyzes sentiment of product reviews using NLP techniques.
- **Data Output**: Stores sentiment results in MongoDB.

### Common Features Across Consumers

- **Scalability**: Designed to handle high data volumes efficiently.
- **Resilience**: Includes error handling for data streaming and processing interruptions.
- **Modularity**: Scripts can function independently or together.

## Usage Instructions

To set up and run the project:

1. Ensure all dependencies are installed and configured.
2. Run the `setup.sh` script:

```bash
./setup.sh
```

This initializes the producer, consumers, and necessary Kafka components, starting the data streaming and analysis processes.

## Contributors

- **Sharjeel Nadir**: Sharjeelnadir127@gmail.com
- **Masroor Bin Rehan**: i211707@nu.edu.pk

## Additional Notes

- Ensure compatibility of all scripts with your Kafka and database setups.
- Adjustments may be necessary based on your specific environment.

## References

- [Apache Kafka](https://kafka.apache.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
