from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
	return Response("hi this is from flask app")

if __name__ == "__main__":
	app.run("0.0.0.0", port=8080, debug=True)
