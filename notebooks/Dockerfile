FROM jupyter/pyspark-notebook:${JUPYTER_VERSION:-latest}

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8888