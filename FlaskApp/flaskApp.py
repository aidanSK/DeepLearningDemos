from flask import Flask, request
#pip install flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    #Retrieves parameters from URL, defaulting to None type if nothing is given
    condition = request.args.get('condition', None)

    if condition == None:
        return "No arguments given"
    elif condition == 'Rowan':
        return "Hello Rowan!"
    else:
        return "Hello World!"

#hostname: localhost
#default port: 8000
#url: localhost:8000/hello
#with params: localhost:8000/hello?option=0

if __name__ == '__main__':
    app.run(debug=False, port=8000, host="localhost")
