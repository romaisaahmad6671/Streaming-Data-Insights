# Streaming Data Insights with Kafka

This repository contains the implementation of a streaming data pipeline and frequent itemset mining using Apache Kafka, designed as part of the Fundamental of Big Data Analytics (DS2004) course. The system processes and analyzes streaming data from the Amazon metadata dataset to derive insights using advanced algorithms like Apriori and PCY.

## Dependencies

* Ubuntu ([install](https://ubuntu.com/download))
* Kafka ([install](https://kafka.apache.org/downloads))
* Python ([install](https://www.python.org/downloads/))
* Jupyter Notebook ([install](https://docs.jupyter.org/en/latest/install.html))
* pandas ([install](https://pandas.pydata.org/docs/getting_started/install.html))
* numpy ([install](https://numpy.org/install/))

## Project Overview:

Our project utilizes Apache Kafka to set up a robust streaming data pipeline, handling large volumes of e-commerce data to perform real-time data analytics. By implementing frequent itemset mining algorithms like Apriori and PCY, the system provides valuable insights into customer buying patterns and product associations.

## Dataset

We are using the Amazon Metadata dataset, which contains details like product IDs, names, features, and pricing information. This dataset, originally 12 GB, expands to 105 GB when extracted. Our analysis uses a 15 GB sample to ensure manageability and performance.

## Approach and Methodology

### Data Preprocessing
First, the Amazon dataset is preprocessed to ensure data quality. This involves cleaning data, formatting it appropriately, and then saving the processed data as a new JSON file. This step is crucial for preparing the dataset for effective streaming.

### Streaming Pipeline Setup
1. **Producer Application**: A Python script (`producer.py`) streams preprocessed data into our Kafka system.
2. **Consumer Applications**: Three separate consumer scripts subscribe to the producer's data and perform various analyses:
   - `consumer_Apriori.py`: Implements the Apriori algorithm.
   - `consumer_PCY.py`: Utilizes the PCY algorithm.
   - `consumer_sentiment_analysis.py`: Conducts an innovative analysis, details of which are described within the script.

### Database Integration
Each consumer application is configured to connect to a MongoDB database to store analysis results, making the insights easily accessible and persistent.

## Implementation Details

### Files and Scripts
- `producer.py`: Streams data into Kafka.
- `consumer_Apriori.py`, `consumer_PCY.py`, `consumer_sentiment_analysis.py`: Consumer scripts that perform data analytics.
- `setup.sh`: Bash script to initialize Kafka components and run the entire system.

## Usage

### Setting up Kafka
Ensure Kafka and all its components like Zookeeper are correctly configured and running. Use the official [Kafka documentation](https://kafka.apache.org/documentation/) for guidance.

### Running the Application
To start the streaming data pipeline and the analytics processes, execute the `setup.sh` bash script:

```bash
./setup.sh
```

This script initializes the producer, consumers, and all necessary Kafka components.

## Contributors:

This project exists thanks to the extraordinary people who contributed to it.
* **[Sharjeel Nadir](i212699@nu.edu.pk)**
* **[Masroor Bin Rehan](i211707@nu.edu.pk)**

## Notes
- Ensure all scripts are compatible with your Kafka and database setup.
- Adjustments may be necessary based on your specific environment.

## References:

* [Apache Kafka](https://kafka.apache.org/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
