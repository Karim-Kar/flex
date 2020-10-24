from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
@app.route('/home', methods=['post', 'get'])
def index():
	message = ''
	if request.method == 'POST':
		yesOrNo = request.form.get('YesOrNo')
		if yesOrNo == "yes":
			message = "Спасибо"
		elif yesOrNo == "no":
			message = "Пожалуйста помоги в продвижении канала"	
	return render_template('index.html', message=message)	
if __name__ == '__main__':
    app.run(debug=True)
