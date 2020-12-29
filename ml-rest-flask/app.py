import time

from flask import Flask, jsonify, request
import redis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6397)
sid = SentimentIntensityAnalyzer()

def get_hit_count():
    """Creates a prediction counter as a 
    simple way to start implementing a redis
    cache store if desired. not currently utilized

    Raises:
        exc: [description]

    Returns:
        [type]: [description]
    """
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/predict', methods=['POST'])
def predict():
    """This Creates a POST request with msg containing
    message in form:
    {"data": "some text to analyze"}

    We use the SentimentIntensityAnalyzer 
    to output a polarity score dictionary
    as the response in the form of JSON

    Returns:
        str: JSON string of polarity score 
    """
    result = sid.polarity_scores(request.get_json()['data'])
    #num_preds = get_hit_count()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
    