# Overview

Simple script that polls CoinMarket every 60 seconds and pulls new data for coin 
values from their API.  You will need a Kafka broker and Druid instance to flow the data
and graph it. I have a simple docker container for druid to run an all in one version
at https://github.com/bmatticus/druid.

# Running

Simply build the docker image and launch, if preferred, or run the main.py script. You 
will need to edit the main.py script to set your own Kafka broker address and create
a file called api_key that includes your Coin Market API key for this to work.

## Docker Build

Simply run the following from the root of this repository, after setting your Kafka 
instance and your API key.

```docker build -t coin .```

## Docker Run

### coin docker

```docker run -d coin```

You can use a -v to pass in an api_key after building if you need.

```docker run -v <path_to_api_key>:/opt/ocoin/api_key -d coin```

### Kafka docker

See https://hub.docker.com/r/bitnami/kafka/, or similar kafka docker image

### Druid docker

See https://github.com/bmatticus/druid. Also, the postman folder here has the Druid
API call to create the ingestion form Kafka to Druid.

### Grafana

See https://grafana.com/docs/grafana/latest/installation/docker/. Also, the grafana 
folder here has a dashboard that will display data from Druid for this project. 

 


