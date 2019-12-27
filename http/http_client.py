import os
import requests
import glob
import time 
import base64


url = 'http://0.0.0.0:5000/'
path = './10_mb'
folders = [f for f in glob.glob(path + '**/*', recursive = True)]



def load_data():

	for folder in folders:
		with open(folder, 'rb') as imageFile:
			#image_s = base64.b64encode(imageFile.read())
			image_s = {'file_image':open(folder, 'rb')}

	return image_s
		    

def send_data():

	start = time.time()
	r = requests.post(url, files = load_data())
	end = time.time()

	print('client 2 : {} ms'.format((end - start)*1000-5000))

if __name__ == "__main__":

	send_data()






# os.chdir('./test')

# start = time.time()
# for image in glob.glob('*.jpg'):

# 	files = {'file1':open(image, 'rb')}

# 	# start = time.time()
# 	r = requests.post(url, files=files)
# 	# end = time.time()


# 	# print(end - start)

# 	r.text
# end = time.time()

# print(end - start)







# os.chdir('./50_mb')
# for image in glob.glob('*.jpg'):

# 	files = {'file1': open(image, 'rb')}

# 	r = requests.post(url, files=files)

# 	r.text