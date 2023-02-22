from flask import Flask, jsonify
from opentracing import Tracer
from jaeger_client import Config

app = Flask(__name__)

# Initialize Jaeger tracer configuration
config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'logging': True,
    },
    service_name='my-flask-app',
)

# Initialize tracer instance with Jaeger configuration
tracer = config.initialize_tracer()

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    with tracer.start_span('index') as span:
        response = requests.get('http://backend:8080/' + name)
        return jsonify(response.json())

if __name__ == '__main__':
    app.run()
