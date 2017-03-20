#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ft=python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Manager config
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class FreeFairs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    original_id = db.Column(db.Integer)

    sensus_sector = db.Column(db.String(15))

    weighted_area = db.Column(db.String(13))

    district_code = db.Column(db.String(9))
    district_name = db.Column(db.String(18))

    sub_city_hall = db.Column(db.String(25))

    city_region = db.Column(db.String(6))
    city_sub_region = db.Column(db.String(7))

    name = db.Column(db.String(30))
    code = db.Column(db.String(8))

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


if __name__ == '__main__':
    manager.run()
