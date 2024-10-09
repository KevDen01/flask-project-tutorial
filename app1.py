from flask import Flask

# Convert current file into an application instance
app = Flask(__name__)

# Whenever i provide '/', run def home() function
@app.route('/')
def home():
    return "Hello World"

# Code runs only if the script is executed directly, not when imported as a module.
if __name__=="__main__":
    app.run(debug=True, host = "127.0.0.1", port = 5001) # http://localhost:5000/