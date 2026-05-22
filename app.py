from flask import Flask, render_template, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total requests count')
LIKE_COUNT = Counter('app_likes_total', 'Total likes count')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return render_template('index.html')

@app.route('/like', methods=['POST'])
def like():
    LIKE_COUNT.inc()
    return '', 204

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
