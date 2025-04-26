from flask import Flask, session
from redis import Redis
import os

app = Flask(__name__)
app.config.from_object('config.Config')

redis_client = Redis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    password=os.getenv('REDIS_PASSWORD', None)
)

@app.route('/')
def index():
    session['visits'] = session.get('visits', 0) + 1
    return f"Visit count: {session['visits']}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
