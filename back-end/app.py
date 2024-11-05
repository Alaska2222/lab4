
from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {"name": "Item 1"},
    {"name": "Item 2"},
    {"name": "Item 3"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    data.append(item)
    return jsonify({'message': 'Item added', 'item': item}), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(data):
        removed_item = data.pop(item_id)
        return jsonify({'message': 'Item deleted', 'item': removed_item}), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
