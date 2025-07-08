from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Welcome system admin</h1>"

@app.route("/how-are-you")
def hello():
    return "I am good, how about you?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # ← Change here
