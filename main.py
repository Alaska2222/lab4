from flask import Flask, request
from waitress import serve

app = Flask(__name__)
@app.route('/api/v1/hello-world-7/', methods=['GET'])
def index():
    return 'Hello World 7'

if __name__ == '__main__':
   serve(app, host='127.0.0.1', port=80)
  #app.run(host='127.0.0.1', port=80)

