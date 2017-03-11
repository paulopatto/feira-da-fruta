#!/usr/bin/env python
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


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    sub_regions = db.relationship('SubRegion', backref='region', lazy='dynamic')


class SubRegion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    districts = db.relationship('District',
                                backref='sub_region',
                                lazy='dynamic'
                                )


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    sub_region_id = db.Column(db.Integer, db.ForeignKey('sub_region.id'))
    free_fairs = db.relationship('FreeFair', backref='district', lazy='dynamic')


class FreeFair(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    code = db.Column(db.String(8))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))


if __name__ == '__main__':
    manager.run()
