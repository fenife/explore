#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DatabaseConfig(object):
    MYSQL_DB = dict(
        host="",
        port=3306,
        username="",
        password="",
        dbname=""
    )
    # SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'.format(**MYSQL_DB)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')


class APSchedulerConfig(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'tasks:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        },
    ]

    SCHEDULER_API_ENABLED = True


class DevConfig(Config, APSchedulerConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'default': DevConfig,
    'dev': DevConfig
}

