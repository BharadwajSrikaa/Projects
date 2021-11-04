from os import stat #ignore this one when you are writing the code in vs code it will automatically added
import requests  #this is to get image from the net
import shutil #this is used to save it in your locality.

from requests import status_codes #ignore this one when you are writing the code in vs code it will automatically added

# Setting up the image
image_url = "https://static.zerochan.net/Natsu.Dragneel.full.823660.jpg"
filename = image_url.split("/")[-1] #this indicates the name of file as summer-4823612_960_720.jpg

# Open the url and set the stream content to True
# This helps in returning the image
# streams allow us to send and recieve data without any callbacks or low level protocals and transports
r = requests.get(image_url, stream=True)

# now we have to check whether we recieve the image successfully or not
# now we have to get the value of status_codes value as 200
# this means the file has been retrived successfully
# That value is a http status code which means ok
if r.status_code == 200:
    # now here commes an important isssue
    # now we have successfully retrived the image 
    # we should set the decode_content to 0
    # if we do not do this then the size of the image you have download will be zero
    r.raw.decode_content == True

    # now we have to open a file using wb permission. 
    with open(filename, 'wb') as f:
        # with keyword is just a replace ment of try: Finaly: statements
        shutil.copyfileobj(r.raw, f)
    # now we have successfully downloaded the image we just have to give the indication that
    # image has been downloaded
    print("The Image has been successfully downloaded with name :  ", filename)
else:
    print("Ths Image could't be retrived")
