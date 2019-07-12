from flask import Flask,render_template,request,jsonify
from mocks import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pages/home.html')



@app.route('/processing')
def get_information():
	
	client_answer=request.args.get('a','Pas de réponse reçue', type=str)
	keywords=Parse().extract_answer(client_answer)
	
	title_article=Search().get_title_article(keywords)
	title=Search().extract_title(**title_article)
	article=Search().get_article(title)
	extract=Search().extract_article(**article)
	
	place=Location().get_place(keywords)
	address=Location().extract_address(**place)
	coords=Location().extract_coords(**place)

	# message=extract+';'+address

	return jsonify(result=extract+';'+address+';'+str(coords['lat'])+';'+str(coords['lng']))

@app.route('/address')
def get_address():

	client_answer=request.args.get('a','Pas de réponse reçue', type=str)
	keywords=Parse().extract_answer(client_answer)


	return jsonify(result=address)

	

@app.route('/formulaire')
def get_data():

	return render_template('pages/formulaire2.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
