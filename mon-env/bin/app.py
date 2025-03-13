from bottle import Bottle,run

app = Bottle()

@app.route("/")
def index():
 return "Bonjour, microframework Bottle"

if __name__ == "__main__":
 run(app, host="localhost", port=8080, reloader=True)
