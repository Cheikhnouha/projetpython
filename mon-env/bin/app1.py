from bottle import Bottle,run

app = Bottle

@app.route("/hello")
def hello_bottle():
  return "hello bottle de cheikh barro"
if __name__ == "__main__":
 run(app, host= localhost, port= 8080, reloader=True)


