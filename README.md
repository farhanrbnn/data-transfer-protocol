# data-transfer-protocol
this repository contains modules of data transfer protocol (HTTP and Websocket) for measuring performance each protocol when sending data 

## Description
### HTTP
- http_server.py
  -> run flask server as data receiver from HTTP Clients (localhost)
- http_client.py
  -> to run client to send data to the server
### Websocket
- ws_server.py
  -> to run websocket server as data receiver from websocket clients (localhost)
- ws_client.py
  -> to run client to send data to the server
  
## How To Run
### HTTP
to run server module, just use this command 
```
python3 http_server.py
```
before you run client, you need to prepare some image folder as the data that we want to send.
then specifiy the folder in client code 
```python
def load_image_data():	
	os.chdir('./10_mb') #put foldername here
	for image in glob.glob('*.jpg'):

		with open(image, 'rb') as imageFile:

		    image_s = base64.b64encode(imageFile.read())

	return image_s
```

to run one client, run this command
```
python3 http_client.py
```
to run multiple client, you need to use bash script
```bash
#/bin/bash

for in {1..1000}; do
  python3 ~/path/to/py/file &
done
```
then run the bash script

### Websocket
to run server, just run this command
```
python3 ws_server.py
```
to run client is exactly the same as the HTTP Client




