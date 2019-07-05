from flask import Flask,render_template,request,jsonify
from mocks import Search,Extract
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pages/home.html')



@app.route('/processing')
def get_information():
	
	client_answer=request.args.get('a','Pas de réponse reçue', type=str)
	title=Search().get_title_article(client_answer)
	article=Search().get_article(**title)
	extract=Extract().extract_article(**article)

	return jsonify(result=extract)

@app.route('/formulaire')
def get_data():

	return render_template('pages/formulaire2.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
