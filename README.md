# Overview

This template repo uses docker compose to build multiple containers for Kafka, zookeeper, flask, and spark/jupyter for use with developing real time machine learning solutions.

# Use

After cloning this repo, you need to run docker-compose up and docker will build the various containers. 

You just need to run `./setup-compose.sh` to build the environment. This script appends the github repo name to the container names to maintain uniqueness. 

## Credentials.

### AWS
In order for access to AWS services, you must have the `~/.aws/credentials` on your local environment. The Docker instance has mounted this file as an external volume, so as you update your credentials locally, they will be live on your docker instance. This file is **not editable** from your docker instance, and only editable from your local OS.

### Twitter
If you are testing the Twitter sections of the notebook, you must first have developer api keys and access tokens. You can apply for one [here](https://developer.twitter.com/en/apply-for-access). The way this data is accessed is from your local home directory in a subdir called `.secrets`. Please create this directory and create a json file (`$HOME/.secrets/twitter.json`) with the following structure:

```json
{
    "api_key": "API KEY from twitter",
    "api_secret_key": "API SECRET KEY from twitter",
    "bearer_token": "BEARER TOKEN FOR curl Access",
    "access_token": "ACCESS TOKEN",
    "access_token_secret": "ACCESS TOKEN SECRET"
}
```
Some documentation for tweepy will use different naming for these keys:
```
CONSUMER_KEY = API_KEY
CONSUMER_SECRET = API_SECRET_KEY
CONSUMER_TOKEN = ACCESS_TOKEN
CONSUMER_TOKEN_SECRET = ACCESS_TOKEN_SECRETD
```

This file will be accessible as a volume in the docker container with read-only access from `~/.secrets/twitter.json`

## Jupyter Lab

The jupyter instance acts as the client for orchestrating all steps for the workflow. There are sections for creating messages and **publishing to a kafka** topic, read them into **Spark** as a **kafka subscriber**, and access the **ml prediction** Flask endpoint all from your jupyter instance. 

Access the jupyter notebook by going to the `jupyter` service container in Docker under the repo build, and look for the URL for the jupyter instance. Copy and paste this into your browser and you will be active in a jupyter lab session.

Suggest starting with the `Pyspark ML and Kafka` notebook as an example of how the interactions occur.

## ml-rest-flask

This directory is where the ML predictions are served. The example `app.py` is used for simply **serving predictions** from a pretrained model. A separate endpoint needs to be established for model training. 

There is also no data preprocessing endpoint either, which should be built 



# Resources 
Based off:
https://github.com/BogdanCojocar/medium-articles/tree/master/realtime_kafka

And 
[This](https://docs.docker.com/compose/gettingstarted/) For Redis for Flask caching

[Networking for flask app](https://pythonspeed.com/articles/docker-connection-refused/)
[Spark with Flask](https://www.codementor.io/@jadianes/building-a-web-service-with-apache-spark-flask-example-app-part2-du1083854)
