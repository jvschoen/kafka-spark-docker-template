FROM python:3.7-alpine
#WORKDIR ./
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN ls ./
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

# For NLP Sentiment
RUN python -c "import nltk; nltk.download('vader_lexicon')"

EXPOSE 9000
COPY ./app.py /app.py

CMD ["python3", "./app.py"]