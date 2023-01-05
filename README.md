# Blockchain-From-Scratch
## Creating a blockchain from scratch in python  
  
python 3.6.3  
Flask 0.12.2  
pip install Flask --upgrade  
pip install requests==2.18.4  
  
##### Separately run flask apps node1, node2 and node3.  
##### Use the connect_node endpoint and as payload send nodes.json without targeted application's address.  
##### Connect all nodes and use other endpoints to observe blockchain.  
  
Json object, while targeting connect_node of node1 flask app:  
```json
{ 
    "nodes": [  
        "http://127.0.0.1:5002",  
        "http://127.0.0.1:5003"  
    ]  
}
```