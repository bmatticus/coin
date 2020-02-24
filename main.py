"""
Main script for coin price collection
"""

import time
import datetime
from coinmarket import CoinMarket
from kafka import KafkaProducer
import json


coin_market = CoinMarket()
producer = KafkaProducer(bootstrap_servers='192.168.35.10:9092')

while True:
    """
    Infinite loop with 60 second sleep between iterations, polling every 60 seconds.
    """
    print("{}: Gathering new data".format(datetime.datetime.now().isoformat()))
    items = coin_market.get_latest_listing()
    for item in items:
        producer.send('coin', json.dumps(item))

    print("{}: Sent {} new items to kafka topic".format(datetime.datetime.now().isoformat(), len(items)))

    time.sleep(60)
