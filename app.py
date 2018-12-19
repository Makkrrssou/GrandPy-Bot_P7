from flask import Flask,render_template,request,jsonify
from mocks import Search
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pages/home.html')



@app.route('/processing')
def get_information():
	
	extr=request.args.get('a','Pas de réponse reçue', type=str)
	aws=Search.get_article(extr)

	return jsonify(result=aws)

@app.route('/formulaire')
def get_data():

	return render_template('pages/formulaire2.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
