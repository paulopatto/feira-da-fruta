#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ft=python

import os

from flask import Flask
from flask import abort
from flask import json
from flask import request as Request
from flask import url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = True

# Database config
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# See https://github.com/kofrasa/flask-activerecord
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Manager config
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class FreeFair(db.Model):

    __tablename__ = 'free_fairs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    original_id = db.Column(db.Integer, index=True)

    sensus_sector = db.Column(db.String(15))

    weighted_area = db.Column(db.String(13))

    district_code = db.Column(db.String(9))
    district_name = db.Column(db.String(18))

    sub_city_hall = db.Column(db.String(25))

    city_region = db.Column(db.String(6))
    city_sub_region = db.Column(db.String(7))

    name = db.Column(db.String(30), index=True)
    code = db.Column(db.String(8), index=True)

    """
    Dados referentes a endereço
    """
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    address_street = db.Column(db.String(50))
    address_number = db.Column(db.String(5))
    address_neighborhood = db.Column(db.String(20))
    address_ref = db.Column(db.String(24))

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, attributes):
        self.original_id = attributes['id']
        self.sensus_sector = attributes['setcens']
        self.weighted_area = attributes['areap']
        self.district_code = attributes['coddist']
        self.district_name = attributes['distrito']
        self.sub_city_hall = attributes['subpref']
        self.city_region = attributes['regiao5']
        self.city_sub_region = attributes['regiao8']
        self.name = attributes['nome_feira']
        self.code = attributes['registro']
        self.lon = attributes['lon']
        self.lat = attributes['lat']
        self.address_street = attributes['logradouro']
        self.address_nighborhood = attributes['bairro']
        self.address_number = attributes['numero']
        self.address_ref = attributes['referencia']

@app.route("/api/v1/free-fairs")
def list():
    return "{}"

@app.route('/api/v1/free-fair/<id>')
def show(id):
    return "{ show: 'free fair' }"

@app.route("/api/v1/free-fair", methods=['POST'])
def create():
    if not Request.json:
        abort(400)

    params = Request.json
    free_fair = FreeFair(params)

    #move to Model.save
    #add timestamps
    db.session.add(free_fair)
    db.session.commit()
    #import code; code.interact(local=dict(globals(), **locals()))

    response = app.response_class(
        response = json.dumps(params),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/api/v1/free-fair/<id>', methods=['PATCH'])
def edit(id):
    return ""
@app.route('/api/v1/free-fair/<id>', methods=['DELETE'])
def delete(id):
    return "drop"

with app.test_request_context():
    print "\n\n"
    print "======================="
    print "FROM reource :free_fair"
    print "======================="
    print "GET    \t", url_for('list'),  "\t #index"
    print "GET    \t", url_for('show', id=':id'), "\t #show"
    print "POST   \t", url_for('create'), "\t #create"
    print "PATCH  \t", url_for('edit', id=':id'), "\t #edit"
    print "DELETE \t", url_for('delete', id=':id'), "\t #delete"


if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port = PORT)
    manager.run()
