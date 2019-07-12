
import requests
import json
import stop_words as s 


class Search():


    @classmethod
    def get_title_article(self, keyword):

        self.url1="https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&utf8&format=json"

        self.title=requests.get(self.url1.format(keyword)).json()



        return self.title

    @classmethod   
    def get_article(self,title):

        
        self.url2='https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=2&format=json&explaintext'
        self.article=requests.get(self.url2.format(title)).json()
    


        return self.article


    @classmethod
    def extract_title(self,**foo):

        self.article_title=foo['query']['search']

        self.title=self.article_title[0]['title']

        return self.title

    @classmethod
    def extract_article(self,**article):

        for key in article['query']['pages'].keys():
            article_key=key 

        self.extract=article['query']['pages'][key]['extract']

        return self.extract

class Parse():

    @classmethod
    def extract_answer(self,answer):
        
        self.keywords=answer.split()
        self.sentence=None
        # for keyword in self.keywords:
        #     if keyword.lower() in s.stop_words:
        #         self.keywords.remove(keyword)
        for keyword in self.keywords:
            if keyword.lower() not in s.stop_words:
                self.sentence=keyword+' '

        return self.sentence

class Location():

    @classmethod
    def get_place(self,keyword):

        self.url_place='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry&key=AIzaSyD4oIexrzcN8LaIRaxszGHPMgRgPLCPxNE'
        self.place=requests.get(self.url_place.format(keyword)).json()

        return self.place

    @classmethod
    def extract_address(self,**place):

        self.address=place['candidates'][0]['formatted_address']

        return self.address 

    def extract_coords(self,**place):

        self.coords=dict()
        lat=place['candidates'][0]['geometry']['location']['lat']
        lng=place['candidates'][0]['geometry']['location']['lng']
        self.coords['lat']=lat
        self.coords['lng']=lng

        return self.coords









