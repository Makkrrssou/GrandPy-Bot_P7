from urllib import request
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



class Extract():

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

    def get_address(self,keyword):

        self.url_place='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry&key=AIzaSyD4oIexrzcN8LaIRaxszGHPMgRgPLCPxNE'
        self.place=request.urlopen(self.url_place.format(keyword))





