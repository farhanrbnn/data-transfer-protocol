from flask import Flask
from flask import request
import time 
from multiprocessing import Process 

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def home():
	timeout = time.time() + 5  # 5 minutes from now

	while True:
		test = 0
		if test ==5 or time.time() > timeout:
			break 

	return 'Hello', 200

def main():
    app.run(host='0.0.0.0', threaded = False, debug = True)
    
   
if __name__ == "__main__":
	main()
	#Process(target = main).start()
	
