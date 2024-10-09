from flask import Flask, render_template

# render_template connects our apps with out html pages

# Convert this file into an app instance
app = Flask(__name__)

@app.route('/')
def home():
    # return my created html page and the message.
    return render_template('app3.html', message = "Welcome to the template-based flask app.")


if __name__=="__main__":
    app.run(debug = True, host = "127.0.0.1", port = 5001)