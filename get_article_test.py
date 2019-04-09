from mocks import * 
import requests
from io import BytesIO

import json

def test_http_return(monkeypatch):
	results="Paris [pa.ʁi]  est la capitale de la France. Elle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la Marne et l'Oise. Ses habitants s’appellent les Parisiens."

	def mockreturn(request):
		return json.dumps(results)

	monkeypatch.setattr(requests,'get',mockreturn)
	assert Search.get_article('Paris') is not None