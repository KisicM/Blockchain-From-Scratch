import datetime, hashlib, json

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.create_block(proof = 1, prev_hash = '0')

    def create_block(self, proof, prev_hash) -> dict:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'prev_hash': prev_hash
        }
        self.chain.append(block)
        return block
    
    def get_last_block(self) -> dict:
        return self.chain[-1]

    def proof_of_work(self, prev_proof) -> int:
        new_proof = 1
        check_proof = False
        while check_proof is False:
            nonce = self.get_nonce(prev_proof, new_proof)
            if nonce[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def get_nonce(self, prev_proof, new_proof):
        return hashlib.sha256(self.non_symmetric_operation(prev_proof, new_proof).encode()).hexdigest()
    
    def non_symmetric_operation(self, prev_proof, new_proof) -> str:
        return str(new_proof**2 - prev_proof**2) #A^2-B^2 != B^2-A^2, while A+B = B+A

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain) -> bool:
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['prev_hash'] != self.hash(prev_block):
                return False
            nonce = self.get_nonce(prev_block['proof'], block['proof'])
            if nonce[:4] != '0000':
                return False
            prev_block = block
            block_index += 1
        return True
