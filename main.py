from flask import Flask
from routes.user import user_bp

app =Flask(__name__)

@app.route("/")
def main():
	return "<h1>Ola mundo</h1>"

app.register_blueprint(user_bp, url_prefix='/user')

app.run(debug=True,port="4000")