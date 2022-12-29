from flask import Flask, jsonify
from blockchain import Blockchain

#Create Web App
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#Init blockchain
blockchain = Blockchain()

#Send request
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    prev_block = blockchain.get_last_block()
    proof = blockchain.proof_of_work(prev_block['proof'])
    prev_hash = blockchain.hash(prev_block)
    new_block = blockchain.create_block(proof, prev_hash)
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': new_block['index'],
        'timestamp': new_block['timestamp'],
        'proof': new_block['proof'],
        'prev_hash': new_block['prev_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/is_valid', methods=['GET'])
def is_chain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    message = "The chain is valid" if is_valid else "The chain is corrupted"
    response = {
        'message': message
    }
    return jsonify(response), 200

#run server
app.run(host = '0.0.0.0', port = 5000)