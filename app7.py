# REDIRECTION OF URLs

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<name>')
def hello_guest(name):
    return f"Hello, {name}. Entered as guest."

@app.route('/user/<name>')
def user_identification(name):
    if name == "admin":  # /user/admin
        return redirect(url_for('hello_admin'))
    else: # anything that's not admin
        return redirect(url_for('hello_guest', name = name))

@app.errorhandler(404)
def page_not_found(e): # e is the error message return by the error handler
    return render_template('app5.html')


if __name__=="__main__":
    app.run(debug = True, host = "127.0.0.1", port = 5001)


# url_for("hello_admin") # provides respective url for the function


