# flask_web/app.py

From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world:
    out = ( 
        f'Hey, we have Flask in a Docker container!<br>'
    )
    return out

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
