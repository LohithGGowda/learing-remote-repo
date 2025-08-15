# filepath: c:\Users\lohit\OneDrive\Desktop\Learn Python\app.py
from flask import Flask, render_template_string, request

app = Flask(__name__)

def age(x):
    if x <= 10:
        return "Hello, World!"
    else:
        return "Age is greater than 10."

@app.route('/', methods=['GET', 'POST'])
def hello():
    message = ""
    if request.method == 'POST':
        try:
            x = int(request.form['age'])
            message = age(x)
        except ValueError:
            message = "Please enter a valid number."
    return render_template_string('''
        <form method="post">
            Enter age: <input name="age" type="number">
            <input type="submit">
        </form>
        <h1>{{ msg }}</h1>
    ''', msg=message)

if __name__ == '__main__':
    app.run()