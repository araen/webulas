import requests

class Grabber :
    def __init__(self, url) :
        self.url = url

    def postgrab(self, params) :
        # Send an HTTP POST request to the website
        response = requests.post(self.url, data = params)
        return response.text
    
    def getgrab(self) :
        # Send an HTTP GET request to the website
        response = requests.get(self.url)
        return response.text