# Blockchain-From-Scratch

This repository contains an implementation of a blockchain from scratch. The project focuses on creating a decentralized blockchain network where multiple nodes interact and validate transactions. By building this blockchain from the ground up, you will gain a comprehensive understanding of how a blockchain system works and learn how to manually handle transaction validation.

## Setup  
  
*python 3.6.3*  
*Flask 0.12.2*

```bash
pip install Flask --upgrade  
pip install requests==2.18.4  
```

##### Separately run flask apps node1, node2 and node3.  
##### Use the connect_node endpoint and as payload send nodes.json without targeted application's address.  
##### Connect all nodes and use other endpoints to observe blockchain.  
  
Example of json object used for targeting connect_node of node1 flask app:
  
```json
{ 
    "nodes": [  
        "http://127.0.0.1:5002",  
        "http://127.0.0.1:5003"  
    ]  
}
```