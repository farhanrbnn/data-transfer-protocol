import asyncio 
import websockets


async def recv_message(websocket, path):

	message = await websocket.recv()
	print(message)


def main():

	start_server = websockets.serve(recv_message, "localhost", 8765)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
	
	main()