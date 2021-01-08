# Overview

This template repo uses docker compose to build multiple containers for Kafka, zookeeper, flask, and spark/jupyter for use with developing real time machine learning solutions.

# Use

After cloning this repo, you need to run docker-compose up and docker will build the various containers. 

You just need to run `./setup-compose.sh` to build the environment. This script appends the github repo name to the container names to maintain uniqueness. 


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
