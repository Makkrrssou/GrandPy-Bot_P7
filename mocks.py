import requests


class Search():


    @classmethod
    def get_article(self, keyword):

        self.url1="https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&utf8&format=json"
        self.url2='https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=3&format=json&explaintext'


        '''recherche de tous les articles similaires au mot-clef saisi au format json'''
        self.r=requests.get(self.url1.format(keyword)).json()

        '''Extraction du titre du premier article'''

        self.title=self.r['query']['search'][0]['title']

        '''Récupération du premier article'''

        self.article=requests.get(self.url2.format(self.title)).json()


        for art in self.article['query']['pages'].keys():
            self.pageid=art

        self.text = self.article['query']['pages'][self.pageid]['extract']

        return self.text