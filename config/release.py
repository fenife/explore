#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import


# Flask config
DEBUG = True


# SQLAlchemy config
MYSQL_DB = dict(
    host="",
    port=3306,
    username="",
    password="",
    dbname=""
)

SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'.format(**MYSQL_DB)


# APScheduler
SCHEDULER_API_ENABLED = True
