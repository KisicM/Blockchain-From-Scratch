from flask import Flask, jsonify, request
from blockchain import Blockchain
from uuid import uuid4

# Create Web App
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Create an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')

# Init blockchain
blockchain = Blockchain()


# Send request
@app.route('/mine_block', methods=['GET'])
def mine_block():
    prev_block = blockchain.get_last_block()
    proof = blockchain.proof_of_work(prev_block['proof'])
    prev_hash = blockchain.hash(prev_block)
    blockchain.add_transaction(sender=node_address, receiver='Mihajlo', amount=1)
    new_block = blockchain.create_block(proof, prev_hash)
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': new_block['index'],
        'timestamp': new_block['timestamp'],
        'proof': new_block['proof'],
        'prev_hash': new_block['prev_hash'],
        'transactions': new_block['transactions']
    }
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_chain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    message = 'The chain is valid' if is_valid else 'The chain is corrupted'
    response = {
        'message': message
    }
    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    new_transaction = request.get_json()
    transaction_keys = {'sender', 'receiver', 'amount'}
    if not all(key in new_transaction for key in transaction_keys):
        return 'Some elements of transaction are missing', 400
    index = blockchain.add_transaction(new_transaction['sender'], new_transaction['receiver'],
                                       new_transaction['amount'])
    response = {
        'message': f'Transaction added to block {index}'
    }
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No nodes", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message': 'All nodes connected. The network now contains the following nodes: ',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 200


@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    message = 'The chain was replaced by the longest one' if is_chain_replaced else 'The chain was up to date'
    response = {
        'message': message,
        'chain': blockchain.chain
    }
    return jsonify(response), 200


# run server
app.run(host='0.0.0.0', port=5001)
