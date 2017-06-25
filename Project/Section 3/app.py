from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item 1',
                'price': 15.99
            }
        ]
    }
]

# @app.route('/')
# def home():
# 	return "Hello, World!"

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json();
    newStore = {
    	'name': requestData['name'],
    	'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def getStore(name):
    for store in stores:
    	if store['name'] == name:
    		return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store', methods=['GET'])
def getStores():
    return jsonify({
    		'stores': stores
    	})

# POST /store/<string:name>/item data: {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
    	if store['name'] == name:
    		newItem = {
    			'name': requestData['name'],
    			'price': requestData['price']
    		}
    		store['items'].append(newItem)
    		return jsonify(newItem)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def getItemsFromStore(name):
    for store in stores:
    	if store['name'] == name:
    		return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(host='0.0.0.0', port=5001, debug=True)
