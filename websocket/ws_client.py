import asyncio
import websockets
import os
import glob
import time
import base64


def load_image_data():	

	os.chdir('./10_mb')
	for image in glob.glob('*.jpg'):

		with open(image, 'rb') as imageFile:

		    image_s = base64.b64encode(imageFile.read())

	return image_s

async def send_message():

    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        
        start = time.time()
        await websocket.send(str(load_image_data()))
        end = time.time()

        print('client 1: {} ms'.format((end - start)*1000))

       
def main():

    asyncio.get_event_loop().run_until_complete(send_message())

    
if __name__ == '__main__':

	main()

	