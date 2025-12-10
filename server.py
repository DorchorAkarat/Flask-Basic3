from flask import Flask
import uuid
app = Flask(__name__)   

@app.route('/')
def home():
    return '''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask - Basic</title>
        </head>
        <body>
            <h1>Hello Flask!</h1>
            <hr>
            
        </body>
        </html>
    
'''

@app.route('/<name>')
def hello(name):
    return f"Hello {name}"


@app.route('/greeting/<name>/<int:age>')
def greeting(name, age):
    return f"<h1> Hello {name}, you are {age} years old.</h1>"

@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    return  f'<h1>{a} + {b} ={a + b} </h1>'

@app.route('/calculate/addition/<int:a>/<int:b>')
def subtracion(a, b):
    return  f'<h1>{a} - {b} ={a - b} </h1>'

@app.route('/secretkey/<uuid:secret_key>')
def secretkey(sk):
    return f'<h1>my secret key {sk} </h1>'
    



#if __name__ == '__main__':
#   app.run(debug=True)
