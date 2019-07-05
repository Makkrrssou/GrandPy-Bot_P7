from mocks import * 
import urllib
from io import BytesIO

import json

def test_http_return_title(monkeypatch):
	results={
			'batchcomplete': '', 
			'continue': {
					'sroffset': 10, 'continue': '-||'}, 
			'query': {
					'searchinfo': {
								'totalhits': 366886}
					}
			}
			 

	def mockreturn(request):
		return BytesIO(json.dumps(results).encode())

	monkeypatch.setattr(urllib.request,'urlopen',mockreturn)
	assert Search().get_title_article('Paris') == results

