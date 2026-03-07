from flask import Flask

app =Flask(__name__)

@app.route("/")
def main():
	return "<h1>Ola mundo</h1>"

app.run(debug=True,port="4000")