#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import logging
from flask import Flask
from flask_apscheduler import APScheduler

import config
from config import basedir


scheduler = APScheduler()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from models import db
    db.app = app
    db.init_app(app)

    scheduler.init_app(app)
    print scheduler.get_jobs()

    return app


app = create_app()


# 日志系统管理
handler = logging.FileHandler(os.path.join(basedir, 'log/app.log'), encoding='UTF-8')
logging_format = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s]-[%(module)s/%(filename)s-%(funcName)s()-%(lineno)s] - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


@app.route('/')
def hello_world():
    app.logger.info('Hello World')
    return 'Hello World!'


if __name__ == '__main__':
    # scheduler.start()
    app.run(debug=True)


