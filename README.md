# Flask Hands-On Tutorial

This project is a step-by-step guide to building simple Flask applications. It covers creating Flask apps, adding routes, handling requests, working with templates, custom error handling, and more.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Creating Flask Apps](#creating-flask-apps)
  - [Basic App (app1.py)](#basic-app-app1py)
  - [Handling Dynamic Routes (app2.py)](#handling-dynamic-routes-app2py)
  - [Working with Templates (app3.py)](#working-with-templates-app3py)
  - [Handling Forms (app4.py)](#handling-forms-app4py)
  - [Custom 404 Page (app5.py)](#custom-404-page-app5py)
  - [Adding Static Files (app6.py)](#adding-static-files-app6py)
  - [Redirection (app7.py)](#redirection-app7py)
- [Running the Apps](#running-the-apps)

## Prerequisites
- Python 3.x
- Flask (installed via pip)
- A code editor like Visual Studio Code
- Basic knowledge of Python and web development

## Setup

### Create a Project Directory
Open Visual Studio Code and create a folder called `flask-project-tutorial` (for example).

### Create a Virtual Environment
In the terminal, create and activate a virtual environment:
```bash
python -m venv flask-venv
.\flask-venv\Scripts\activate  # Windows
```

### Install Flask
Inside the virtual environment, install Flask:
```bash
pip install flask
```

### Create Requirements File
Save installed packages to `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## Creating Flask Apps

### Basic App (app1.py)
Create your first Flask app (`app1.py`):
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
```

### Handling Dynamic Routes (app2.py)
Add dynamic routes to handle user input via URLs:
```python
@app.route('/greet/<name>')
def greet(name):
    return f"Good morning, {name}."
```

### Working with Templates (app3.py)
Render HTML templates using Jinja2:
```python
@app.route('/')
def home():
    return render_template('app3.html', message="Welcome to Flask with templates!")
```

### Handling Forms (app4.py)
Capture form input and display it dynamically:
```python
@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['name']
    return f"Hello, {user_name}"
```

### Custom 404 Page (app5.py)
Customize the 404 error page:
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('app5.html'), 404
```

### Adding Static Files (app6.py)
Use static files for styling (e.g., CSS):
```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

### Redirection (app7.py)
Implement URL redirection based on user roles:
```python
@app.route('/user/<name>')
def user_identification(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', name=name))
```

## Running the Apps
Activate the virtual environment:
```bash
.\flask-venv\Scripts\activate
```
Run any of the apps (e.g., `app1.py`):
```bash
python app1.py
```
Access the app in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000), or at [http://127.0.0.1:5001](http://127.0.0.1:5001), depending on how you've configured your project.
