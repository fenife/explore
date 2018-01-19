#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
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
            'id': None,
            'func': 'tasks:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        },
        {
            'id': None,
            'func': 'tasks:task2',
            'args': None,
            'trigger': 'interval',
            'seconds': 10
        },
    ]

    SCHEDULER_JOBSTORES_URL = "sqlite:///" + os.path.join(basedir, 'task.db')
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SCHEDULER_JOBSTORES_URL)
    }

    SCHEDULER_API_ENABLED = True


class ConfigSet(BaseConfig, DatabaseConfig, APSchedulerConfig):
    pass


class DevConfig(ConfigSet):
    """ 开发环境配置 """
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


class TestConfig(ConfigSet):
    """ 测试环境配置 """
    pass


class ProductionConfig(ConfigSet):
    """ 生产环境配置 """
    pass


config = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'production': ProductionConfig,
}

