from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # render_template takes two parameters: html template and message
    return render_template("app4.html", message = "Enter your name: ")

@app.route('/greet', methods=['POST'])
def greet():
    # Go to form and pull the value from 'name' from the html file.
    user_name = request.form["name"]
    return f"Hello, {user_name}"



# To run the app
if __name__=="__main__":
    app.run(debug = True, host = "127.0.0.1", port = 5001)

