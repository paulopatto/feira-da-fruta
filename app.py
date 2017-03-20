import os

from flask import Flask
from flask import request as Request
from flask import abort
from flask import url_for
from flask import json

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# GET /
@app.route("/")
def index():
    return ""

# GET /free-fairs/
@app.route("/api/v1/free-fairs")
def list():
    return "{}"

# GET /free-fair/:id
@app.route('/api/v1/free-fair/<id>')
def show(id):
    return "{ show: 'free fair' }"

# POST /free-fair/
@app.route("/api/v1/free-fair", methods=['POST'])
def create():
    if not Request.json:
        abort(400)

    #import code; code.interact(local=dict(globals(), **locals()))

    params = Request.json

    print("Criando a feira: ", params['name'])

    response = app.response_class(
        response = json.dumps(params),
        status = 200,
        mimetype = 'application/json'
    )
    return response


# PATCH /free-fair/:id
@app.route('/api/v1/free-fair/<id>', methods=['PATCH'])
def edit(id):
    return ""
# DELETE /free-fair/:id
@app.route('/api/v1/free-fair/<id>', methods=['DELETE'])
def delete(id):
    return "drop"

with app.test_request_context():
    print "\n"
    print "======================="
    print "FROM reource :free_fair"
    print "======================="
    print "GET    \t", url_for('list'),  "\t #index"
    print "GET    \t", url_for('show', id=':id'), "\t #show"
    print "POST   \t", url_for('create'), "\t #create"
    print "PATCH  \t", url_for('edit', id=':id'), "\t #edit"
    print "DELETE \t", url_for('delete', id=':id'), "\t #delete"

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = PORT)
