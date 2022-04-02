# https://www.geeksforgeeks.org/flask-creating-first-simple-application/

from flask import Flask

app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello():
    return 'Hello World!'


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    # app.run(host='0.0.0.0', debug=True)
    app.run()
