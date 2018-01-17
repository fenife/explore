#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64))

    def __repr__(self):
        return '<Post %r>' % self.title


def create_data():
    print 'start'
    db.create_all()

    admin = Role(name='Admin')
    guest = Role(name='Guest')
    user = Role(name='User')

    u1 = User(username='u1', role=admin)
    u2 = User(username='u2', role=guest)
    u3 = User(username='u3', role=user)

    db.session.add_all([admin, guest, user])
    db.session.add_all([u1, u2, u3])

    db.session.commit()
    db.session.close()
    print 'success'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    create_data()
    app.run()


