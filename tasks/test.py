#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# from explore import db
from models import (Role, User, Post)
# from models import *

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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


def job1(a, b):
    print str(a) + ' ' + str(b)


def task2():
    print 'Hello World!'


if __name__ == '__main__':
    print 'tasks'
