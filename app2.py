from flask import Flask

# Convert current file into an application instance
app = Flask(__name__)

# Checks URL, then runs one function or the other.
# Whenever i provide '/', run def home() function
@app.route('/') # http://localhost:5001/
def home():
    return "Hello World"

# Checks URL, then runs one function or the other.
# Sees /greet/<name> and runs def greet() function
@app.route('/greet/<name>') # http://localhost:5001/greet/kevin
def greet(name):
    return f"Good morning {name} "

@app.route('/request/<int:id>') # By default string, specify to expect integer.
def show_request(id):
    return f"Integer number is: {id}."

@app.route('/request/<id>') # Uses this one if input is a string.
def show_name(id):
    return f"Name is: {id}."

@app.route('/request/<float:id>') # Here the id is a float
def show_float(id):
    return f"Float number is: {id}."

# Code runs only if the script is executed directly, not when imported as a module.
if __name__=="__main__":
    app.run(debug=True, host = "127.0.0.1", port = 5001) # http://localhost:5001/