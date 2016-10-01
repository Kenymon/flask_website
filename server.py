from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template( 'header.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template( 'error_404.html')






