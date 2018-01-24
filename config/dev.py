#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
from .base import basedir


# Flask config
DEBUG = True


# SQLAlchemy config
MYSQL_DB = dict(
    host="localhost",
    port=3306,
    username="root",
    password="root",
    dbname="tysql"
)

# 主表
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
# SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'.format(**MYSQL_DB)

# 副表
SQLALCHEMY_BINDS = {
    'tysql': 'mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'.format(**MYSQL_DB),
    # 'tysql': "sqlite:///" + os.path.join(basedir, 'tysql.sqlite'),

}

# APScheduler
SCHEDULER_API_ENABLED = True

