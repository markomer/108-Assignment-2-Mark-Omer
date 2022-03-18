from flask import Flask

app = Flask("Server")


@app.route("/")
def home():
  return "Hello from Flask"


@app.route("/me") # add /me to the URL
def about_me():
  return "Mark Omer"


app.run(debug=True)