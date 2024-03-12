import pandas as pd
import time
import json

from bs4 import BeautifulSoup
from Grabber import Grabber
from Config import *

class Scrapper :
    def __init__(self) :
        self.baseurl = "https://ulas.surakarta.go.id"
        self.mainurl = self.baseurl + "/index.php?mod=widget&sub=semuaAspirasi&act=view&typ=html"

    def scrap(self) :
        grabber = Grabber(self.mainurl)
        params = {'content': 'aplikasi solo', 'collapse_status' : '0', 'opd' : '', 'pengadu' : '', 'status' : ''}
        main_content = grabber.postgrab(params)

        # Parse the HTML code using BeautifulSoup
        soup = BeautifulSoup(main_content, 'html.parser')

        # Extract the relevant information from the HTML code
        aspirations = []
        for a in soup.find_all('a', {'class':'color-asp-black'}, href=True):
            title = a.get_text()
            link = a['href']
            aspirations.append([title, link])

        # Store the information in a pandas dataframe
        df = pd.DataFrame(aspirations, columns=['Title', 'Link'])

        for index, row in df.iterrows():
            if index == 0 : 
                link = row['Link'].replace('%3D', '=')
                contentgrabber = Grabber(self.baseurl + link)
                print(self.baseurl + link)
                print(contentgrabber.getgrab())