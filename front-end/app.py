from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

BACKEND_URL = 'http://backend:5000/items'

@app.route('/')
def index():
    response = requests.get(BACKEND_URL)
    items = response.json()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = {'name': request.form['name']}
    requests.post(BACKEND_URL, json=item)
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    requests.delete(f"{BACKEND_URL}/{item_id}")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
